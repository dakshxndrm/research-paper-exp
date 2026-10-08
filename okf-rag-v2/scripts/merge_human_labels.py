"""Merge a filled human-labelling sheet back into a scored results CSV.

`evaluate.py --sample-for-human N` writes `human_labels_<stem>.csv` with blank
`human_label` / `human_notes` columns. A human fills `human_label` with one of
{supported, unsupported, contradicted, abstained}. This script copies those
labels into the matching rows of `scored_<stem>.csv` (keyed on arm + ablation
+ qid), so `analyze.py --label-col human_label` has something to read.

Usage (paths are relative to results/, like analyze.py):
    python scripts/merge_human_labels.py \
        --sheet  v2_kaggle/human_labels_okf_rag_v2_kaggle_full.csv \
        --scored v2_kaggle/scored_okf_rag_v2_kaggle_full.csv

Re-runnable: it overwrites `human_label` only for rows the sheet actually
labels, so you can label in passes and re-merge.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # project root, for `src`
from src.config import load_config

VALID = {"supported", "unsupported", "contradicted", "abstained"}
KEYS = ["arm", "ablation", "qid"]


def _clean(s: pd.Series) -> pd.Series:
    # A blank CSV cell reads back as NaN; NaN.astype(str) == "nan". Fill first.
    return s.fillna("").astype(str).str.strip()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sheet", required=True, help="filled human_labels CSV (rel. to results/)")
    ap.add_argument("--scored", required=True, help="scored CSV to update in place (rel. to results/)")
    ap.add_argument("--out", default=None, help="write here instead of overwriting --scored")
    ap.add_argument("--config", default=None)
    args = ap.parse_args()

    results_dir = Path(load_config(args.config)["paths"]["results"])
    sheet_path = results_dir / args.sheet
    scored_path = results_dir / args.scored
    out_path = results_dir / args.out if args.out else scored_path

    sheet = pd.read_csv(sheet_path)
    scored = pd.read_csv(scored_path)
    for col in KEYS:
        if col not in sheet.columns or col not in scored.columns:
            raise SystemExit(f"Both files need column '{col}'. sheet={list(sheet.columns)}")
    if "human_label" not in sheet.columns:
        raise SystemExit("--sheet has no 'human_label' column -- nothing to merge.")

    sheet = sheet.copy()
    sheet["human_label"] = _clean(sheet["human_label"]).str.lower()
    sheet["human_notes"] = _clean(sheet.get("human_notes", pd.Series("", index=sheet.index)))
    labelled = sheet[sheet["human_label"] != ""]
    if labelled.empty:
        raise SystemExit(f"No non-blank human_label in {sheet_path.name}.")

    bad = sorted(set(labelled["human_label"]) - VALID)
    if bad:
        raise SystemExit(f"Unrecognised human_label value(s): {bad}. Allowed: {sorted(VALID)}")

    # Build whole replacement columns rather than per-cell .loc writes: the
    # scored file ships human_label as an all-blank column, which pandas reads
    # as float64 NaN, and setting a string into a float64 cell raises in
    # pandas >= 2.1. Assigning a full list sidesteps the dtype entirely.
    lab_map = {tuple(str(r[k]) for k in KEYS): (r["human_label"], r["human_notes"])
               for _, r in labelled.iterrows()}
    row_keys = [tuple(str(v) for v in t) for t in zip(*(scored[k] for k in KEYS))]
    present = set(row_keys)
    missing = [k for k in lab_map if k not in present]

    new_label = _clean(scored["human_label"]).tolist() if "human_label" in scored.columns else [""] * len(scored)
    new_notes = _clean(scored["human_notes"]).tolist() if "human_notes" in scored.columns else [""] * len(scored)
    applied = 0
    for i, key in enumerate(row_keys):
        hit = lab_map.get(key)
        if hit is None:
            continue
        new_label[i] = hit[0]
        if hit[1]:
            new_notes[i] = hit[1]
        applied += 1
    scored["human_label"] = new_label
    scored["human_notes"] = new_notes

    out_path.write_text(scored.to_csv(index=False), encoding="utf-8")
    still_blank = int((_clean(scored["human_label"]) == "").sum())
    print(f"merged {applied} label(s) into {out_path.name}")
    if missing:
        print(f"[warn] {len(missing)} sheet row(s) had no match in {scored_path.name}: {missing[:10]}")
    print(f"{still_blank} of {len(scored)} scored rows still have no human_label")
    print(f"label counts now: {scored['human_label'].pipe(_clean).replace('', pd.NA).value_counts(dropna=True).to_dict()}")


if __name__ == "__main__":
    main()
