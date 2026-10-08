"""Stage 4 -- aggregate scored results into paper-ready tables and figures.

Outputs into results/:
  table_main.csv / table_main.tex        headline comparison
  table_hop.csv                          single-hop vs multi-hop breakdown
  table_ablation.csv                     ablation study
  significance.txt                       paired bootstrap + McNemar
  fig_main.png, fig_hop.png, fig_cost.png

Usage:
    python -m src.analyze --inputs scored_okf_rag_v1_full.csv
    python -m src.analyze --inputs scored_..._full.csv scored_..._no_expansion.csv
    python -m src.analyze --inputs ... --label-col human_label
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from src.config import load_config  # noqa: E402

METRICS = ["hallucination", "f1", "em", "retrieval_recall",
           "citation_valid", "abstained", "context_tokens", "n_units"]


def apply_label_col(df: pd.DataFrame, label_col: str) -> pd.DataFrame:
    """Recompute the hallucination flag from whichever label column is chosen."""
    if label_col not in df.columns:
        raise SystemExit(f"Column '{label_col}' not in the scored file.")
    labelled = df[df[label_col].astype(str).str.strip() != ""].copy()
    if labelled.empty:
        raise SystemExit(f"Column '{label_col}' is empty -- nothing to analyse.")
    labelled["hallucination"] = (
        labelled[label_col].astype(str).str.strip().str.lower()
        .isin(["unsupported", "contradicted"]).astype(int)
    )
    return labelled


def summarise(df: pd.DataFrame, by: List[str]) -> pd.DataFrame:
    cols = [m for m in METRICS if m in df.columns]
    out = df.groupby(by)[cols].mean().round(4)
    out["n"] = df.groupby(by).size()
    return out.reset_index()


def paired_bootstrap(a: np.ndarray, b: np.ndarray, n_boot: int = 10000,
                     seed: int = 42) -> float:
    """Two-sided p-value for the paired difference in means (b - a)."""
    rng = np.random.default_rng(seed)
    observed = b.mean() - a.mean()
    diffs = b - a
    centred = diffs - diffs.mean()
    idx = rng.integers(0, len(diffs), size=(n_boot, len(diffs)))
    null = centred[idx].mean(axis=1)
    return float((np.abs(null) >= abs(observed)).mean())


def mcnemar(a: np.ndarray, b: np.ndarray) -> str:
    """Exact McNemar test on paired binary outcomes."""
    from math import comb

    b01 = int(((a == 0) & (b == 1)).sum())
    b10 = int(((a == 1) & (b == 0)).sum())
    n = b01 + b10
    if n == 0:
        return "McNemar: no discordant pairs (p = 1.0)"
    k = min(b01, b10)
    p = min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / (2 ** n))
    return f"McNemar: discordant {b01}/{b10}, exact p = {p:.4g}"


def significance(df: pd.DataFrame, seed: int) -> str:
    lines: List[str] = []
    main = df[df["ablation"] == "full"]
    chunk = main[main["arm"] == "chunk"].set_index("qid").sort_index()
    okf = main[main["arm"] == "okf"].set_index("qid").sort_index()
    shared = chunk.index.intersection(okf.index)

    if len(shared) < 5:
        return "Not enough paired questions for significance testing."

    chunk, okf = chunk.loc[shared], okf.loc[shared]
    lines.append(f"Paired on {len(shared)} questions (chunk vs okf, ablation=full).\n")

    for metric in ["hallucination", "f1", "em", "retrieval_recall"]:
        if metric not in chunk.columns:
            continue
        a = chunk[metric].astype(float).fillna(0).to_numpy()
        b = okf[metric].astype(float).fillna(0).to_numpy()
        p = paired_bootstrap(a, b, seed=seed)
        lines.append(
            f"{metric:18s} chunk={a.mean():.4f}  okf={b.mean():.4f}  "
            f"delta={b.mean() - a.mean():+.4f}  bootstrap p={p:.4g}"
        )
        if set(np.unique(np.concatenate([a, b]))) <= {0.0, 1.0}:
            lines.append(f"{'':18s} {mcnemar(a.astype(int), b.astype(int))}")

    lines.append(
        "\nReport the p-values as-is. With ~100 questions, a non-significant "
        "result is a legitimate finding -- say so rather than hiding it."
    )
    return "\n".join(lines)


def to_latex(df: pd.DataFrame, caption: str, label: str) -> str:
    body = df.to_latex(index=False, float_format="%.3f", escape=True)
    return (
        "\\begin{table}[t]\n\\centering\n"
        f"\\caption{{{caption}}}\n\\label{{tab:{label}}}\n"
        f"{body}\\end{{table}}\n"
    )


def plot_main(summary: pd.DataFrame, out: Path) -> None:
    main = summary[summary["ablation"] == "full"]
    if main.empty:
        return
    metrics = [m for m in ["hallucination", "f1", "em", "retrieval_recall"]
               if m in main.columns]
    x = np.arange(len(metrics))
    width = 0.36

    fig, ax = plt.subplots(figsize=(7, 4))
    for i, arm in enumerate(main["arm"].unique()):
        vals = [main[main["arm"] == arm][m].to_numpy()[0] for m in metrics]
        ax.bar(x + (i - 0.5) * width, vals, width,
               label={"chunk": "Naive chunk RAG", "okf": "OKF-RAG"}.get(arm, arm))
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, rotation=15)
    ax.set_ylabel("score")
    ax.set_title("Main comparison (lower is better for hallucination)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out, dpi=200)
    plt.close(fig)


def plot_hop(df: pd.DataFrame, out: Path) -> None:
    main = df[df["ablation"] == "full"]
    if main.empty or "hop_type" not in main.columns:
        return
    pivot = main.pivot_table(index="hop_type", columns="arm",
                             values="hallucination", aggfunc="mean")
    fig, ax = plt.subplots(figsize=(6, 4))
    pivot.plot(kind="bar", ax=ax)
    ax.set_ylabel("hallucination rate")
    ax.set_title("Hallucination rate by question type")
    ax.tick_params(axis="x", rotation=0)
    fig.tight_layout()
    fig.savefig(out, dpi=200)
    plt.close(fig)


def plot_cost(df: pd.DataFrame, out: Path) -> None:
    main = df[df["ablation"] == "full"]
    if main.empty:
        return
    fig, ax = plt.subplots(figsize=(6, 4))
    for arm in main["arm"].unique():
        sub = main[main["arm"] == arm]
        ax.scatter(sub["context_tokens"], 1 - sub["hallucination"],
                   alpha=0.5, label=arm)
    ax.set_xlabel("context tokens supplied")
    ax.set_ylabel("grounded (1) vs hallucinated (0)")
    ax.set_title("Context cost vs grounding")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out, dpi=200)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate scored results.")
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--label-col", default="judge_label",
                        choices=["judge_label", "human_label"])
    parser.add_argument("--config", default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    results_dir = Path(cfg["paths"]["results"])
    seed = cfg["experiment"]["seed"]

    frames = [pd.read_csv(results_dir / name) for name in args.inputs]
    df = pd.concat(frames, ignore_index=True)

    if args.label_col == "human_label":
        df = apply_label_col(df, "human_label")
        print(f"Using HUMAN labels on {len(df)} rows.")
    else:
        print(f"Using LLM-judge labels on {len(df)} rows. "
              "Headline numbers in the paper should use human labels.")

    main_tbl = summarise(df, ["arm", "ablation"])
    main_tbl.to_csv(results_dir / "table_main.csv", index=False)
    (results_dir / "table_main.tex").write_text(
        to_latex(main_tbl, "Main results: naive chunk RAG vs OKF-RAG.", "main"),
        encoding="utf-8",
    )

    if "hop_type" in df.columns:
        hop_tbl = summarise(df, ["arm", "ablation", "hop_type"])
        hop_tbl.to_csv(results_dir / "table_hop.csv", index=False)

    abl = df[df["arm"] == "okf"]
    if abl["ablation"].nunique() > 1:
        summarise(abl, ["ablation"]).to_csv(
            results_dir / "table_ablation.csv", index=False
        )

    sig = significance(df, seed)
    (results_dir / "significance.txt").write_text(sig, encoding="utf-8")

    plot_main(main_tbl, results_dir / "fig_main.png")
    plot_hop(df, results_dir / "fig_hop.png")
    plot_cost(df, results_dir / "fig_cost.png")

    print("\n=== MAIN TABLE ===")
    print(main_tbl.to_string(index=False))
    print("\n=== SIGNIFICANCE ===")
    print(sig)
    print(f"\nAll artefacts written to {results_dir}")


if __name__ == "__main__":
    main()
