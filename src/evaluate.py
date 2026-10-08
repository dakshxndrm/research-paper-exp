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
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
from tqdm import tqdm

from src.config import load_config, set_seed
from src.llm import LLMClient

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


def retrieval_recall(retrieved: str, gold_concepts: Any) -> float:
    """Fraction of gold units retrieved. Substring match handles the fact that
    the baseline retrieves `doc.md#chunk3` while gold is written as `doc.md`."""
    if not isinstance(gold_concepts, str) or not gold_concepts.strip():
        return float("nan")
    gold = [g.strip().lstrip("/") for g in gold_concepts.split(";") if g.strip()]
    if not gold:
        return float("nan")
    got = (retrieved or "").lower()
    hits = sum(1 for g in gold if g.lower() in got)
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


def judge_rows(df: pd.DataFrame, cfg: Dict[str, Any], contexts: Dict[str, str]) -> List[str]:
    client = LLMClient(
        {
            "provider": cfg["judge"]["provider"],
            "model": cfg["judge"]["model"],
            "temperature": cfg["judge"]["temperature"],
            # Not 10: reasoning models spend the budget on hidden reasoning
            # before emitting the one-word label, and return empty content.
            "max_tokens": 300,
            "base_url": cfg["judge"]["base_url"],
            "api_key_env": cfg["generation"]["api_key_env"],
        }
    )
    labels: List[str] = []
    valid = {"supported", "unsupported", "contradicted", "abstained"}
    for _, row in tqdm(df.iterrows(), total=len(df), desc="judging"):
        key = f"{row['arm']}|{row['ablation']}|{row['qid']}"
        raw = client.generate(
            JUDGE_SYSTEM,
            JUDGE_USER.format(
                context=contexts.get(key, "[context not cached]"),
                question=row["question"],
                answer=row["answer"],
            ),
        )
        words = raw.strip().lower().split()
        token = words[0].strip(".,:") if words else ""
        labels.append(token if token in valid else "unparsed")
    return labels


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

    df = pd.read_csv(results_dir / args.input)
    print(f"Scoring {len(df)} rows.")

    df["answer"] = df["answer"].fillna("")
    df["abstained"] = df["answer"].str.upper().str.contains("INSUFFICIENT CONTEXT").astype(int)
    df["em"] = [exact_match(a, g) for a, g in zip(df["answer"], df["gold_answer"])]
    df["f1"] = [token_f1(a, g) for a, g in zip(df["answer"], df["gold_answer"])]
    df["retrieval_recall"] = [
        retrieval_recall(r, g) for r, g in zip(df["retrieved_ids"], df.get("gold_concepts", ""))
    ]
    df["citation_valid"] = [
        citation_valid(a, r) for a, r in zip(df["answer"], df["retrieved_ids"])
    ]

    if cfg["judge"]["enabled"] and not args.no_judge:
        # Re-derive contexts so the judge sees exactly what the generator saw.
        contexts = rebuild_contexts(cfg, df)
        df["judge_label"] = judge_rows(df, cfg, contexts)
    else:
        df["judge_label"] = "not_judged"

    df["hallucination"] = df["judge_label"].isin(["unsupported", "contradicted"]).astype(int)
    df["human_label"] = ""   # you fill this in
    df["human_notes"] = ""

    out = results_dir / args.input.replace("raw_", "scored_")
    df.to_csv(out, index=False)
    print(f"Scored -> {out}")

    if args.sample_for_human > 0:
        sample = df.sample(
            min(args.sample_for_human, len(df)), random_state=cfg["experiment"]["seed"]
        )
        cols = ["arm", "ablation", "qid", "question", "gold_answer", "answer",
                "judge_label", "human_label", "human_notes"]
        sample_path = results_dir / "human_labelling_sheet.csv"
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
