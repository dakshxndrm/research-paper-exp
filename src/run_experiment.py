"""Stage 2 -- run both arms over the question set and record raw outputs.

Design constraints that keep the comparison valid:
  - identical generator model, prompt, temperature (0.0), and seed
  - identical context token budget
  - only the retrieval substrate differs

Usage:
    python -m src.run_experiment                       # main run, both arms
    python -m src.run_experiment --arms okf            # single arm
    python -m src.run_experiment --ablation no_expansion
    python -m src.run_experiment --limit 5             # smoke test
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
from tqdm import tqdm

from src.chunk_pipeline import ChunkRAG
from src.config import ensure_dir, load_config, set_seed
from src.llm import LLMClient
from src.okf_pipeline import OKFRag

SYSTEM_PROMPT = """You answer questions using ONLY the provided context.

Rules:
1. If the context contains the answer, answer concisely in 1-3 sentences.
2. After your answer, add a line starting with "SOURCES:" listing the bracketed
   identifiers of every context block you actually used, comma-separated.
3. If the context does not contain enough information to answer, reply exactly:
   INSUFFICIENT CONTEXT
   Do not guess. Do not use knowledge from outside the context.
4. Never contradict the context. Never add facts the context does not state."""

USER_PROMPT = """CONTEXT:
{context}

QUESTION: {question}

ANSWER:"""

# Ablation presets. Each overrides retrieval.okf settings for Arm B.
ABLATIONS: Dict[str, Dict[str, Any]] = {
    "full": {},
    "no_expansion": {"hop_expansion": 0},
    "no_freshness": {"use_freshness_filter": False},
    "with_freshness": {"use_freshness_filter": True},
    "embed_full_body": {"embed_field": "full_body"},
    "two_hop": {"hop_expansion": 2, "max_expanded": 8},
}


def load_questions(path: str, limit: int | None = None) -> pd.DataFrame:
    df = pd.read_csv(path)
    required = {"qid", "question", "gold_answer", "hop_type"}
    missing = required - set(df.columns)
    if missing:
        raise SystemExit(f"questions.csv is missing columns: {sorted(missing)}")
    df = df.dropna(subset=["question", "gold_answer"])
    return df.head(limit) if limit else df


def run_arm(name: str, retriever, questions: pd.DataFrame, client: LLMClient,
            tag: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for _, q in tqdm(questions.iterrows(), total=len(questions), desc=f"{name}/{tag}"):
        t0 = time.perf_counter()
        r = retriever.retrieve(str(q["question"]))
        t_retrieve = time.perf_counter() - t0

        t0 = time.perf_counter()
        answer = client.generate(
            SYSTEM_PROMPT,
            USER_PROMPT.format(context=r["context"], question=q["question"]),
        )
        t_generate = time.perf_counter() - t0

        rows.append(
            {
                "arm": name,
                "ablation": tag,
                "qid": q["qid"],
                "question": q["question"],
                "gold_answer": q["gold_answer"],
                "hop_type": q["hop_type"],
                "gold_concepts": q.get("gold_concepts", ""),
                "answer": answer,
                "retrieved_ids": "|".join(r["retrieved_ids"]),
                "n_units": r["n_units"],
                "n_seed": r.get("n_seed", r["n_units"]),
                "n_expanded": r.get("n_expanded", 0),
                "context_tokens": r["context_tokens"],
                "retrieve_s": round(t_retrieve, 4),
                "generate_s": round(t_generate, 4),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the OKF-RAG comparison.")
    parser.add_argument("--arms", nargs="+", default=["chunk", "okf"],
                        choices=["chunk", "okf"])
    parser.add_argument("--ablation", default="full", choices=list(ABLATIONS))
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--config", default=None)
    parser.add_argument("--out", default=None, help="Override output filename.")
    args = parser.parse_args()

    cfg = load_config(args.config)
    set_seed(cfg["experiment"]["seed"])

    questions = load_questions(cfg["paths"]["questions"], args.limit)
    print(f"Loaded {len(questions)} questions.")

    client = LLMClient(cfg["generation"])
    rows: List[Dict[str, Any]] = []

    if "chunk" in args.arms and args.ablation == "full":
        # The baseline has no OKF knobs, so it only runs in the main condition.
        rag = ChunkRAG(cfg)
        print(f"Baseline index: {rag.unit_count} chunks.")
        rows += run_arm("chunk", rag, questions, client, "full")

    if "okf" in args.arms:
        okf = OKFRag(cfg, ABLATIONS[args.ablation])
        print(f"OKF index: {okf.unit_count} concepts (ablation={args.ablation}).")
        rows += run_arm("okf", okf, questions, client, args.ablation)

    results_dir = ensure_dir(cfg["paths"]["results"])
    name = args.out or f"raw_{cfg['experiment']['name']}_{args.ablation}.csv"
    out_path = Path(results_dir) / name
    pd.DataFrame(rows).to_csv(out_path, index=False)

    meta = {
        "config": cfg,
        "ablation": args.ablation,
        "n_questions": len(questions),
        "arms": args.arms,
    }
    (Path(results_dir) / f"runmeta_{args.ablation}.json").write_text(
        json.dumps(meta, indent=2, default=str), encoding="utf-8"
    )

    print(f"\nRaw outputs -> {out_path}")
    print("Next: python -m src.evaluate --input", out_path.name)


if __name__ == "__main__":
    main()
