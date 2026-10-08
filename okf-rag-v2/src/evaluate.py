"""Stage 3 -- score the raw outputs.

Metrics:
  em                  exact match after normalisation
  f1                  token-overlap F1 against the gold answer
  retrieval_recall    fraction of gold concepts/sources present in the context
  citation_valid      every id in the SOURCES line actually appears in context
  abstained           model said INSUFFICIENT CONTEXT
  judge_label         supported | unsupported | contradicted   (LLM-as-judge)
  hallucination       1 if judge_label in {unsupported, contradicted}

IMPORTANT FOR THE PAPER: the LLM judge is a screening tool, not ground truth.
Hand-label a random sample of at least 50 rows yourself, report the judge's
agreement with your labels (Cohen's kappa), and report the HUMAN numbers as the
headline result. `--sample-for-human N` writes that sample out for you.
"""

from __future__ import annotations

import argparse
import re
import string
import unicodedata
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
from tqdm import tqdm

from src.config import append_row, done_keys, load_config, set_seed
from src.llm import LLMClient
from src.okf_pipeline import split_frontmatter

JUDGE_SYSTEM = """You are a strict evaluator of factual grounding.

Given a CONTEXT, a QUESTION, and an ANSWER, classify the ANSWER as exactly one of:

  supported     - every factual claim in the answer is stated in or directly
                  entailed by the context
  unsupported   - the answer contains at least one claim the context does not
                  state (added detail, invented specifics, outside knowledge)
  contradicted  - the answer conflicts with something the context states
  abstained     - the answer declines to answer for lack of information

Judge only grounding in the context. Do NOT judge whether the answer is correct
in the real world. Reply with one word from the list above and nothing else."""

JUDGE_USER = """CONTEXT:
{context}

QUESTION: {question}

ANSWER: {answer}

LABEL:"""

PUNCTUATION = set(string.punctuation)


def normalise(text: str) -> str:
    text = text.lower()
    # Strip Unicode punctuation too, not just ASCII. The generator emits typographic
    # characters (U+2011 non-breaking hyphen, U+2014 em dash) where a hand-written
    # gold_answer has plain "-", so "end-semester" and "end‑semester" would
    # otherwise count as different tokens and silently zero out EM.
    text = "".join(
        ch for ch in text
        if ch not in PUNCTUATION and not unicodedata.category(ch).startswith("P")
    )
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    return " ".join(text.split())


def strip_sources(answer: str) -> str:
    return re.split(r"\n?SOURCES\s*:", answer, maxsplit=1)[0].strip()


def parse_sources(answer: str) -> List[str]:
    m = re.search(r"SOURCES\s*:(.+)", answer, re.DOTALL)
    if not m:
        return []
    raw = m.group(1).replace("\n", " ")
    return [s.strip().strip("[]") for s in raw.split(",") if s.strip().strip("[]")]


def exact_match(pred: str, gold: str) -> int:
    return int(normalise(strip_sources(pred)) == normalise(gold))


def token_f1(pred: str, gold: str) -> float:
    p = normalise(strip_sources(pred)).split()
    g = normalise(gold).split()
    if not p or not g:
        return float(p == g)
    common = Counter(p) & Counter(g)
    overlap = sum(common.values())
    if overlap == 0:
        return 0.0
    precision = overlap / len(p)
    recall = overlap / len(g)
    return 2 * precision * recall / (precision + recall)


@lru_cache(maxsize=4)
def doc_to_concepts(bundle_dir: str) -> Dict[str, tuple]:
    """source document filename -> concept paths extracted from it.

    Derived from each concept's `resource: source://<doc>` frontmatter, which
    write_bundle() records for exactly this purpose. Nothing is hardcoded, so a
    rebuilt or re-scoped corpus keeps working. Cached because evaluate scores
    every row against the same bundle.
    """
    mapping: Dict[str, List[str]] = {}
    root = Path(bundle_dir)
    for path in sorted(root.rglob("*.md")):
        meta, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        doc = str(meta.get("resource", "")).replace("source://", "").strip()
        if doc:
            mapping.setdefault(doc.lower(), []).append(
                path.relative_to(root).as_posix()
            )
    return {k: tuple(v) for k, v in mapping.items()}


def expand_gold_to_concepts(gold_doc_names: Any, bundle_dir: str) -> List[str]:
    """Every bundle concept path extracted from the named source documents.

    questions.csv writes gold in the SOURCE DOCUMENT namespace ("architecture.md")
    because that is what a human authoring gold answers can reasonably name. The
    OKF arm reports concept paths ("definition/kubernetes_architecture.md"). This
    bridges the two without editing the human-authored file.
    """
    if not isinstance(gold_doc_names, str) or not gold_doc_names.strip():
        return []
    mapping = doc_to_concepts(bundle_dir)
    out: List[str] = []
    for doc in gold_doc_names.split(";"):
        out.extend(mapping.get(doc.strip().lstrip("/").lower(), ()))
    return out


def retrieval_recall(retrieved: str, gold_concepts: Any,
                     bundle_dir: str | None = None) -> float:
    """Fraction of gold units retrieved.

    A gold document counts as retrieved if EITHER:
      * its name appears in `retrieved` -- the chunk baseline reports
        `doc.md#chunk3`, so a plain substring test already works there; or
      * any concept the bundle extracted from that document appears -- the OKF
        arm reports `type_slug/title_slug.md`, which shares no substring with
        the document name at all.

    The first test runs first and short-circuits, and a concept path always
    contains "/" while a chunk id never does, so the chunk arm's numbers are
    provably unchanged by the second branch.

    KNOWN LIMITATION -- this is deliberately LOOSE. "architecture.md" expands to
    all 9 concepts extracted from it, so a single-hop question about one fact in
    that document scores a hit on ANY of the 9, not only the concept that
    actually answers it. Recall is therefore an OPTIMISTIC upper bound for the
    OKF arm. It is still far better than the alternative it replaces, which was
    a hard 0.0 on every answerable question regardless of what was retrieved --
    a measurement artefact, not a result. Tightening this needs per-question
    concept-level gold, which only a human can author.
    """
    if not isinstance(gold_concepts, str) or not gold_concepts.strip():
        return float("nan")
    gold = [g.strip().lstrip("/") for g in gold_concepts.split(";") if g.strip()]
    if not gold:
        return float("nan")
    got = (retrieved or "").lower()

    hits = 0
    for g in gold:
        if g.lower() in got:
            hits += 1
        elif bundle_dir and any(
            c.lower() in got for c in expand_gold_to_concepts(g, bundle_dir)
        ):
            hits += 1
    return hits / len(gold)


def _canonical_id(unit_id: str) -> str:
    """Strip the decoration the OKF renderer adds around a concept path.

    Blocks are rendered as `[concept: /policies/x.md]`, so the model cites
    `/policies/x.md` while retrieved_ids stores `policies/x.md`. Without folding
    the prefix and leading slash, every OKF citation scores invalid and the arm
    reports citation_valid = 0.0, which is a measurement artefact, not a result.
    """
    return re.sub(r"^concept\s*:\s*", "", unit_id.strip().lower()).lstrip("/")


def citation_valid(answer: str, retrieved: str) -> float:
    cited = parse_sources(answer)
    if not cited:
        return float("nan")
    pool = _canonical_id(retrieved or "")
    return sum(1 for c in cited if _canonical_id(c) in pool) / len(cited)


def make_judge(cfg: Dict[str, Any]) -> LLMClient:
    return LLMClient(
        {
            "model": cfg["judge"]["model"],
            "temperature": cfg["judge"]["temperature"],
            # Not 10: reasoning models spend the budget on hidden reasoning
            # before emitting the one-word label, and return empty content.
            "max_tokens": cfg["judge"].get("max_tokens", 300),
            "base_url": cfg["judge"]["base_url"],
            "api_key_env": cfg["generation"]["api_key_env"],
            # None unless a config sets judge.reasoning_effort -- no-op today
            # (qwen2.5:7b-instruct is not a reasoning model), here for parity
            # with build_bundle.make_client if the judge ever becomes one.
            "reasoning_effort": cfg["judge"].get("reasoning_effort"),
            "seed": cfg["judge"].get("seed"),
        }
    )


VALID_LABELS = {"supported", "unsupported", "contradicted", "abstained"}


def judge_row(client: LLMClient, row: Any, context: str) -> str:
    raw = client.generate(
        JUDGE_SYSTEM,
        JUDGE_USER.format(context=context, question=row["question"], answer=row["answer"]),
    )
    words = raw.strip().lower().split()
    token = words[0].strip(".,:") if words else ""
    return token if token in VALID_LABELS else "unparsed"


def main() -> None:
    parser = argparse.ArgumentParser(description="Score raw experiment outputs.")
    parser.add_argument("--input", required=True, help="Filename inside results/.")
    parser.add_argument("--no-judge", action="store_true")
    parser.add_argument("--sample-for-human", type=int, default=60,
                        help="Rows to export for manual labelling.")
    parser.add_argument("--config", default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    set_seed(cfg["experiment"]["seed"])
    results_dir = Path(cfg["paths"]["results"])

    out = results_dir / args.input.replace("raw_", "scored_")

    df = pd.read_csv(results_dir / args.input)
    # Resume: rows already scored are kept as they are. Delete the scored file to
    # force a clean rescore -- a resumed run keeps labels produced by whatever
    # judge settings were in force when they were written.
    done = done_keys(out, ["arm", "ablation", "qid"])
    if done:
        keep = [
            (str(a), str(b), str(c)) not in done
            for a, b, c in zip(df["arm"], df["ablation"], df["qid"])
        ]
        print(f"Resuming {out.name}: {len(done)} rows already scored.")
        df = df[keep].reset_index(drop=True)
    print(f"Scoring {len(df)} rows.")

    if not df.empty:
        df["answer"] = df["answer"].fillna("")
        df["abstained"] = df["answer"].str.upper().str.contains("INSUFFICIENT CONTEXT").astype(int)
        df["em"] = [exact_match(a, g) for a, g in zip(df["answer"], df["gold_answer"])]
        df["f1"] = [token_f1(a, g) for a, g in zip(df["answer"], df["gold_answer"])]
        # bundle_dir lets gold expand from the source-document namespace that
        # questions.csv is authored in into the concept paths the OKF arm
        # reports. Chunk-arm rows are unaffected -- see retrieval_recall.
        bundle_dir = cfg["paths"]["bundle"]
        df["retrieval_recall"] = [
            retrieval_recall(r, g, bundle_dir)
            for r, g in zip(df["retrieved_ids"], df.get("gold_concepts", ""))
        ]
        df["citation_valid"] = [
            citation_valid(a, r) for a, r in zip(df["answer"], df["retrieved_ids"])
        ]

        judging = cfg["judge"]["enabled"] and not args.no_judge
        # Re-derive contexts so the judge sees exactly what the generator saw.
        contexts = rebuild_contexts(cfg, df) if judging else {}
        client = make_judge(cfg) if judging else None

        for _, row in tqdm(df.iterrows(), total=len(df), desc="scoring"):
            key = f"{row['arm']}|{row['ablation']}|{row['qid']}"
            label = (
                judge_row(client, row, contexts.get(key, "[context not cached]"))
                if judging else "not_judged"
            )
            append_row(
                {
                    **row.to_dict(),
                    "judge_label": label,
                    "hallucination": int(label in ("unsupported", "contradicted")),
                    "human_label": "",   # you fill this in
                    "human_notes": "",
                },
                out,
            )

    print(f"Scored -> {out}")

    if args.sample_for_human > 0:
        # Read back so the sheet samples the whole scored file, resumed rows included.
        scored = pd.read_csv(out)
        sample = scored.sample(
            min(args.sample_for_human, len(scored)), random_state=cfg["experiment"]["seed"]
        )
        cols = ["arm", "ablation", "qid", "question", "gold_answer", "answer",
                "judge_label", "human_label", "human_notes"]
        # Named after the scored file it came from. A single fixed name meant
        # every later evaluate.py run silently clobbered someone's finished
        # labelling, which is exactly what happened to the OKF sheet here.
        sample_path = results_dir / f"human_labels_{out.stem.removeprefix('scored_')}.csv"
        if sample_path.exists():
            existing = pd.read_csv(sample_path)
            if existing.get("human_label", pd.Series(dtype=str)).fillna("").astype(str).str.strip().any():
                sample_path = sample_path.with_name(sample_path.stem + "_REGENERATED.csv")
                print(f"[warn] existing sheet has labels in it -- writing {sample_path.name} "
                      f"instead of overwriting your work.")
        sample[cols].to_csv(sample_path, index=False)
        print(f"Manual-labelling sheet -> {sample_path}")
        print("Fill the human_label column with: supported / unsupported / "
              "contradicted / abstained")


def rebuild_contexts(cfg: Dict[str, Any], df: pd.DataFrame) -> Dict[str, str]:
    """Reconstruct each row's retrieval context for the judge.

    Retrieval is deterministic (fixed embeddings, no sampling), so re-running it
    reproduces the exact context the generator saw.
    """
    from src.chunk_pipeline import ChunkRAG
    from src.okf_pipeline import OKFRag
    from src.run_experiment import ABLATIONS

    contexts: Dict[str, str] = {}
    for (arm, ablation), group in df.groupby(["arm", "ablation"]):
        retriever = (
            ChunkRAG(cfg) if arm == "chunk" else OKFRag(cfg, ABLATIONS.get(ablation, {}))
        )
        for _, row in group.iterrows():
            contexts[f"{arm}|{ablation}|{row['qid']}"] = retriever.retrieve(
                str(row["question"])
            )["context"]
    return contexts


if __name__ == "__main__":
    main()
