"""Report cross-link precision from the hand-filled link audit.

Link recall is measurable automatically; precision is not. Fill the `verdict`
column of results/link_audit.csv with correct / spurious / borderline, then:

    python scripts/link_precision.py

Precision is reported two ways because `borderline` should not be silently
rounded in either direction:

    strict  -- only `correct` counts as a hit
    lenient -- `correct` + `borderline` count as hits

Report both in the paper, or state which one you chose and why. The result is
merged into results/bundle_stats.json under "link_precision".
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from src.config import load_config

VERDICTS = {"correct", "spurious", "borderline"}


def summarise(df: pd.DataFrame) -> dict:
    n_correct = int((df["verdict"] == "correct").sum())
    n_borderline = int((df["verdict"] == "borderline").sum())
    n_spurious = int((df["verdict"] == "spurious").sum())
    total = len(df)
    return {
        "links_graded": total,
        "correct": n_correct,
        "borderline": n_borderline,
        "spurious": n_spurious,
        "precision_strict": round(n_correct / total, 3) if total else None,
        "precision_lenient": round((n_correct + n_borderline) / total, 3) if total else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input", default="link_audit_alias.csv",
                        help="Audit filename inside results/, e.g. "
                             "link_audit_alias.csv or link_audit_title_only.csv.")
    parser.add_argument("--stats", default="bundle_stats_alias.json",
                        help="Stats file inside results/ to merge precision into.")
    parser.add_argument("--config", default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    results_dir = Path(cfg["paths"]["results"])
    audit_path = results_dir / args.input

    if not audit_path.exists():
        raise SystemExit(f"No {audit_path}. Run `python -m src.build_bundle` first.")

    df = pd.read_csv(audit_path)
    if df.empty:
        raise SystemExit(f"{audit_path} has no links to grade.")

    df["verdict"] = df["verdict"].fillna("").astype(str).str.strip().str.lower()

    ungraded = df[df["verdict"] == ""]
    unknown = df[(df["verdict"] != "") & (~df["verdict"].isin(VERDICTS))]
    if len(unknown):
        raise SystemExit(
            f"{len(unknown)} row(s) have a verdict outside {sorted(VERDICTS)}: "
            f"{sorted(unknown['verdict'].unique())}"
        )
    if len(ungraded):
        # Scoring only the graded subset would silently inflate precision if the
        # unfilled rows are the ones that looked wrong.
        raise SystemExit(
            f"{len(ungraded)} of {len(df)} links are ungraded. Fill every "
            f"`verdict` cell in {audit_path} with correct/spurious/borderline."
        )

    overall = summarise(df)
    by_type = {t: summarise(g) for t, g in df.groupby("match_type")}

    print(f"Link precision over {overall['links_graded']} graded links")
    print("=" * 58)
    print(f"  correct {overall['correct']}  borderline {overall['borderline']}  "
          f"spurious {overall['spurious']}")
    print(f"  precision (strict, correct only)      : {overall['precision_strict']}")
    print(f"  precision (lenient, + borderline)     : {overall['precision_lenient']}")
    print("\nBy match type")
    print("-" * 58)
    for match_type, s in sorted(by_type.items()):
        print(f"  {match_type:<6} n={s['links_graded']:<4} "
              f"strict={s['precision_strict']}  lenient={s['precision_lenient']}  "
              f"(correct {s['correct']}, borderline {s['borderline']}, spurious {s['spurious']})")

    stats_path = results_dir / args.stats
    stats = json.loads(stats_path.read_text(encoding="utf-8")) if stats_path.exists() else {}
    stats["link_precision"] = {**overall, "by_match_type": by_type}
    stats_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")
    print(f"\nMerged into {stats_path}")


if __name__ == "__main__":
    main()
