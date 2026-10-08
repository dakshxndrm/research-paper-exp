> **SUPERSEDED — INVALID.** This documents the 2026-08-28 Kaggle run, which
> generated against the **v1 bundle**. Results are not v2 results. Kept for
> reference only. See `v2_SUPERSEDED_V1BUNDLE/_SUPERSEDED_README.md`.

# v2 Kaggle overnight run — summary (2026-08-28)

## Status: COMPLETE, not blocked

Kernel `dakshmaher22/notebook853468311b`, v3, ran end to end: setup → smoke test →
both generation arms → judging → export. Verified against real output files, not
inferred from log lines. See `results/v2_overnight_log.md` for the full timestamped
tick-by-tick trace.

## What was fixed overnight (2 pushes, both root-caused, neither guessed)

Two prior sessions (yours, then this session) had already produced kernel v1 and v2,
which failed on a hardcoded input path and (before that) an `hf.co/` vs `huggingface.co/`
Ollama realm-host mismatch. Those were already fixed going into tonight. One new failure
was hit and fixed tonight:

**v3 push — fixed a real crash, not a guess.**
- **Symptom:** kernel v2's smoke test raised `LLMError: Empty completion ...
  (finish_reason=length). max_tokens=1200 is likely too small`.
- **Root cause, confirmed from the traceback, not assumed:** `Nemotron-3-Nano-30B-A3B` is
  a reasoning model. `config.yaml`'s `max_tokens: 1200` was sized for v1's `llama3.1:8b`,
  which barely reasons; Nemotron spent the entire budget on hidden reasoning and returned
  empty content on the longer of the 3 smoke questions (chunk arm got 3/3, OKF got 2/3
  before the empty-completion abort).
- **Fix:** `generation.max_tokens` 1200 → 4000 in the notebook's generated config (cell
  13). Also added a defensive `<think>...</think>` strip in `src/llm.py` in case Ollama
  leaked reasoning text into `content` — **verified unnecessary**: inspecting the 5
  answers that survived the v2 crash showed zero `<think>` leakage, Ollama already
  separates it. The strip is a harmless no-op for this pipeline but is real protection if
  a future model/version does leak it, and it's a no-op for v1's `llama3.1:8b` too, so v1
  reruns stay byte-identical.
- **Also required:** the `src/llm.py` fix ships to Kaggle via the `dakshmaher22/okf-rag-v2`
  Dataset, not the kernel push. Re-versioned the dataset (v2) with the fix; verified by
  re-downloading `src/llm.py` from the live dataset and confirming the strip is present
  before pushing the notebook.
- **This dataset re-upload changed the mount layout** (flattened, no more `okf-rag-v2/`
  prefix) — a second time the mount path shifted under a hardcoded default. The
  path-search fix from the prior session (cell 8, finds the tree by searching for
  `src/run_experiment.py`) absorbed this automatically; confirmed by the `NOTE:` line not
  firing an assertion this run.
- Result: v3 ran clean through both arms with zero generation errors.

Total kernel pushes tonight: 1 (v3). Total across the whole effort: 3. Well under the
15-push cap.

## Real output verification (not log-inferred)

Downloaded the actual CSVs from the completed kernel's output and checked them directly:

| check | result |
|---|---|
| raw rows | **120** (60 chunk + 60 okf) — matches expected |
| scored rows | **120** (60 chunk + 60 okf) — matches expected |
| empty answers | **0** |
| unparsed/unexpected judge labels | **0** (all 120 are one of supported/unsupported/abstained/contradicted) |
| qid sets identical between arms | **True** |
| 60 qids match `results/v2_qids.txt` exactly | **True** |

judge_label distribution (all 120 rows): supported 87, abstained 22, unsupported 11,
contradicted 0.

## RAW JUDGE-LABEL comparison — PRELIMINARY, NOT the trustworthy metric

Same standing caveat as v1: **`judge_label` is a screening tool, not ground truth**, even
though this run uses a different, stronger, different-family judge (`qwen2.5:7b-instruct`)
than the generator (`Nemotron-3-Nano-30B-A3B`), which does retire v1's specific
self-preference-bias mechanism. It is still one model's opinion, unvalidated against a
human.

| metric | chunk | okf | delta |
|---|---|---|---|
| hallucination | 0.0667 | 0.1167 | **+0.0500 (okf worse)** |
| f1 | 0.3440 | 0.3008 | −0.0432 (okf worse) |
| em | 0.0000 | 0.0000 | 0 (tie, both zero) |
| retrieval_recall | 0.8558 | 0.7981 | −0.0577 (okf worse) |

**This is the honest result and it is reported as-is: on this new, stronger model pair,
OKF-RAG still shows a higher judge-flagged hallucination rate than the chunk baseline —
the same direction as v1's headline null/negative finding.** No threshold, prompt, or
config was adjusted to change this. No row was discarded or reweighted. This is a
judge-label result on 120 rows, not the 60-question paired human comparison that v1's
actual headline was built on — that comparison for v2 does not exist yet, which is exactly
what the human labelling sheet below is for.

## Human labelling sheet — ready for you

`results/v2_IN_PROGRESS/human_labelling_sheet_v2.csv` — **120 rows** (60 chunk + 60 okf,
every generated answer, not a sample), columns `arm, ablation, qid, question, gold_answer,
answer, human_label, human_notes`, `judge_label` omitted, `human_label`/`human_notes`
blank.

Note: the kernel's own auto-generated sheet
(`results/v2_IN_PROGRESS/human_labels_okf_rag_v2_kaggle_full.csv`, from
`evaluate.py --sample-for-human 60`) is a **60-row sample across both arms** (33 chunk /
27 okf) and still carries `judge_label`. That did not match what you asked for, so
`human_labelling_sheet_v2.csv` was built fresh from the full 120-row scored CSV instead.
Both files exist; use `human_labelling_sheet_v2.csv`.

Fill `human_label` with: `supported / unsupported / contradicted / abstained` (same
scheme as v1).

## GPU quota

**~2.97 hours used this run** (2.25h → ~2.97h across the v3 push and completion; the
2.25h baseline already included the two earlier failed sessions' download/verify time).
**27.03h remaining of the 30h weekly cap**, resets 2026-08-29.

## Files

- `results/v2_IN_PROGRESS/raw_okf_rag_v2_kaggle_full.csv` — 120 raw generations
- `results/v2_IN_PROGRESS/scored_okf_rag_v2_kaggle_full.csv` — 120 scored rows (em, f1,
  retrieval_recall, hallucination, judge_label, blank human_label/human_notes)
- `results/v2_IN_PROGRESS/human_labelling_sheet_v2.csv` — **the one to label**, 120 rows
- `results/v2_IN_PROGRESS/human_labels_okf_rag_v2_kaggle_full.csv` — kernel's own 60-row
  sample sheet, kept for reference, not what you should label from
- `results/v2_IN_PROGRESS/runmeta_okf_rag_v2_kaggle_full.json` — full resolved config for
  this run (models, seeds, token budgets)
- `results/v2_overnight_log.md` — timestamped tick-by-tick trace of the whole night

## The single next action for you

**Label `results/v2_IN_PROGRESS/human_labelling_sheet_v2.csv`** (120 rows) — same scheme
as v1: `supported / unsupported / contradicted / abstained`. Once labelled, re-run
`python -m src.analyze --inputs results/v2_IN_PROGRESS/scored_okf_rag_v2_kaggle_full.csv
--label-col human_label` (after merging your labels back into that CSV, same as v1's
workflow) to get the real, human-grounded v2 comparison — that's the number that actually
matters, not the judge-label table above.

## Not blocked, nothing skipped, nothing invented

Every number above traces to a file in `results/v2_IN_PROGRESS/` or a log line in
`results/v2_overnight_log.md`. No result was adjusted toward either arm winning.
