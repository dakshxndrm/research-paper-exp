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
    # fillna FIRST: a blank CSV cell reads back as pandas NaN, and
    # NaN.astype(str) becomes the literal string "nan", which passes a bare
    # `!= ""` filter -- every unlabeled row would silently count as labeled.
    labelled = df[df[label_col].fillna("").astype(str).str.strip() != ""].copy()
    if labelled.empty:
        raise SystemExit(f"Column '{label_col}' is empty -- nothing to analyse.")
    labelled["hallucination"] = (
        labelled[label_col].astype(str).str.strip().str.lower()
        .isin(["unsupported", "contradicted"]).astype(int)
    )
    return labelled


# run_experiment records link_mode on every row, so it is always present.
# Without it an alias run and a title_only run concatenated together average
# into a single row -- two different configurations reported as one number.
GROUP_KEYS = ["arm", "ablation", "link_mode"]


def series_label(row: pd.Series) -> str:
    name = {"chunk": "Naive chunk RAG", "okf": "OKF-RAG"}.get(row["arm"], row["arm"])
    return f"{name} ({row['link_mode']})"


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
    """Pair chunk against okf, separately per link_mode.

    Pairing is by qid, so two link modes in one frame would give each qid two
    okf rows and silently misalign the paired arrays. Split first.
    """
    return "\n\n".join(
        _significance_one(df[df["link_mode"] == mode], seed, str(mode))
        for mode in sorted(df["link_mode"].unique())
    )


def _significance_one(df: pd.DataFrame, seed: int, link_mode: str) -> str:
    lines: List[str] = []
    header = f"[link_mode={link_mode}] "
    main = df[df["ablation"] == "full"]
    chunk = main[main["arm"] == "chunk"].set_index("qid").sort_index()
    okf = main[main["arm"] == "okf"].set_index("qid").sort_index()
    shared = chunk.index.intersection(okf.index)

    if len(shared) < 5:
        return f"{header}Not enough paired questions for significance testing."

    chunk, okf = chunk.loc[shared], okf.loc[shared]
    if chunk.index.duplicated().any() or okf.index.duplicated().any():
        return (f"{header}Duplicate qids after pairing -- the inputs mix runs "
                f"that share a link_mode and ablation. Cannot pair safely.")
    lines.append(f"{header}Paired on {len(shared)} questions "
                 f"(chunk vs okf, ablation=full).\n")

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


def plot_main(summary: pd.DataFrame, out: Path) -> None:
    main = summary[summary["ablation"] == "full"]
    if main.empty:
        return
    metrics = [m for m in ["hallucination", "f1", "em", "retrieval_recall"]
               if m in main.columns]
    x = np.arange(len(metrics))
    # One bar group per (arm, link_mode); taking row 0 per arm would silently
    # plot whichever link mode happened to sort first.
    series = list(main.itertuples(index=False))
    width = 0.8 / max(len(series), 1)

    fig, ax = plt.subplots(figsize=(7, 4))
    for i, row in enumerate(series):
        row = pd.Series(row._asdict())
        vals = [row[m] for m in metrics]
        offset = (i - (len(series) - 1) / 2) * width
        ax.bar(x + offset, vals, width, label=series_label(row))
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
    cols = ["arm", "link_mode"]
    pivot = main.pivot_table(index="hop_type", columns=cols,
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
    keys = ["arm", "link_mode"]
    fig, ax = plt.subplots(figsize=(6, 4))
    for values, sub in main.groupby(keys):
        values = values if isinstance(values, tuple) else (values,)
        ax.scatter(sub["context_tokens"], 1 - sub["hallucination"],
                   alpha=0.5, label=" / ".join(str(v) for v in values))
    ax.set_xlabel("context tokens supplied")
    ax.set_ylabel("grounded (1) vs hallucinated (0)")
    ax.set_title("Context cost vs grounding")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out, dpi=200)
    plt.close(fig)


def expansion_breakdown(df: pd.DataFrame):
    """Why link expansion contributed what it did, per arm and ablation.

    A row of all `no_links` means the link graph is empty; all `all_redundant`
    means retrieval already covered the neighbourhood. Both show up as
    n_expanded == 0 and require opposite fixes, so report them apart.
    """
    if "expansion_status" not in df.columns:
        return None
    keys = GROUP_KEYS
    tbl = (
        df.groupby(keys + ["expansion_status"])
        .size()
        .reset_index(name="n")
    )
    totals = tbl.groupby(keys)["n"].transform("sum")
    tbl["pct"] = (100 * tbl["n"] / totals).round(1)
    return tbl


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

    # Every artefact is suffixed with the label column it was built from. A
    # judge run and a human run used to write the same table_main.csv, so the
    # file on disk silently reflected whichever ran last -- and the paper's
    # headline number depends on which one that was.
    tag = "human" if args.label_col == "human_label" else "judge"

    main_tbl = summarise(df, GROUP_KEYS)
    main_tbl.to_csv(results_dir / f"table_main_{tag}.csv", index=False)
    (results_dir / f"table_main_{tag}.tex").write_text(
        main_tbl.to_latex(index=False, float_format="%.3f", escape=True,
                          caption=f"Main results ({tag} labels): naive chunk "
                                  f"RAG vs OKF-RAG.",
                          label=f"tab:main-{tag}", position="t"),
        encoding="utf-8",
    )

    if "hop_type" in df.columns:
        hop_tbl = summarise(df, GROUP_KEYS + ["hop_type"])
        hop_tbl.to_csv(results_dir / f"table_hop_{tag}.csv", index=False)

    abl = df[df["arm"] == "okf"]
    abl_keys = ["ablation", "link_mode"]
    if abl.groupby(abl_keys).ngroups > 1:
        summarise(abl, abl_keys).to_csv(
            results_dir / f"table_ablation_{tag}.csv", index=False
        )
    else:
        # Silently leaving a stale all-ablation table on disk is how a
        # judge-label ablation table survived next to human-label headlines.
        print(f"[warn] only one ablation group in --inputs; "
              f"table_ablation_{tag}.csv not written. Pass every scored file "
              f"if you want a current ablation table.")

    exp_tbl = expansion_breakdown(df)
    if exp_tbl is not None:
        exp_tbl.to_csv(results_dir / f"table_expansion_{tag}.csv", index=False)

    sig = significance(df, seed)
    (results_dir / f"significance_{tag}.txt").write_text(sig, encoding="utf-8")

    plot_main(main_tbl, results_dir / f"fig_main_{tag}.png")
    plot_hop(df, results_dir / f"fig_hop_{tag}.png")
    plot_cost(df, results_dir / f"fig_cost_{tag}.png")

    print("\n=== MAIN TABLE ===")
    print(main_tbl.to_string(index=False))
    if exp_tbl is not None:
        print("\n=== EXPANSION STATUS ===")
        print(exp_tbl.to_string(index=False))
    print("\n=== SIGNIFICANCE ===")
    print(sig)
    print(f"\nAll artefacts written to {results_dir} (suffixed _{tag})")


if __name__ == "__main__":
    main()
