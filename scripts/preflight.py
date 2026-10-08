"""Preflight check. Run this BEFORE any long experiment.

Verifies: dependencies importable, LLM provider reachable, embedding model
downloadable, corpus present, question file well-formed.

    python scripts/preflight.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

OK, FAIL, WARN = "  [ok]  ", "  [FAIL]", "  [warn]"
problems = 0


def check(label: str, fn) -> None:
    global problems
    try:
        detail = fn()
        print(f"{OK} {label}" + (f" -- {detail}" if detail else ""))
    except Exception as exc:  # noqa: BLE001
        problems += 1
        print(f"{FAIL} {label} -- {exc}")


def main() -> None:
    print("OKF-RAG preflight\n" + "=" * 50)

    def deps():
        import matplotlib, numpy, pandas, requests, sentence_transformers, yaml  # noqa: F401
        import frontmatter  # noqa: F401
        return "all imports fine"

    check("Python dependencies", deps)

    from src.config import load_config

    cfg = load_config()

    def corpus():
        raw = Path(cfg["paths"]["raw_docs"])
        docs = [p for p in raw.rglob("*") if p.suffix.lower() in {".md", ".txt"}]
        if not docs:
            raise RuntimeError(f"no .md/.txt files in {raw}")
        words = sum(len(p.read_text(errors='ignore').split()) for p in docs)
        if len(docs) < 20:
            print(f"{WARN} only {len(docs)} docs -- aim for 30-50")
        return f"{len(docs)} docs, ~{words:,} words"

    check("Raw corpus", corpus)

    def questions():
        import pandas as pd

        df = pd.read_csv(cfg["paths"]["questions"])
        need = {"qid", "question", "gold_answer", "hop_type"}
        if not need <= set(df.columns):
            raise RuntimeError(f"missing columns {sorted(need - set(df.columns))}")
        if df["qid"].duplicated().any():
            raise RuntimeError("duplicate qid values")
        if df["notes"].astype(str).str.contains("EXAMPLE ROW").any():
            print(f"{WARN} example rows still present -- replace them")
        multi = (df["hop_type"] == "multi").sum()
        if multi < 15:
            print(f"{WARN} only {multi} multi-hop questions -- aim for 20+")
        return f"{len(df)} questions ({multi} multi-hop)"

    check("Question set", questions)

    def embedder():
        from src.embeddings import encode

        v = encode(["preflight test sentence"], cfg["embedding"]["model"])
        return f"{cfg['embedding']['model']}, dim={v.shape[1]}"

    check("Embedding model", embedder)

    def generator():
        from src.llm import LLMClient

        out = LLMClient(cfg["generation"]).generate(
            "Reply with exactly: PONG", "ping"
        )
        return f"{cfg['generation']['provider']}/{cfg['generation']['model']} -> {out[:40]!r}"

    check("Generator LLM", generator)

    def bundle():
        b = Path(cfg["paths"]["bundle"])
        files = [p for p in b.rglob("*.md") if p.name not in {"index.md", "log.md"}]
        if not files:
            raise RuntimeError("bundle empty -- run `python -m src.build_bundle` next")
        return f"{len(files)} concepts"

    check("OKF bundle", bundle)

    print("=" * 50)
    if problems:
        print(f"{problems} blocking problem(s). Fix before running the experiment.")
        sys.exit(1)
    print("All clear. Proceed to run_experiment.")


if __name__ == "__main__":
    main()
