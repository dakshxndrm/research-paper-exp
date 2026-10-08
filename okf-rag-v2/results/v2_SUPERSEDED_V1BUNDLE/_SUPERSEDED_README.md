# SUPERSEDED — every file in this directory used the WRONG BUNDLE

**Status: INVALID. Reference only. Do not cite, do not label, do not analyze.**

## What went wrong

The v2 Kaggle run (kernel v3, 2026-08-28) generated all 120 rows against
`data/okf_bundle/`, which at the time was **v1's bundle copied verbatim** from
`PUBLICATION_v1/bundle/okf_bundle/` — 371/371 files byte-identical, confirmed by
SHA-256 over the sorted tree. It was extracted by v1's local Ollama
`llama3.1:8b`, not by any v2 process.

So the OKF arm of this run answered from a **v1 substrate**, not a v2 one. The
run is not a v2 result. Superseded by a rerun against a freshly rebuilt
Nemotron bundle.

## What is invalid, and what is not

Invalid — everything downstream of the OKF arm's retrieval:
- `raw_*_V1BUNDLE_INVALID.csv` — the 120 generations (60 okf + 60 chunk)
- `scored_*_V1BUNDLE_INVALID.csv` — Qwen `judge_label` scoring
- `scored_okf_rag_v2_kaggle_full_CLAUDE_V1BUNDLE_INVALID.csv` — the 120-row
  `claude_label` grading pass
- `significance_CLAUDE_V1BUNDLE_INVALID.txt` — chunk 0.1000 vs okf 0.1833,
  p=0.1333. **Do not report this number.**
- `CLAUDE_LABELS_README_V1BUNDLE_INVALID.md`
- `human_labelling_sheet_v2_V1BUNDLE_INVALID.csv` — still blank. Do NOT label
  it; its rows point at dead generations. A fresh sheet comes from the rerun.
- `runmeta_*_V1BUNDLE_INVALID.json`

Strictly speaking the **chunk arm** never touched the bundle and its 60 rows are
mechanically unaffected. They are still shelved here: the paired comparison is
the unit of analysis, and pairing chunk rows from this run against okf rows from
the rerun would mix two generation sessions. Re-run both arms together.

## Still valid, kept for the rerun

Two findings from the `claude_label` pass are properties of the *method*, not of
the bundle, and survive:
- **Judge-vs-judge agreement**: `claude_label` vs Qwen `judge_label` agreed
  0.900 (108/120), Cohen's kappa = 0.518. Two capable different-family judges at
  kappa 0.52 on the same rubric and contexts — this supports the
  judge-variance caveat and is worth restating.
- **`supported` != correct.** The rubric grades grounding only.

The two bundle defects found during that pass (truncated
`/process/how_finalizers_work.md` losing Q029's `202`; cross-link markup leaking
into generated text on Q020) were defects **of the v1 bundle** and must be
re-checked against the new one — they may or may not recur.

## Provenance of the run itself

T4x2 Kaggle. Generator
`huggingface.co/lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-GGUF:Q3_K_L`,
judge `qwen2.5:7b-instruct`. Both fine; the models were never the problem. Only
the retrieval substrate was wrong.
