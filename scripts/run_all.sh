#!/usr/bin/env bash
# Full experiment pipeline. Run from the project root.
#   bash scripts/run_all.sh
set -euo pipefail

echo "==> Preflight"
python scripts/preflight.py

echo "==> Building OKF bundle"
python -m src.build_bundle

echo "==> Main run (both arms)"
python -m src.run_experiment --ablation full

echo "==> Ablations (OKF arm only)"
python -m src.run_experiment --arms okf --ablation no_expansion
python -m src.run_experiment --arms okf --ablation embed_full_body
python -m src.run_experiment --arms okf --ablation two_hop

echo "==> Scoring"
for f in results/raw_*.csv; do
  python -m src.evaluate --input "$(basename "$f")"
done

echo "==> Analysis"
python -m src.analyze --inputs $(cd results && ls scored_*.csv | tr '\n' ' ')

echo
echo "Done. Now open results/human_labelling_sheet.csv and label it by hand,"
echo "then rerun: python -m src.analyze --inputs <scored files> --label-col human_label"
