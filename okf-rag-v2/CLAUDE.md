# OKF-RAG — project guide

<!-- READ-ONLY: everything in results/v1_reference/ is frozen v1 evidence copied
     from PUBLICATION_v1/. Read it, compare against it, never edit or overwrite it. -->

**This tree (`okf-rag-v2/`) was rebuilt on 2026-08-27 from `../PUBLICATION_v1/`
after the original project folder was deleted. `../PUBLICATION_v1/` is the
archival source of truth and is treated as read-only.**

v1's frozen outputs live in `results/v1_reference/`. v2 runs write to
`results/v2_kaggle/`. `PROJECT_MAP.md`, `results/DETAILED_AUDIT.md`,
`archive/`, `tests/` and `pyproject.toml` did **not** survive into
PUBLICATION_v1 and no longer exist — ignore references to them below.
Run modules from this directory (`python -m src.x`); there is no package to
`pip install -e .` any more.

## 1. What this project is

OKF-RAG tests whether curating raw documents into an **Open Knowledge Format
(OKF) bundle** — small, self-contained, cross-linked concept units — reduces
hallucination in RAG compared to naive fixed-size chunk retrieval. Both arms
share the same 40-document Kubernetes documentation corpus, the same
generator LLM, the same context token budget, and the same 100 human-authored
questions; only the retrieval substrate differs (Arm A: overlapping text
chunks. Arm B: OKF concept bundle + markdown cross-link expansion). That's
the whole experiment — if OKF-RAG hallucinates less under those controlled
conditions, the difference is attributable to the retrieval substrate, not to
something else being unfair between the arms.

## 2. How the pipeline works

```
corpus (data/raw/)
   -> bundle       src/build_bundle.py        [LLM-assisted extraction, needs no human]
   -> questions    questions/questions.csv     [HUMAN-AUTHORED, cannot be automated]
   -> generation   src/run_experiment.py       [both arms answer all 100 questions]
   -> scoring      src/evaluate.py             [EM/F1/recall/citation + LLM judge]
   -> human labels results/human_labels_*.csv  [HUMAN-AUTHORED, cannot be automated]
   -> analysis     src/analyze.py              [tables, significance test, figures]
```

- **Corpus and questions are the two human-input stages.** Nothing else
  requires a person, except reading model output to fill in `human_label`.
- Bundle build is LLM-assisted (extraction) + fully deterministic
  (cross-linking) — see `src/build_bundle.py`'s module docstring for why
  linking specifically must never be LLM-driven.
- Generation and scoring are checkpointed (`done_keys`/`append_row` in
  `src/config.py`) so a crash or rate-limit mid-run loses nothing already paid
  for — just re-run the same command.

## 3. Current state (as of 2026-08-26)

| Stage | State | Evidence |
|---|---|---|
| Bundle (alias mode, live) | **PASS** | `data/okf_bundle/`: 371 concepts, 1,103 cross-links. |
| Bundle (title_only ablation) | **PASS** | `data/okf_bundle_title_only/`: 371 concepts, 387 cross-links. |
| Questions | **PASS** | 100 rows, 52 single / 33 multi / 15 unanswerable. |
| Generation | **PASS** | All 5 `raw_*.csv` present (200 main, 100 each ablation). |
| Scoring | **PASS** | All 5 `scored_*.csv` present, 1:1 with the raw files. |
| Human labels — both arms | **PASS** | 120 labelled rows in `v1_reference/scored_okf_rag_v1_full.csv` (60 okf + 60 chunk). Source sheets: `v1_reference/human_labels_okf_rag_v1_full_OKF.csv`, `..._CHUNK.csv`. |
| Paired human comparison | **PASS — 60 paired questions** | `v1_reference/significance_human.txt`. |
| Link precision | **PASS** | 100-link seed-42 sample fully graded; merged into `v1_reference/bundle_stats_alias.json`. |
| Analysis tables/figures | **CURRENT** | `*_human.*` and `*_judge.*` regenerated 2026-08-26. |

### The headline result is a null, and it is negative

On the 60 paired human-labelled questions, **OKF-RAG did not beat the chunk
baseline** on any metric:

| metric | chunk | okf | delta | bootstrap p |
|---|---|---|---|---|
| hallucination | 0.0333 | 0.0833 | **+0.0500** (worse) | 0.3056 |
| f1 | 0.3151 | 0.2869 | −0.0282 | 0.3108 |
| em | 0.0000 | 0.0167 | +0.0167 | 0.5248 |
| retrieval_recall | 0.7417 | 0.6917 | −0.0500 | 0.1963 |

Nothing is significant at n=60, so the honest reading is **"no detectable
difference, with the point estimate favouring the baseline"** — not "OKF-RAG
is worse". Write the paper around that. It is a legitimate finding and the
project's own README already commits to reporting it rather than dropping it.

OKF-RAG does win decisively on **context cost**: 1,163 tokens/question vs the
baseline's 1,615, a 28% reduction, while answering the same questions. That is
the defensible claim currently in the data.

Judge labels (all 600 rows) tell the same story: chunk 0.03 vs okf 0.05
hallucination. The judge is an 8B model scoring its own generations, so it is
a screening tool only — but it agrees on direction, which is worth stating.

## 4. How to run things

```bash
# One-time: make src/ importable without sys.path hacks
pip install -e .

# Preflight (corpus, questions, embedder, generator LLM, bundle)
python scripts/preflight.py

# Build the main (alias-mode) bundle, then the title_only ablation bundle
python -m src.build_bundle
python -m src.build_bundle --config config_title_only.yaml

# Run the experiment (main run, both arms)
python -m src.run_experiment

# Ablations (OKF arm only)
python -m src.run_experiment --arms okf --ablation no_expansion
python -m src.run_experiment --arms okf --ablation embed_full_body
python -m src.run_experiment --arms okf --ablation two_hop
python -m src.run_experiment --config config_title_only.yaml --ablation full \
    --arms okf --out raw_okf_rag_v1_title_only.csv

# Score (repeat --input per raw file). Paths are relative to results/.
python -m src.evaluate --input raw_okf_rag_v1_full.csv

# Analyze — judge labels, all 5 files -> *_judge.*
python -m src.analyze --inputs \
    v1_reference/scored_okf_rag_v1_full.csv v1_reference/scored_okf_rag_v1_no_expansion.csv \
    v1_reference/scored_okf_rag_v1_embed_full_body.csv v1_reference/scored_okf_rag_v1_two_hop.csv \
    v1_reference/scored_okf_rag_v1_title_only.csv

# Analyze — HUMAN labels, the headline -> *_human.*
python -m src.analyze --inputs v1_reference/scored_okf_rag_v1_full.csv --label-col human_label

# Link precision (grade a link_audit_*.csv `verdict` column first)
python scripts/link_precision.py --input v1_reference/link_audit_RANDOM100.csv \
    --stats v1_reference/bundle_stats_alias.json

# Bundle reproducibility variance (~120 LLM calls at -n 3 on the full corpus)
python scripts/bundle_variance.py -n 3

# Tests (no model download, no LLM needed)
python tests/test_logic.py && python tests/test_expansion.py
```

## 5. Known limitations that MUST appear in the paper

- **The headline result is null.** See section 3. Report it as such.
- **Link precision in alias mode is poor.** Over the graded 100-link sample:
  strict precision 0.44, lenient 0.79. Split by match type, `title` links are
  0.778 strict / 0.963 lenient but `alias` links are only **0.315 strict** /
  0.726 lenient. Alias matching is what produces most of the link graph
  (1,103 links vs title_only's 387), so most of Arm B's link expansion is
  running on low-precision edges. This is the most likely mechanical
  explanation for the null result and should be stated as such.
- **Concept extraction used multiple models across sessions** due to API
  quota exhaustion: Groq `gpt-oss-120b` and Gemini `2.5-flash` were tried
  first and hit hard quota walls; the corpus was ultimately (re-)extracted
  end-to-end on local Ollama `llama3.1:8b`, which produced the committed
  `data/okf_bundle/`. State plainly which model produced the bundle you
  report numbers from — it's the local one.
- **Generation and judging both ran on the same model** (`llama3.1:8b`, local
  Ollama), so the LLM judge has a self-preference bias. **Human labels are
  the trustworthy metric; `judge_label` is a screening tool only.**
- **`min_concept_words` filtering discarded 108 of 479 extracted concepts
  (23%)**, including at least 3 that were the correct answer to a question
  (Q003 etcd, Q005 kubelet, Q096 kube-apiserver). Some questions are
  therefore harder for the OKF arm than intended, independent of retrieval
  quality — the gold concept never made it into the bundle at all.
- **`retrieval_recall` for the OKF arm uses a document→concept mapping
  layer** (`src/evaluate.py:expand_gold_to_concepts`), expanding each gold
  document to every concept extracted from it (median ~11). This is a
  deliberately **loose, optimistic upper bound** for OKF and is **not
  like-for-like** against the chunk arm's document-granularity recall. Note
  that OKF still loses on this metric despite the handicap being in its
  favour.
- **Human labelling covers 60 of 100 questions per arm**, and 0 rows on any
  ablation arm.
- **Link precision is estimated from 100 of 1,103 links** (seed 42).

## 6. Gotchas — all six now fixed in code

Every output file that used to have a fixed name is now named after what
produced it, so nothing silently clobbers anything:

| Was | Now |
|---|---|
| `human_labelling_sheet.csv` (overwritten every run) | `human_labels_<scored-stem>.csv`, and refuses to overwrite a sheet that already has labels — writes `*_REGENERATED.csv` instead |
| `bundle_stats.json` (last build wins) | `bundle_stats_<link_mode>.json` |
| `link_audit.csv` (last build wins) | `link_audit_<link_mode>.csv`, and **carries existing verdicts forward** so a rebuild cannot destroy hand-grading |
| `runmeta_<ablation>.json` (title_only overwrote main) | `runmeta_<output-stem>.json` |
| `table_*.csv` / `fig_*.png` (judge run vs human run clobbered each other) | suffixed `_judge` / `_human` |
| `table_ablation.csv` silently not regenerated with one ablation group | now prints an explicit `[warn]` instead of leaving a stale file |

Still true, not a code problem:

- **Blank CSV cells read as NaN and stringify to the literal `"nan"`.** A bare
  `df[col] != ""` filter does NOT catch this. `apply_label_col` fills NaN
  first and has a regression test in `tests/test_logic.py`. If you write new
  code filtering on a label column being non-empty, `fillna("")` first.
- **`wc -l` miscounts CSV rows when a field has embedded newlines.** Trust
  `pandas.read_csv` row counts for any file with free-text columns.

## 7. How to improve the results (prioritised)

1. **Attack the alias link precision problem** — this is now the top item,
   because it is the most plausible cause of the null. Alias links are 0.315
   strict precision and dominate the graph. Add a filter at
   `build_bundle.py:count_ambiguous_aliases` (currently a pure diagnostic,
   which is where a filter would slot in) dropping generic single-word and
   ambiguous aliases, rebuild, and re-run. Cost: one rule + one rebuild.
   Buys: the cleanest shot at turning the null into a real effect, and a
   defensible alias-vs-title ablation either way.
2. **Raise human-label coverage from 60 to all 100 questions, and onto the
   ablation arms** (currently 0 human-labelled ablation rows). Cost: a few
   hours of reading model output. Buys: tighter intervals on a result that is
   currently indistinguishable from noise — at n=60 the study is underpowered
   for the effect sizes observed.
3. **Grade more of the link audit.** 100 of 1,103 links are graded. Cost:
   hours. Buys: a precision number with a real confidence interval, which
   item 1 depends on to show improvement.
4. **Lower or remove `min_concept_words` and rebuild**, recovering the 108
   discarded concepts (23%), including 3 that directly answer questions
   (Q003, Q005, Q096). Cost: one rebuild + re-running affected runs. Buys:
   closes a known hole that handicaps Arm B.
5. **Concept-level gold annotations**, replacing the loose document→concept
   recall mapping. Cost: hand-annotating 85 answerable questions. Buys: a
   `retrieval_recall` genuinely comparable between arms.
6. **Use a different, stronger model for judging than for generation.** Cost:
   a second local model or paid API. Buys: removes the self-preference
   caveat on `judge_label`.
7. **Increase the question set beyond 100.** Highest effort on this list.
   Buys: narrower bootstrap intervals — the binding constraint on saying
   anything conclusive.

---

## Session Log

### 2026-08-26 — Project reorganised, v1 frozen
- Audited every file; wrote `PROJECT_MAP.md` (root) and `results/DETAILED_AUDIT.md`.
- Moved v1's 33 output artefacts to `results/v1_reference/`, logs to `results/logs/`,
  superseded files to `archive/`. Nothing deleted. Commands in section 4 repathed.
- `bundle_debug/` and `link_audit_*.csv` deliberately stayed at `results/` root:
  build_bundle rewrites them and carries hand-graded verdicts forward.
- Both test suites pass under `.venv/Scripts/python.exe`.

### 2026-08-26 — v2 setup: security sweep
- Swept the whole tree + all 8 git commits for `nvapi-`. **No key material found
  anywhere.** The only hits are prose mentions in PROJECT_MAP.md:56 and
  DETAILED_AUDIT.md:166 describing the old leak — no key digits in either.
- `archive/testtt.py`, which did hold a plaintext `nvapi-` key, is gone from disk
  (removed outside this session). Both docs still reference it; left as-is
  pending confirmation, since deleting is the user's call.

### 2026-08-26 — v2 config created
- `config_v2.yaml` written, `extends: config.yaml`. Verified by flattened diff:
  **only** `paths.results`, `generation.*` and `judge.*` differ. `retrieval`,
  `embedding`, `bundle_builder`, bundle path, questions path and seed all
  byte-identical to v1 — v2 uses the exact same bundle.
- Generation `minimaxai/minimax-m3` @ max_tokens 3000; judge
  `nvidia/nemotron-3.5-lightning-30b-a3b` @ 2000; both on
  `https://integrate.api.nvidia.com/v1`, key from `NVIDIA_API_KEY`.

### 2026-08-26 — v2 question set pinned to v1's 60
- Extracted the 60 human-labelled qids from `v1_reference/scored_okf_rag_v1_full.csv`;
  okf and chunk label the identical qid set. Written to
  `results/v2_kaggle/v2_qids.txt` (39 single / 13 multi / 8 unanswerable).
- Added `--qids-file` to `run_experiment.py` (`--limit` is head(n) and cannot
  express this subset); it hard-fails if any listed qid is absent from
  questions.csv. Verified: filters to exactly 60. Both test suites still pass.
- Added `LLMClient.last_usage` (prompt/completion tokens + finish_reason) so the
  smoke test can report real budget consumption instead of guessing.

### 2026-08-26 — BLOCKED before smoke test
- `NVIDIA_API_KEY` is **not in `.env`**. `.env` holds only `LLM_API_KEY`
  (a Groq `gsk_…` key, plus one commented-out) and `GEMINI_API_KEY`.
- Also: nothing in this repo ever reads `.env` — no `python-dotenv`, no loader.
  v1 worked because the key was `export`ed into the shell (README section 0).
- Steps 3–5 (smoke test, full run, labelling sheet) cannot start until the key is
  available in the environment. Waiting on the user.

### 2026-08-26 — v2 unblocked, then BLOCKED again on a minimax-m3 quota wall
- Key supplied in `.env`. Nothing read `.env`, so added `_load_dotenv()` to
  `src/config.py` (~10 lines, stdlib, `setdefault` so a real export still wins).
  Verified `NVIDIA_API_KEY` now reaches the process. Both test suites still pass.
- Fixed a 404: NVIDIA's base_url already ends in `/v1` and llm.py's default
  chat_path adds another. Set `chat_path: "/chat/completions"` in config_v2.yaml
  (the same one-key mechanism Gemini needed). Endpoint then worked.
- Smoke test (3 qids, both arms): **chunk arm completed all 3**, answers are
  on-topic, correctly cited and well-formed. **OKF arm got 0 rows** — every call
  429s.
- **`minimaxai/minimax-m3` is quota-exhausted on this account.** Evidence: the
  429 body is bare (`{"status":429,"title":"Too Many Requests"}`), carries no
  `retry-after` and no rate headers; it did NOT clear after 60s, 120s or 180s of
  total quiet. It is **per-model, not account-wide** — a same-moment probe of
  `nvidia/nemotron-3.5-lightning-30b-a3b` returned 200. Roughly 4 successful
  minimax-m3 completions were served before the wall.
- Not substituting a model, per standing instruction. Waiting on the user.

### 2026-08-27 — Kaggle T4x2 notebook for v2 created (awaiting a run)
- Wrote `notebooks/okf_rag_v2_kaggle.ipynb`. It **drives the existing CLI** rather than
  reimplementing anything: `run_experiment.py` for both arms, `evaluate.py` for judging,
  so `done_keys`/`append_row` checkpointing, the retry/backoff logic and the JUDGE_SYSTEM
  rubric are all v1's, unchanged. Judge labels stay methodologically comparable to v1.
- Runtime: **Ollama**, not vLLM. Kaggle's T4 is Turing (no bf16/FP8) and vLLM's quantised
  MoE kernels are unreliable there; Ollama installs with one curl and already serves
  `/v1/chat/completions`, which is exactly what `src/llm.py` speaks — zero pipeline
  changes, and no external API means none of the Groq/Gemini/NVIDIA quota walls apply.
- Models, both chosen off the Vectara hallucination leaderboard for a low measured rate
  and **different families**, which retires v1's self-preference-bias caveat:
  generation `nvidia/Nemotron-3-Nano-30B-A3B` (9.6%), judge `zai-org/GLM-4.6` (9.5%).
- **BLOCKER, flagged not worked around: GLM-4.6 is ~355B and cannot run on T4x2 (32 GB).**
  At 4-bit its weights are ~200 GB. No quantisation fits. Per the standing instruction I
  did not substitute a model — `JUDGE_MODEL` is a variable in the settings cell, the
  notebook fails loudly on an OOM load, and the warning cell lists runnable
  different-family alternatives (`qwen3:30b-a3b`, `gemma3:27b`, `glm4:9b`). Whichever is
  used must be reported as the v2 judge, **not** as GLM-4.6. The generator is fine: ~17 GB
  at Q4.
- Scope: the same **60 qids** as v1 (derived in-notebook from `human_label` on the okf
  rows of `v1_reference/scored_okf_rag_v1_full.csv`; verified locally to match
  `v2_kaggle/v2_qids.txt` exactly), both arms = 120 generations + 120 judge calls.
  Writes to `results/v2_kaggle/`, nowhere near `v1_reference/`.
- Config is **generated by the notebook** (`config_v2_kaggle.yaml`, `extends: config.yaml`)
  so it can never disagree with the models that session actually pulled. Nothing checked
  in was modified.
- Has a 3-qid smoke-test section that prints all 6 answers and judge labels, per this
  project's standing smoke-test-first discipline; every work cell is re-runnable and
  resumes. Also sets `OLLAMA_CONTEXT_LENGTH=8192` (the OpenAI endpoint cannot pass
  `num_ctx`, and the default would truncate the 1800-token retrieval context) and
  `OLLAMA_MAX_LOADED_MODELS=1` (holding generator + judge resident OOMs a T4).
- **Awaiting the user running it on Kaggle.** Needs Internet ON and either a `REPO_URL` or
  a Kaggle Dataset containing `data/raw/` (not optional — the chunk arm reads it),
  `data/okf_bundle/`, `questions/questions.csv`, `results/v1_reference/scored_okf_rag_v1_full.csv`,
  `src/`, `config.yaml`, `pyproject.toml`.

### 2026-08-27 — Original folder deleted; project rebuilt from PUBLICATION_v1
- The working `okf-rag/` folder is gone. This tree (`okf-rag-v2/`) was rebuilt
  from `../PUBLICATION_v1/`, which was **not** modified — copied from, never
  moved or edited. Verified afterwards by a recursive byte-level compare.
- Copied in: `config.yaml`, `config_title_only.yaml`, `questions/questions.csv`,
  `data/raw/` (40 docs), `data/corpus_selection.json`, `src/` (9 modules),
  `scripts/`, `CLAUDE.md`, and the frozen v1 evidence into
  `results/v1_reference/` (scored full CSV, table_main_HUMAN, significance_HUMAN,
  both link audits, both human labelling sheets, both bundle stats JSONs,
  concept_paths.txt).
- **The bundle did not need rebuilding.** It *was* preserved in PUBLICATION_v1,
  at `bundle/okf_bundle/` — 371 concept files. Copied verbatim to
  `data/okf_bundle/`; SHA-256 over the sorted tree is identical to the source,
  and a deterministic re-count of markdown cross-links gives **371 concepts /
  1,103 links**, exactly matching `okf_bundle_stats.json`. All 371 paths listed
  in v1's `concept_paths.txt` resolve on disk.
  Re-extracting with an LLM was therefore *not* done: it would have introduced
  extraction variance and broken like-for-like comparability with v1, for no
  gain. v2 runs on the identical bundle v1 ran on.
- Not carried over (only stats survived, bundle itself absent):
  `data/okf_bundle_title_only/`. The title_only ablation cannot be re-run
  without rebuilding that bundle. Out of v2's scope, flagged here.
- The 60 v2 qids re-extracted to `results/v2_qids.txt`: 39 single / 13 multi /
  8 unanswerable. Verified identical across all four sources — okf rows and
  chunk rows of `scored_okf_rag_v1_full.csv`, plus both
  `human_labelling_sheet_*_FINAL.csv`. All 60 present in `questions.csv`.
- `notebooks/okf_rag_v2_kaggle.ipynb` rebuilt: seeded from the surviving
  notebook, repathed `v1_FINAL/` → `v1_reference/`, dropped the
  `pip install -e .` / `pyproject.toml` dependency (runs from cwd instead), the
  qid cell now reads the shipped `results/v2_qids.txt` and cross-asserts it
  against v1, and a new **first cell** is a full pre-flight setup checklist
  (accelerator, internet, dataset creation and attachment, quota + time budget,
  smoke-test-first). Every code cell compiles.
- **The GLM-4.6 blocker is unchanged and unresolved**: it is ~355B and cannot
  fit T4x2 at any quantisation. Not substituted; `JUDGE_MODEL` is a variable,
  the load cell fails loudly, and runnable different-family alternatives are
  listed in the notebook.
- Awaiting the manual Kaggle run. It expects a **Kaggle Dataset upload** —
  there is no GitHub remote for this project.

### 2026-08-28 — v2 Kaggle run COMPLETE (kernel v3), overnight, unattended
- Two live-debugging passes fixed real crashes as they happened, each
  root-caused from the actual traceback, not guessed:
  1. `hf.co/...` realm-host mismatch in `ollama pull` → switched to
     `huggingface.co/...` (kernel v2).
  2. Hardcoded `KAGGLE_INPUT` mount path wrong → cell 8 now searches
     `/kaggle/input` for `src/run_experiment.py` instead of trusting one
     guessed path (kernel v2; this also absorbed a second, later mount-layout
     change from re-uploading the dataset, with zero further edits needed).
  3. `LLMError: Empty completion ... max_tokens too small` — Nemotron-3-Nano
     is a reasoning model; v1's `max_tokens: 1200` (sized for `llama3.1:8b`,
     which barely reasons) let it burn the whole budget on hidden reasoning.
     Fixed: `max_tokens` 1200 → 4000 (kernel v3). Also added a defensive
     `<think>` strip to `src/llm.py`, confirmed unnecessary by inspecting
     surviving smoke answers (Ollama already separates reasoning from
     content) but kept as real protection, no-op for v1.
  4. `src/llm.py` ships via the `dakshmaher22/okf-rag-v2` Kaggle Dataset, not
     the kernel — re-versioned the dataset and verified the fix was live by
     re-downloading it before pushing the notebook.
- Kernel v3 ran clean end to end: T4x2, generator
  `huggingface.co/lmstudio-community/NVIDIA-Nemotron-3-Nano-30B-A3B-GGUF:Q3_K_L`
  (19.3 GiB, measured 20.4/30 GiB loaded across both cards), judge
  `qwen2.5:7b-instruct` (~4.7 GB, Ollama library, different family from the
  generator — **retires v1's self-preference-bias caveat**, report this as
  the v2 judge, not GLM-4.6, which remains impossible on this hardware and
  was never used). **`Q3_K_M` does not exist** in that HF repo — quants are
  `Q3_K_L`/`Q4_K_M`/`Q6_K`/`Q8_0`/`F16`; used `Q3_K_L`.
- Output verified from the real downloaded CSVs, not inferred: 120 raw rows
  (60+60), 120 scored rows, 0 empty answers, 0 unparsed judge labels, both
  arms answer the identical 60-qid set matching `results/v2_qids.txt`.
- **Judge-label result (preliminary, screening only): OKF hallucination 0.1167
  vs chunk 0.0667 — OKF still worse, same direction as v1's null/negative
  finding**, on a stronger, different-family, non-self-judging model pair.
  Not adjusted toward either arm; every row counted as generated.
- Total GPU quota for this run: ~0.72h (2.25h→2.97h). 27.03h/30h remaining
  this week.
- Full trace: `results/v2_overnight_log.md`. Full report + next action:
  `results/v2_overnight_summary.md`. Results: `results/v2_IN_PROGRESS/`,
  including `human_labelling_sheet_v2.csv` (120 rows, blank, ready to label —
  built by hand because the kernel's own `--sample-for-human 60` sheet was
  a 60-row sample across both arms with `judge_label` still attached, not
  what was needed).
- **Next action: label `human_labelling_sheet_v2.csv`**, then
  `analyze.py --label-col human_label` for the real v2 headline number.

### 2026-08-28 — v2 graded by a third independent judge (`claude_label`), NOT human labels
- User asked me to label the sheet. **Declined to write into `human_label`** — that
  column's whole function is to be a non-LLM check on `judge_label`, and filling it
  with model output would falsify the paper's "human labels are the trustworthy
  metric" claim. Instead graded all 120 rows into a new **`claude_label`** column,
  named for what it is. `human_labelling_sheet_v2.csv` is still blank and still needs
  a human.
- Method: `JUDGE_SYSTEM` from `evaluate.py` verbatim (grounding only, not
  correctness), judged against contexts rebuilt with `evaluate.rebuild_contexts()`
  and **verified** to contain every `retrieved_ids` entry (120/120, 0 mismatches).
  All 120 rows read in full; per-row rationale in `claude_note`.
- **Result, same direction as v1 and as Qwen: OKF hallucinates more.**
  chunk 0.1000 vs okf 0.1833, delta **+0.0833**, bootstrap p=0.1333, McNemar 8/3
  p=0.2266. Answerable-only (n=52): 0.1154 vs 0.2115, p=0.1585. **Not significant at
  n=60** — the honest reading remains "no detectable difference, point estimate
  favours the baseline".
- **Judge-vs-judge is the new number**: `claude_label` vs Qwen `judge_label` agree
  0.900 exactly (108/120), **Cohen's κ=0.518**, perfect agreement on all 22
  abstentions. I am stricter (17 flagged vs 11). Two capable different-family judges
  landing at κ=0.52 on the same rubric and same contexts means single-judge
  hallucination rates carry real judge-dependent variance — this *supports* the
  standing caveat rather than removing it.
- **Calibration favours OKF**: both arms abstained correctly on all 8 unanswerable.
  OKF abstained on 5 extra answerable (Q016/Q017/Q028/Q029/Q066) vs chunk's 1 — i.e.
  it says "INSUFFICIENT CONTEXT" on retrieval misses instead of confabulating. On
  **Q066 chunk hallucinated where OKF abstained.** Hallucination rate alone hides this.
- **Two bundle defects found, independent of retrieval quality**:
  1. `/process/how_finalizers_work.md` is **truncated mid-list** (`does the
     following: ...`), losing the `202` answer to Q029 at extraction time. Not a
     retrieval failure — a bundle defect, and a second instance of the
     extraction-quality problem beyond `min_concept_words`.
  2. OKF cross-link markup leaks into generated text (Q020 answer contains
     `metadata.[ownerReferences]`).
- **`supported` != correct.** The rubric grades grounding only. Q048(okf) and
  Q039(chunk) are grounded-but-wrong. `1 - hallucination` is not accuracy; a
  correctness pass would need the human sheet.
- **Correction to an earlier claim in this session**: I said mid-run that OKF was
  ~2.5x faster per question, reading tqdm rates during warmup. The actual per-row
  numbers say the opposite: `generate_s` chunk 8.93s vs okf 10.56s. OKF is *slower*
  here despite the smaller context. The 28.0% context-token reduction (1615.4 ->
  1162.6) is real but is **not independent evidence** — retrieval config and bundle
  are byte-identical to v1, so those tokens are deterministically the same numbers.
- Files: `results/v2_IN_PROGRESS/scored_okf_rag_v2_kaggle_full_CLAUDE.csv`,
  `significance_CLAUDE.txt`, `CLAUDE_LABELS_README.md`.
- **Next action unchanged: label `human_labelling_sheet_v2.csv`.**

### 2026-08-28 — Bundle cleared, previous v2 run invalidated, 7 questions excluded
- **Audit finding that triggered all of this:** `data/okf_bundle/` was **v1's
  bundle, byte for byte** — 371/371 files identical to
  `PUBLICATION_v1/bundle/okf_bundle/`, same tree SHA-256
  (`99a2242e…70b956`). It was produced by v1's `llama3.1:8b`, not by anything
  v2. `data/raw/` (40 docs), `questions/questions.csv` and
  `corpus_selection.json` are also byte-identical to v1 — **that reuse is
  correct and stays.** No `bundle_debug/` or stale checkpoints exist anywhere.
- **Decision (user): Option B — clear it, rebuild fresh with Nemotron.** The
  earlier "don't rebuild, preserve like-for-like comparability with v1"
  rationale in the 2026-08-27 entry is **superseded**.
- Bundle **moved, not deleted** (archive-only instruction) to
  `data/_ARCHIVED_okf_bundle_V1COPY_DO_NOT_USE/` + `_WHY_ARCHIVED.md`.
  `data/okf_bundle/` no longer exists — `config.yaml:14` still points there, so
  the rebuild writes into a clean path. The archive is fully redundant with
  `PUBLICATION_v1/`; safe to delete outright.
- **The completed 2026-08-28 Kaggle run is INVALID** — it generated against the
  v1 bundle. `results/v2_IN_PROGRESS/` → **`results/v2_SUPERSEDED_V1BUNDLE/`**,
  every artefact suffixed `_V1BUNDLE_INVALID`, with `_SUPERSEDED_README.md`
  explaining why. **Do not report chunk 0.1000 vs okf 0.1833 / p=0.1333.**
  Text files carry a banner; CSVs do not (it would break `read_csv`) — the
  filename suffix and the README carry it instead.
  - The chunk arm never touched the bundle and is mechanically unaffected, but
    is shelved too: pairing its rows against okf rows from a different
    generation session would confound the paired comparison. Re-run both arms.
  - **Survives the invalidation** (properties of the method, not the bundle):
    judge-vs-judge agreement 0.900, Cohen's κ=0.518 between `claude_label` and
    Qwen `judge_label`; and `supported` != correct.
  - The two bundle defects found in that pass (truncated
    `/process/how_finalizers_work.md` losing Q029's `202`; cross-link markup
    leaking into Q020's answer) were **v1-bundle** defects — re-check against
    the new bundle rather than assuming they carry over.
  - `human_labelling_sheet_v2_V1BUNDLE_INVALID.csv` is still blank and must
    **not** be labelled; its rows point at dead generations.
- **`questions/questions.csv` is NOT edited** (human-authored). Selection is now
  driven by three files in `results/`, described in `v2_qids.txt.README`:
  `v2_qids.txt` (the historical 60), `v2_excluded_qids.txt` (7 drops + reason
  each), `v2_active_qids.txt` (**56**, provisional).
- **7 questions excluded from v2's active set.** Content defects: **Q016**
  (asks for the config *file*, gold gives the *directory*), **Q049** (gold
  answer's "non-unique names" premise is in `names.md`, not the cited
  `owners-dependents.md`), **Q058**/**Q066** (gold says kube-scheduler
  "enforces" RuntimeClass constraints; the doc says they merge *in admission* —
  and the second gold doc contributes nothing), **Q076** (second gold doc
  `runtime-class.md` never mentions loopback — not a real multi-hop), **Q079**
  (two-part question, gold answers one part). Duplicate: **Q048** dropped,
  **Q018** kept (identical UID question, both were in the 60).
- Only **4 of the 7** were in the labelled 60 (Q016/Q048/Q066/Q079), so
  **60 → 56**. hop_type **37 single / 11 multi / 8 unanswerable**. All 17 gold
  documents still covered; no document lost.
- **Multi-hop is now 19.6%**, against 21.7% in the 60 and 33.0% in the full
  100 — the arm OKF-RAG is supposed to win on is the most under-sampled.
  Flagged in the paper's limitations regardless of the backfill decision.
- **Also for the paper, unchanged by any of this:** only **17 of 40** raw docs
  are ever a gold document. The other 23 are distractor-only — they are
  embedded and compete for retrieval but can never be a hit. Legitimate design,
  but state it; do not let a reader assume 40-doc coverage.
- `results/v1_reference/okf_bundle_stats.json` was **left in place**, not
  archived: it describes v1's bundle, which still exists in `PUBLICATION_v1/`,
  so it is current v1 evidence, not stale — and `scripts/link_precision.py`
  reads it by path. `_BUNDLE_STATS_SCOPE_NOTE.md` added there to say so.
- `PUBLICATION_v1/` untouched, re-verified after all moves.
- **Next action: decide backfill vs n=56, then rebuild the bundle with
  Nemotron.** Nothing was rebuilt in this session.

### 2026-08-28 — Backfill applied: v2 active set is 63 questions
- User chose **option 2**: add 7 multi-hop, ignore the round count. `results/v2_active_qids.txt`
  is now **63** and FINAL. `questions/questions.csv` still unedited (sha256 verified).
- Distribution **37 single / 18 multi / 8 unanswerable = 58.7% / 28.6% / 12.7%**, against the
  full set's 52/33/15. Multi-hop went 19.6% -> 28.6%; the gap to 33% is what remains.
- Added: `results/v2_backfill_qids.txt` (7 qids + per-qid rationale).
- **Only 4 of the 7 are genuinely two-document** — Q057, Q064, Q072, Q100. Verified: neither
  cited doc alone contains both halves.
- **Q051, Q069, Q075 are single-doc answerable** despite being labelled `multi` and citing two
  docs. Verified degenerate at `architecture.md:21`, `kube-scheduler.md:41`(binding) /
  "isn't (yet) schedulable", and `architecture__cloud-controller.md:57,92`. Taken anyway for
  content coverage (kube-proxy-optional path, the scheduling FAILURE path, cloud-controller
  content) — **but they must not be cited as evidence that link expansion helped.**
- **This is now a known property of the question set, not just of the backfill:** of the 18
  multi rows in the active 63, a substantial minority are answerable from one document. The
  earlier audit already found 5 such rows among the original 60 (Q065, Q067, Q071, Q073,
  Q074). **State in the paper that `hop_type == multi` is an authoring label, not a verified
  two-document requirement.** A real fix is re-deriving hop_type by checking whether either
  cited doc alone contains the answer — deferred, not done.
- Correction to a claim made earlier in this session: I first shortlisted Q051/Q061/Q075 as
  the *clean* multi-hop candidates. That was wrong — all three are degenerate. Q061 was
  dropped from the backfill as a result; Q051 and Q075 were kept knowingly, on content
  grounds, and are labelled as such above.
- Doc coverage unchanged at **17 of 40**; the other 23 remain distractor-only.
- **Next action: rebuild the bundle with Nemotron.** Nothing rebuilt yet — see the readiness
  notes in that session entry when it happens.

### 2026-08-28 — Model string corrected: Nemotron-3-Nano → Nemotron-3.5-Lightning
- **The generator/bundle-builder model string was wrong.** The notebook pointed at
  `NVIDIA-Nemotron-3-Nano-30B-A3B-GGUF` — a different model. The one actually tested and
  confirmed working on this project (via the NVIDIA API, 2026-08-26 entries) is
  **Nemotron-3.5-Lightning**. Corrected to
  `huggingface.co/lmstudio-community/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF:Q4_K_M`.
- **Quant: `Q4_K_M` (24.5 GB).** Verified against the HF API: this repo has exactly three
  GGUFs — `Q4_K_M` (24.5 GB), `Q6_K` (33.5 GB), `Q8_0` (33.6 GB). No `Q4_0`, no `BF16`
  (the quant list quoted in the request was for a different repo). `Q4_K_M` is the only
  one that fits T4x2 (~29 GiB), and the fit is tight — KV-cache headroom is thin, an OOM
  at load is possible. `GEN_QUANT` changed `Q3_K_L` → `Q4_K_M`.
- **First push (kernel v7, 2026-08-28 18:03 UTC) failed in ~2 min** at the `ollama pull`
  cell: `pull model manifest: 400 ... The specified tag is not available` — because `Q4_0`
  does not exist in the repo. Fixed by switching to `Q4_K_M` (kernel v8).
- **`reasoning_effort: "none"` kept** — it addressed a real hidden-reasoning runaway and
  applies to any reasoning-tuned Nemotron variant.
- **Architecture caveat:** Lightning is hybrid Mamba-2 + MoE (`nemotron_h_moe`), not a plain
  transformer. The notebook's VRAM cell (section 3b) must load it cleanly before a long run
  is trusted — do not assume it behaves like the earlier tested transformer.
- Edited: `notebooks/okf_rag_v2_kaggle.ipynb` (both the repo-root copy and
  `okf-rag-v2/notebooks/…` — kept byte-identical). Settings cell, config-generation cell,
  and the VRAM/quant markdown cells all updated; **0 remaining `Nemotron-3-Nano` references
  in the notebook.** `config.yaml` was never involved (it still names `llama3.1:8b`; the v2
  config is notebook-generated at runtime).
- **Deliberately NOT edited:** dated session-log entries above (2026-08-27, 2026-08-28) that
  record what earlier now-invalidated runs actually used, and everything under
  `results/v2_SUPERSEDED_V1BUNDLE/` + `results/v2_overnight_summary_V1BUNDLE_INVALID.md` +
  `PUBLICATION_v1/`. Those are historical records of real events; rewriting them would
  falsify the log. They still contain the `Nemotron-3-Nano` string, correctly, as history.
- **Local `ollama rm` not applicable** — Ollama is not installed on this machine; the wrong
  model was only ever pulled into ephemeral Kaggle session disk and is already gone.
- **Next action unchanged: push the corrected notebook to Kaggle and re-run the bundle
  rebuild + verification gate.** Do not proceed past the gate into generation.

### 2026-09-01 — Pre-run blocker fixes + LAUNCHED bundle rebuild (kernel v9)
- **Audit of the Kaggle notebook before spending a GPU session found 2 hard blockers:**
  1. **`reasoning_effort` was not plumbed through.** `src/build_bundle.py:make_client()`
     built the `LLMClient` dict with an explicit key whitelist that **omitted
     `reasoning_effort`**, so `bundle_builder.reasoning_effort: "none"` in the generated
     config was inert. Nemotron-3.5-Lightning is a reasoning model — without it, extraction
     burns the whole token budget on hidden reasoning and returns empty completions,
     crashing on document 1 (exactly the 2026-08-28 failure). **Fixed:** added
     `"reasoning_effort": bcfg.get("reasoning_effort")` to `make_client()`. Consumer side
     (`llm.py:60` reads it, `:126` injects into payload) was already correct. Also added the
     same key to `evaluate.py:make_judge()` for parity — no-op today (qwen2.5:7b-instruct
     isn't a reasoning model). Full path traced + unit-verified locally (no Ollama needed):
     config → make_client → `LLMClient.reasoning_effort` → payload.
  2. **`OLLAMA_CONTEXT_LENGTH=8192` too small for extraction.** Bundle build feeds whole
     docs (largest 11 KB ≈ 4.2k input tokens) + `bundle_builder.max_tokens: 16000` output
     ≈ 20.2k worst case. **Fixed:** cell 10 → `24576`, with an inline note that cell 11
     (VRAM check) is the real test of whether Q4_K_M + 24k ctx fits T4x2, and the fallback
     (drop `max_tokens` 16000→~10000, ctx→~14000, accept truncation-salvage on the 2-3
     largest docs) if it OOMs. VRAM math: hybrid Mamba-2 + MoE means only the periodic
     attention layers hold a context-scaling KV cache, so 24k KV is ~1-4 GiB (uncertain —
     exact attention-layer count unknown), against ~4.7-6.4 GiB headroom above the 22.8 GiB
     model. Not provable statically; cell 11 is the gate.
- **2 should-fix (notebook consistency):** cell 0 setup checklist told the user to include
  `data/okf_bundle/` in the dataset, but cell 8 hard-fails if that folder exists (v1
  contamination guard) and cell 0 omitted the 4 qid files cell 8/21 need — rewrote cell 0's
  file list (no bundle, +4 qid files, explicit "do NOT include okf_bundle"). Added
  `results/v2_qids.txt` to cell 8's `REQUIRED` (cell 21 reads it for the 63-qid
  reconstruction assert; a missing file now gives cell 8's clean error). Cosmetic: stale
  `60/120/240` counts → `63/126/252`, `~19 GiB` → `~24.5 GB` across cells 0/1/2/9/34.
- **Backup of pre-fix notebook:** `scratchpad/okf_rag_v2_kaggle.ipynb.bak`.
- **Kaggle wiring (MCP server was down; used the `kaggle` CLI with the user's token):**
  - v2 kernel is `dakshmaher22/notebook853468311b` (GPU T4, internet on,
    `dataset_sources: [dakshmaher22/okf-rag-v2]`) — the earlier "v8" push lived here.
  - **Dataset `dakshmaher22/okf-rag-v2` re-uploaded** as a new version (2026-09-01 14:09
    UTC) with the corrected `src/`. Verified after upload: `src/build_bundle.py` carries the
    `reasoning_effort` line, **0 `okf_bundle` files**, 40 raw docs, all 4 qid files +
    `scored_okf_rag_v1_full.csv` present.
  - **Kernel v9 pushed 2026-09-01 ~19:41 IST. Ran ~28 min, ended `KernelWorkerStatus.ERROR`.**

#### Outcome: bundle BUILT successfully; verification gate has a false-negative bug
- **The `reasoning_effort` fix worked.** All 40 docs extracted — every
  `results/v2_kaggle/bundle_debug/<doc>.concepts.json` + `.raw.txt` present, zero failures,
  NO empty-completion crash on document 1. `src/build_bundle.main()` ran to completion:
  wrote 358 concept files, `bundle_stats_alias.json`, `link_audit_alias.csv`.
- **New v2 bundle stats** (`results/v2_kaggle/bundle_stats_alias.json`, Nemotron-3.5-Lightning
  Q4_K_M, `reasoning_effort:none`):
  - **358 concepts / 1031 cross-links** (806 alias + 225 title), avg 2.88 links/concept,
    82 ambiguous aliases, avg body 72.8 words, 78 type dirs.
  - vs **v1: 371 / 1103.** Genuinely different extractor output; tree SHA `c72da2de…` ≠
    v1's `99a2242e…`.
  - Quality spot-check good: `architecture.md` → 12 clean concepts incl. etcd / kubelet /
    kube-apiserver as their own concepts (v1's `min_concept_words` had dropped those).
- **The ERROR is `cell 17` (the verification gate), assert 2b: `assert "llama3.1" not in bb`.**
  `bb` is the raw `bundle_builder:` slice of the generated `config_v2_kaggle.yaml` —
  **including comments.** Cell 13 writes two explanatory comments into that block that
  contain the literal string `llama3.1:8b` (`"...NOT v1's llama3.1:8b."` and `"16000 is
  v1's value, confirmed good for llama3.1:8b..."`). The naive substring check trips on its
  own comment. Reproduced locally against the pulled config + bundle: asserts [1] hash≠v1
  and [2a] Nemotron `model:` line present both PASS; [2b] is the only failure; [3] freshness
  would pass on-box. Gate raised `AssertionError`, so `bundle_provenance.json` was never
  written and generation never started (cell 19's `SystemExit` was never even reached).
  **This is a bug in the gate I reviewed and wrongly cleared in the pre-run audit** — the
  fix is to make 2b precise (check only non-comment `model:` lines), e.g.
  `assert not any(l.strip().startswith("model:") and "llama3.1" in l for l in bb.splitlines())`.
- **Could NOT verify cell 6 (1 GPU vs T4x2) or cell 11 VRAM numbers** — Kaggle's CLI log
  export returned 0 bytes and the rendered notebook isn't in `kaggle kernels output`. But
  the model pulled and ran 40 extraction calls over ~28 min, which is inconsistent with a
  single-T4 OOM at load — T4x2 + the 24576 context almost certainly worked; the printed
  numbers just aren't recoverable from this run.
- **Built bundle pulled locally** to `scratchpad`/`kv9_out/okf-rag/` (358 concepts +
  stats + link audit + 40 debug checkpoints) — usable to skip re-extraction if desired.
- **Cell 17 assert 2b fixed (user: option 1 — full rebuild).** Was
  `assert "llama3.1" not in bb` over the raw comment-laden config slice. Now strips YAML
  comments and checks only the ACTIVE `model:` directive(s):
  `bb_model_lines = [l.split("#",1)[0].strip() for l in bb.splitlines() if ...startswith("model:")]`,
  then `assert bb_model_lines == ['model: "<Nemotron>"']` + `assert not any("llama3.1" in l ...)`.
  Verified against the exact `config_v2_kaggle.yaml` the errored run generated: all of
  [1]/[2a]/[2b]/[3] now pass. Notebook backup: `scratchpad/okf_rag_v2_kaggle.ipynb.bak2`.
- **Kernel v10 pushed 2026-09-01 ~20:19 IST. ~29 min in queue, ran ~25+ min, ended
  `KernelWorkerStatus.ERROR` at 21:59 IST.**

#### Outcome: VERIFICATION GATE PASSED. The "ERROR" is cell 19's intentional `SystemExit`.
- `results/v2_kaggle/bundle_provenance.json` **was written** — cell 17 ran all 3 asserts and
  its final writes/prints. No `raw_*`/`scored_*` CSVs exist → generation never started →
  the ERROR is the designed hard-stop (`raise SystemExit` in cell 19; Kaggle flags any
  SystemExit as ERROR). The cell 17 assert-2b fix worked.
- **`bundle_provenance.json`** (built_at_utc `2026-09-01T16:28:55Z`):
  - `bundle_builder_model`: `huggingface.co/lmstudio-community/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF:Q4_K_M`
  - `gen_quant`: `Q4_K_M`
  - `tree_sha256`: `489c7db1d86463664d24213f35351fc1187c8326619db9db684420d0a13df541`
    (independently recomputed from the pulled bundle — matches)
  - `v1_tree_sha256`: `99a2242e…`, `differs_from_v1`: **true**
  - `n_concept_files`: 358, `n_source_docs`: 40, `concepts`: 358, `cross_links`: 1031,
    `link_mode`: alias
- **Gate asserts, all PASS:** [1] tree hash `489c7db1…` ≠ v1 `99a2242e…`; [2] bundle_builder
  `model:` line is Nemotron, no active `llama3.1` line (the fix); [3] all 358 concept files
  freshly written this session.
- **Bundle stats** (`bundle_stats_alias.json`): 358 concepts / 1031 cross-links
  (806 alias + 225 title), avg 2.88 links/concept, 82 ambiguous aliases, avg body
  72.8 words. vs **v1: 371 / 1103.**
- **v10 vs v9 hash differs** (`489c7db1…` vs v9's `c72da2de…`) but concept/link **counts are
  identical** (358 / 1031). Expected: MoE routing + per-run `timestamp:` frontmatter make
  the bytes non-reproducible even at temp 0 (llm.py notes seed is best-effort on MoE); the
  extraction is structurally stable. Do NOT claim bit-reproducible builds.
- **Cell 6 / cell 11 printed VRAM numbers still not recoverable** (Kaggle CLI log export = 0
  bytes both runs; rendered notebook not in `kaggle kernels output`). But the model pulled,
  extracted all 40 docs, cross-linked, over ~25+ min with no OOM — T4x2 + `OLLAMA_CONTEXT_LENGTH=24576`
  worked. If the exact numbers are needed, open the kernel on kaggle.com and read cells 6/11.
- **Built bundle pulled locally:** `scratchpad/kv10_out/okf-rag/` — `data/okf_bundle/`
  (358 files), `results/v2_kaggle/{bundle_provenance.json, bundle_stats_alias.json,
  link_audit_alias.csv, bundle_debug/ (40 docs)}`.
- **Gate is passed; the v2 bundle is validated and reproduced twice.** Next stages
  (re-validate questions vs new bundle → generation + judging) are NOT started.

### 2026-09-02 — New multi-hop questions audited; 7 of 10 added to questions.csv
- User supplied `questions/new_genuine_multihop_Q126_Q135.csv` (10 rows, columns match
  questions.csv). Audited each with the cover-one-up test (read both cited docs, is the
  gold answer genuinely impossible from either single doc alone). **All 20 cited filenames
  exist in `data/raw/`.**
- **GENUINE two-doc (7, ADDED): Q126, Q127, Q128, Q129, Q132, Q133, Q134.**
  - Q126 dual-stack(`.spec.clusterIP`=first ipFamily) + endpoint-slices(≥2 slices by IP type)
  - Q127 gateway(Service-IP vs backing-EndpointSlices) + endpoint-slices(auto-managed, Pod refs)
  - Q128 dual-stack(`RequireDualStack` create-fails) + endpoint-slices(≥2 slices)
  - Q129 windows-networking(CNI→HNS) + services-networking(proxy watches Service+EndpointSlice)
  - Q132 (**weak**) workload-api(policy copied) + workload-api-TAS(constraint copied + label placement) — only workload-api's "policy is copied" clause keeps this off single-doc
  - Q133 disruption-and-priority(PodGroup priority authoritative) + workload-aware-preemption(tie-break: PodGroup > Pod at equal priority)
  - Q134 ttlafterfinished(TTL→cascade delete of dependents) + lifecycle(PodGroup finalizer blocks deletion until Pods terminal)
- **DEGENERATE (3, NOT added):**
  - **Q130** — single-doc from `workloads__workload-api__policies.md` (near-duplicate of existing Q106/Q114).
  - **Q131** — single-doc from `workloads__podgroup-api__lifecycle.md` (its Limitations section has both the `PodGroupScheduled`-is-initial-only fact and the deletion-protection finalizer).
  - **Q135** — single-doc from `scheduling-eviction__workload-aware-preemption.md` (its text already states both the victim hierarchy and "considers … disruption mode … to evaluate if and how its pods can be preempted").
- Also flagged (added anyway, content overlap not a validity defect): Q128 Part 2 reuses the
  "EndpointSlices split by IP family" hop shared with Q126 and existing Q101; Q129 overlaps
  existing Q104; Q134 overlaps existing Q109 (inverted to the finalizer angle).
- **`questions/questions.csv` edited for the first time — user-directed.** 115 → **122 rows**
  (Q001–Q115 + Q126–Q129, Q132–Q134). CRLF preserved, no dup qids, every cited doc present,
  all 7 `hop_type: multi` / 2-doc. Backup: `scratchpad/questions.csv.bak`. Note: qid gap
  Q116–Q125 and Q130/Q131/Q135 are intentionally unused. The earlier "questions.csv is NOT
  edited" rule is now superseded for deliberate additions of audited new questions; the
  qid-list files in `results/` still govern which questions a run uses.
### 2026-09-02 — v2 active qid list rebuilt around verified-genuine multi-hop
- `results/v2_active_qids.txt` (63, frozen 2026-08-28) was built BEFORE the genuine
  multi-hop questions existed and still carried ~12 degenerate "multi" rows. Rebuilt as
  **`results/v2_active_qids_v2.txt` — 65 qids, FINAL** (old file kept, not overwritten;
  nothing reads the new one yet). `+ .README` documents composition/validation.
- **Verified-genuine multi-hop pool = 18** (cover-one-up: gold answer impossible from
  either single cited doc): original `Q056 Q057 Q064 Q070 Q072 Q100`; round-1
  `Q102 Q104 Q109 Q111 Q115`; round-2 `Q126 Q127 Q128 Q129 Q132 Q133 Q134`. All 18
  confirmed present in questions.csv, `hop_type=multi`, 2 cited docs. Q132 weakest.
- **37 degenerate `hop_type=multi` qids excluded** (multi in csv but not verified-genuine):
  Q051-Q055, Q058-Q063, Q065-Q069, Q071, Q073-Q080, Q098, Q099, Q101, Q103, Q105-Q108,
  Q110, Q112-Q114. Plus the 7 flawed (Q016 Q048 Q049 Q058 Q066 Q076 Q079).
- **New set: 37 single / 18 multi / 10 unanswerable = 65** (56.9 / 27.7 / 15.4 %). Multi is
  27.7%, not the ~35% corpus target — 18 is the hard ceiling of verified-genuine multi-hop
  that exist; raising the % means cutting single-hop rows. Singles = the exact 37 from the
  old active set; unanswerable = old 8 + Q083 Q085; multi = the 18 genuine.
- **Validation vs the new 358-concept Nemotron bundle (local pull):** all 65 in
  questions.csv; no dups; no flawed qid; every gold_concepts doc for the 55 answerable qids
  resolves to >=1 concept (2-12/doc; thinnest `workloads__workload-api__disruption-and-priority.md`
  -> 2, cited by Q111/Q133). The 10 unanswerable have empty gold_concepts by design.
- **Human-label burden for v2 = 130 rows** (65 qids x 2 arms), ALL fresh. v1 human labels
  do NOT carry over: different bundle (358 vs 371 concepts) + different generator
  (Nemotron-3.5-Lightning vs llama3.1:8b) => every answer differs, no reuse for any row.
### 2026-09-02 — 3-qid SMOKE TEST launched (kernel v11)
- **Purpose:** run 3 qids x 2 arms (6 gen + 6 judge) on the new bundle + new models, then
  hard-stop for review. Smoke qids: **Q001 (single) / Q109 (genuine multi) / Q081
  (unanswerable)**.
- **Bundle reuse, not rebuild:** the v10 `bundle_debug/` checkpoints (40 `.concepts.json`
  + 40 `.raw.txt`) are now shipped in the dataset at `results/v2_kaggle/bundle_debug/`, so
  cell 15's `build_bundle` skips all 40 extraction calls — only deterministic cross-linking
  + `write_bundle` run (~1-2 min), then the verification gate. Saves ~15-20 min of the run.
- **Notebook v11 changes** (backup `scratchpad/okf_rag_v2_kaggle.ipynb.bak3`):
  - Cell 4: new flags `ALLOW_SMOKE` / `ALLOW_FULL_RUN` (both default off in the committed
    file; **this push sets `ALLOW_SMOKE=True`, `ALLOW_FULL_RUN=False`**),
    `ACTIVE_QIDS_FILE="results/v2_active_qids_v2.txt"`, `SMOKE_QIDS=["Q001","Q109","Q081"]`.
  - Cell 19: unconditional `raise SystemExit` -> `if not ALLOW_SMOKE: raise SystemExit(...)`.
  - **New cell 24: `if not ALLOW_FULL_RUN: raise SystemExit(...)`** — hard-stops after the
    smoke test, before the 65-qid cells. Both stops are reversible flags, not deletions.
  - Cell 21 rewritten for the 65-qid list (`v2_active_qids_v2.txt`): asserts len 65, hop
    mix {37,18,10}, no flawed qid, and that every active `multi` row is in the verified
    18-genuine pool.
  - Cell 23 per-row print now shows `finish_reason` / `prompt_tokens` / `completion_tokens`
    / `n_expanded`.
- **`src/run_experiment.py`** now persists `finish_reason` + `prompt_tokens` +
  `completion_tokens` from `LLMClient.last_usage` onto every raw row (additive columns;
  `evaluate.py` carries them through via `**row.to_dict()`). Shipped in dataset v3.
- Dataset `dakshmaher22/okf-rag-v2` re-uploaded (2026-09-02 12:32 UTC) with the checkpoints,
  `v2_active_qids_v2.txt` (+README), 122-row `questions.csv`, and the updated `src/`.
- **Kernel v11: ran ~14 min (18:03->18:17 IST), ended `KernelWorkerStatus.ERROR` = cell 24's
  intentional `raise SystemExit` after the smoke test. SMOKE TEST PASSED.** All artifacts
  present: `bundle_provenance.json`, `raw_/scored_okf_rag_v2_kaggle_smoke.csv`, `runmeta`,
  `v2_qids_smoke.txt`. (Checkpoint reuse worked -> model pull was Kaggle-layer-cached this
  session, so the whole run was fast.)

#### Smoke-test results (Q001 single / Q109 genuine-multi / Q081 unanswerable, both arms)
| arm | qid | finish | prompt_tok | completion_tok | judge | n_expanded |
|---|---|---|---|---|---|---|
| chunk | Q001 | stop | 1268 | 624  | supported | 0 (n/a) |
| chunk | Q081 | stop | 1725 | 712  | abstained | 0 (n/a) |
| chunk | Q109 | stop | 1549 | 1041 | supported | 0 (n/a) |
| okf   | Q001 | stop | 1425 | 566  | supported | 4 (expanded) |
| okf   | Q081 | stop | 1525 | 974  | abstained | 4 (expanded) |
| okf   | Q109 | stop | 1361 | 1510 | supported | 4 (expanded) |

- **1. Truncation:** none. All 6 `finish=stop`. Max completion 1510 tok << `generation.max_tokens:
  4000` (~2.6x headroom). `generation` does NOT set `reasoning_effort:none` (only bundle_builder
  does) and generation is still fine -- the runaway was extraction-specific. 4000 confirmed enough.
- **2. Answers:** all 6 real, on-topic, coherent, `SOURCES:` line present. Both unanswerable
  rows -> "INSUFFICIENT CONTEXT" (correct). Both Q109 (multi) answers correctly synthesise
  ownerReferences + TTL cascade from both cited docs. No empty answers, no `<think>` leak, no
  cross-link-markup leak (a v1-bundle defect -- clean here).
- **3. Judge (qwen2.5:7b-instruct):** 6/6 parseable, 0 malformed. 4 supported / 2 abstained.
- **4. OKF link expansion: WORKING.** every okf row `n_expanded=4` (= `max_expanded` cap),
  `expansion_status=expanded`. Chunk `n_expanded=0` / `not_applicable` (correct). retrieval_recall
  1.0 on all 4 answerable rows, both arms.
- **5. GPU quota:** not CLI-exposed (Kaggle CLI 2.2.4). Wall ~14 min; only 106.8s of actual
  gen inference across 6 calls. Rough cost ~0.2-0.25 GPU-hr. Check the kernel page for the
  remaining weekly balance.
- **Bundle provenance (v11):** 358 concepts / 1031 links (identical structure to v10 --
  checkpoint reuse is faithful), tree_sha256 `ca0b13eb...` (!= v1 `99a2242e...`, != v10
  `489c7db1...`; only per-run `timestamp:` frontmatter differs). Gate [1]/[2]/[3] all passed.
- **`src/run_experiment.py` finish_reason/token persistence works** -- columns present and
  populated in the smoke CSVs; `evaluate.py` carried them through.
### 2026-09-02 — FULL 65-qid v2 run launched (kernel v12)
- Smoke test approved by user. Notebook: `ALLOW_FULL_RUN=True` (+ `ALLOW_SMOKE=True`),
  `ACTIVE_QIDS_FILE=results/v2_active_qids_v2.txt` (65). Cell 31 `--sample-for-human`
  126->130; cell 35 expects 130 / 65 qids. Backup `scratchpad/okf_rag_v2_kaggle.ipynb.bak4`.
- **Run scope:** smoke re-runs first (Q001/Q109/Q081, 6 gen + 6 judge -> `*_smoke.csv`,
  separate files), then the full run: 65 qids x 2 arms = **130 generation + 130 judge**
  -> `raw_okf_rag_v2_kaggle_full.csv` / `scored_okf_rag_v2_kaggle_full.csv`. Bundle reused
  from shipped checkpoints (no re-extraction). Dataset unchanged (v3, 2026-09-02 12:32 UTC).
- Checkpointed via `done_keys(["arm","qid"])` + `append_row` -> a crash/timeout keeps
  finished rows; recovery would be: pull the partial `raw_*_full.csv`, ship it in the
  dataset, re-push so `done_keys` resumes. 12h session cap is well clear (~55-75 min est).
- **Kernel v12 pushed 2026-09-02 ~18:5x IST.** Auto-poll watcher running.
### 2026-09-02 — v12 died mid-run (Ollama OOM); v13 pushed retry-hardened
- **Kernel v12: `ERROR` at 19:04 IST, ~21 min in.** Not an intentional halt (ALLOW_FULL_RUN=True).
  Gate passed, smoke re-ran clean (6/6 `stop`). Full run got **28 chunk rows** (Q001..Q037,
  all `finish=stop`, 0 empty) then died on ~the 29th generation call. No traceback (`.log` 0
  bytes as always). `scored_*_full.csv` / `runmeta_*_full.json` absent -> died in cell 27
  (chunk generation), ~34 sustained Ollama calls in (6 smoke + 28).
- **Diagnosis:** Ollama server crash, almost certainly a **VRAM OOM / fragmentation** on the
  tight Q4_K_M-on-T4x2 fit under sustained load. `OLLAMA_CONTEXT_LENGTH=24576` (sized for the
  now-skipped extraction stage) reserves a large KV window per request -> less headroom.
  A single `LLMError` after retries makes `sh()` raise -> whole kernel ERROR.
- **v13 fixes (backup `scratchpad/okf_rag_v2_kaggle.ipynb.bak5`):**
  1. Cell 10: `OLLAMA_CONTEXT_LENGTH` **24576 -> 8192** (gen <6k, judge <5.4k; extraction is
     checkpoint-only now so it never needed the big window).
  2. Cell 10: new `ollama_restart()` + `sh_resumable(cmd, tries=4)` -- on a batch failure it
     kills+relaunches `ollama serve` and re-runs the command; `done_keys` makes the re-run
     RESUME (skip finished (arm,qid) rows), so an Ollama crash self-heals instead of ending
     the session.
  3. Cells 27/29/31 call `sh_resumable(...)` instead of `sh(...)`.
  4. Cell 13: generation & judge `timeout_s` **1800 -> 600** (max observed gen_s = 128s; bounds
     a hung call to 600x5 instead of 1800x5).
- **Decision: v13 regenerates all 130 from scratch** -- did NOT ship v12's 28-row partial.
  A clean single-session generation is worth ~9 min; the partial-resume path is kept for
  crash recovery (if v13 also dies, ship its partial for a v14 resume).
- Dataset unchanged (v3, 2026-09-02 12:32 UTC). **Kernel v13 pushed ~19:1x IST.** Heartbeat
  cron `9565487d` (10 min) + watcher `bi2z2fh06`.
### 2026-09-02 — v13 died at the SAME row as v12 (chunk/Q039); v14 = per-row skip+log
- **Kernel v13: `ERROR` at 20:01 IST, ~48 min in. Died at exactly 28 chunk rows
  (Q001..Q037), identical to v12** -- despite `OLLAMA_CONTEXT_LENGTH=8192` and
  `sh_resumable(tries=4)`. `sh_resumable` engaged (ollama restarted x4) and chunk/Q039
  failed identically each time -> **deterministic, input-related, NOT Ollama state/OOM.**
- **Local repro (CPU, no Ollama):** `ChunkRAG(cfg).retrieve()` runs fine for ALL 65 active
  qids including Q039 (3 chunks, 1722 ctx tok -- unremarkable). So the failure is in
  `client.generate(...)` -- the Ollama chat call for chunk/Q039 specifically. Can't repro
  the generate step locally (no GPU). Q039 context = `cluster-administration__networking.md#chunk1`
  + `services-networking__dual-stack.md#chunk0,1` (has IPv6/CIDR examples with literal
  `<IPv4 CIDR>` angle brackets, YAML blocks -- a plausible chat-template/tokenizer trigger,
  unconfirmed).
- **v14 fix -- `src/run_experiment.py`: per-row `try/except`.** A failing `(arm, qid)` is
  logged (qid + full traceback) and SKIPPED; the run continues. `main()` writes
  `skipped_<stem>.json` and prints a summary; a re-run retries only the skipped rows
  (`done_keys`). One bad question can no longer kill a 130-row run. Combined with the
  v13 `sh_resumable` (Ollama-crash recovery), the run is now robust to both failure modes.
- Dataset re-uploaded v4 (2026-09-02 14:40 UTC, updated `run_experiment.py`). Notebook
  unchanged from v13. **Kernel v14 pushed ~20:1x IST.** Heartbeat cron `f6a27b79` + watcher
  `bbbcvpzg2`.
### 2026-09-02 — v14 COMPLETE (124/130); root cause found; v15 re-run with generation.reasoning_effort=none
- **Kernel v14: `KernelWorkerStatus.COMPLETE`** (first clean completion), ~85 min. Outputs
  + `okf_rag_v2_kaggle_results.zip` saved under `/kaggle/working/`.
- **124/130 rows** (62 chunk + 62 okf). scored 124/124, judge labels 91 supported /
  32 abstained / 1 unsupported, **0 unparsed**. All 124 completed rows `finish_reason=stop`,
  0 empty, completion_tokens peak 3132 (p95 2745).
- **6 rows SKIPPED, same root cause** (per-row try/except caught + logged them; the
  `skipped_*.json` was overwritten by the 2nd arm -- fixed, see below -- but the errors are
  identical): **chunk Q039/Q104/Q132, okf Q050/Q056/Q115.** Every one:
  `LLMError: Empty completion ... finish_reason=length. max_tokens=4000 is likely too
  small -- a reasoning model consumed the whole budget before emitting an answer.`
  => Nemotron-3.5-Lightning went into a hidden-`<think>` spiral on those 6 questions and
  emitted zero answer content. Deterministic (failed all 5 retries). NOT the OOM/Q039-
  specific theory -- it is the same runaway-reasoning class as bundle extraction.
- **Fixes:**
  1. Generated config (cell 13): **`generation.reasoning_effort: "none"`** (plumbs straight
     through -- `run_experiment` passes the whole `generation` dict to `LLMClient`, which
     reads the key; no src change needed) + **`max_tokens` 4000 -> 6000** as headroom
     insurance. Rationale: grounded 1-3 sentence QA needs no reasoning trace, and v1's
     llama3.1:8b barely reasoned, so this makes v2 gen MORE comparable to v1, not less.
  2. `src/run_experiment.py`: `skipped_<stem>.json` -> `skipped_<stem>_<arm>.json` + merges
     any existing file, so the chunk and okf invocations no longer clobber each other's
     skip log.
- **Decision: re-run ALL 130 fresh with reasoning_effort=none** (did NOT backfill the 6 into
  v14's 124 -- mixed reasoning-on/off in one dataset would be a confound). v14's 124 rows
  are discarded.
- Dataset re-uploaded v5. Notebook backup `scratchpad/okf_rag_v2_kaggle.ipynb.bak6`.
- **Kernel v15 pushed ~21:52 IST** (dataset v5). Heartbeat cron `84c1813f` + watcher
  `bxm4ctxit`. Expect 130/130, 0 skips.

### 2026-09-02 — pipeline prep while v15 runs
- **`analyze.py` confirmed v2-ready:** the new raw columns (`finish_reason`,
  `prompt_tokens`, `completion_tokens`) are ignored by `summarise()` (it filters to
  `METRICS`); `GROUP_KEYS`/pairing all work with one link_mode ("alias") + one ablation
  ("full"). v2 analysis commands (paths relative to `results/`):
  - screening: `python -m src.analyze --inputs v2_kaggle/scored_okf_rag_v2_kaggle_full.csv`
  - headline: `... --label-col human_label` (after labels merged in)
  - run with a config whose `paths.results` = `results/v2_kaggle` so tables land there.
- **NEW `scripts/merge_human_labels.py`** -- fills a completed `human_labels_<stem>.csv`
  sheet back into `scored_<stem>.csv`'s `human_label`/`human_notes` columns, keyed on
  (arm, ablation, qid). This was a missing pipeline step -- v1's labels were written into
  the scored CSV directly with no script. Handles the all-blank-column -> float64 ->
  "can't set string" pandas gotcha (assigns whole replacement columns). Human label
  overrides the judge label and can carry a note. Re-runnable (label in passes). Tested
  locally against v14's sheet. Usage:
  `python scripts/merge_human_labels.py --sheet v2_kaggle/human_labels_okf_rag_v2_kaggle_full.csv --scored v2_kaggle/scored_okf_rag_v2_kaggle_full.csv`
- **v2 post-generation workflow:** v15 -> `scored_okf_rag_v2_kaggle_full.csv` (130) +
  `human_labels_okf_rag_v2_kaggle_full.csv` (130 blank) -> **user labels all 130** ->
  `merge_human_labels.py` -> `analyze.py --label-col human_label` -> compare vs v1's
  `v1_reference/table_main_HUMAN.csv` / `significance_HUMAN.txt`.
- **Next: v15 result — report `_full` counts (130/130), finish_reason, judge parseability,
  `/kaggle/working` zip. Then hand the human-labelling sheet to the user.**

### 2026-09-02 — v15 COMPLETE but DATA UNUSABLE; reasoning_effort:none was the wrong fix; v16
- **Kernel v15: `COMPLETE`, ~25 min, 130/130 rows, 0 skips, 0 unparsed judge labels,
  `/kaggle/working/okf_rag_v2_kaggle_results.zip` present.** Mechanically perfect. **But the
  ANSWERS are broken** -- `generation.reasoning_effort: "none"` collapsed Nemotron into a
  keyword extractor that ignores the (v1, shared) SYSTEM_PROMPT format:
  | check | v14 (reasoning ON, 124 rows) | v15 (reasoning OFF, 130 rows) |
  |---|---|---|
  | answers with `SOURCES:` line | 101/124 | **20/130** |
  | exact "INSUFFICIENT CONTEXT" | 32 | **0** |
  | `abstained` flag total | 32 | **0** |
  | completion_tokens mean / max | 1221 / 3132 | 48 / 401 (min 3) |
  - v15 answers are 1-3 WORDS ("generateName", "kubectl", "202"), no SOURCES line, and on
    unanswerable Qs it paraphrases ("context does not specify...") or **hallucinates from
    outside knowledge** (Q084 -> "Raft", Q091 -> "GCP"). `abstained` detection (literal-
    string match) is dead, EM/F1 tanked, citation metric dead. NOT usable for the paper.
- **Root understanding:** v14 with reasoning ON produced *correctly formatted* answers;
  only **6/130** rows spiraled on an unbounded `<think>` and hit `finish_reason=length` at
  max_tokens 4000. The right fix is headroom + tolerate-a-few-skips, NOT killing reasoning.
- **v16 fix (notebook cell 13 generated config):** REMOVED `generation.reasoning_effort`
  (back to default = reasoning ON), `max_tokens` **6000 -> 8000**. `bundle_builder`
  keeps `reasoning_effort:none` (unchanged; extraction is checkpoint-reused anyway).
  `sh_resumable` + `run_experiment` per-row skip both stay -- a genuine runaway still hits
  the cap, errors, gets logged to `skipped_<stem>_<arm>.json`, and the run continues.
- Expect v16: ~85 min, ~124-130 good rows, possibly a few (<=6) skipped-and-logged runaways
  to document as a limitation. Dataset unchanged (v5). Notebook backup `.bak7`.
- **Kernel v16 pushed ~22:2x IST.** Heartbeat + watcher restarted.

### 2026-09-02 — v16 COMPLETE. This is the usable v2 generation dataset.
- **Kernel v16: `COMPLETE`, ~68 min. 130/130 rows (65 chunk + 65 okf), 0 skips, 0 empty,
  `finish_reason` 130/130 `stop`.** `okf_rag_v2_kaggle_results.zip` saved to `/kaggle/working`.
- **Answer quality restored** (reasoning ON, `max_tokens: 8000`):
  | check | v14 | v15 (bad) | **v16** |
  |---|---|---|---|
  | rows | 124 | 130 | **130** |
  | `SOURCES:` line | 101/124 | 20/130 | **104/130** |
  | `abstained` flag | 32 | 0 | **35** |
  | judge unparsed | 0 | 0 | **0** |
  | completion_tokens max | 3132 | 401 | **7135** (finished; `stop`) |
  - The 7135-token row proves `max_tokens: 8000` was the right call -- it would have been
    a skip at 4000/6000. No runaways this time (0 `skipped_*.json`).
- **Judge-SCREENING result** (NOT the headline -- needs human labels):
  hallucination **chunk 0.0154 / okf 0.0154** (2 flags in 130 rows -- dead even, very low).
  By hop: okf multi 0.056 vs chunk multi 0.0; single/unanswerable 0 both.
  abstained chunk 0.277 / okf 0.262; f1 0.231 / 0.242; em 0 / 0;
  retrieval_recall 0.864 / 0.909 (okf's loose doc->concept map favours it, per v1 caveat);
  citation_valid 1.0 / 1.0.
- **Copied into the local tree:** `results/v2_kaggle/{raw,scored,human_labels}_okf_rag_v2_kaggle_full.csv`,
  `bundle_provenance.json`, `bundle_stats_alias.json`, `link_audit_alias.csv`, `runmeta_*`,
  smoke CSVs, `okf_rag_v2_kaggle_results.zip`; `config_v2_kaggle.yaml`; `data/okf_bundle/`
  (358 concepts, from the reused checkpoints).
- **Bundle provenance:** Nemotron-3.5-Lightning Q4_K_M, 358 concepts / 1031 links,
  `tree_sha256` (v16 build) differs from v1; gate passed.
- **NEXT = HUMAN LABELLING (step 8).** `results/v2_kaggle/human_labels_okf_rag_v2_kaggle_full.csv`
  = 130 rows, `human_label` blank. User fills each with supported / unsupported /
  contradicted / abstained. Then:
  `python scripts/merge_human_labels.py --sheet v2_kaggle/human_labels_okf_rag_v2_kaggle_full.csv --scored v2_kaggle/scored_okf_rag_v2_kaggle_full.csv`
  then `python -m src.analyze --inputs v2_kaggle/scored_okf_rag_v2_kaggle_full.csv --label-col human_label`
  (with a config whose `paths.results` = `results/v2_kaggle`), then compare vs
  `results/v1_reference/table_main_HUMAN.csv` / `significance_HUMAN.txt`.
- Cron/watcher for the run: stopped.

### 2026-09-03 — v2 HUMAN-LABELLED RESULT + v1-vs-v2 comparison (the headline)
- User hand-labelled all 130 rows (via `human_labels_v2_LABELLING.csv`, `label_after` col +
  `new_note`). Built `human_labels_v2_MERGED_INPUT.csv` (arm/ablation/qid/human_label/
  human_notes), ran `scripts/merge_human_labels.py` (added `sys.path` bootstrap so it runs
  standalone). Merge verified: 130/130 non-blank, chunk 45 sup / 18 abst / 2 unsup, okf
  47 sup / 17 abst / 1 contra; only `human_label`+`human_notes` changed (the `answer`
  column shows a diff only because pandas re-wrote `\n`->`\r\n`, 0 rows semantically
  changed). `results/v1_reference/` md5s unchanged -- untouched. Analysis written to
  `results/v2_kaggle/*_human.*` only.
- **v2 human, n=65 paired:**
  | metric | chunk | okf | delta | bootstrap p | McNemar |
  |---|---|---|---|---|---|
  | hallucination | 0.0308 (2/65) | 0.0154 (1/65) | -0.0154 (okf better) | 0.6042 | discordant 1/2, exact p=1 |
  | f1 | 0.2312 | 0.2418 | +0.0106 | 0.6241 | -- |
  | em | 0.0 | 0.0 | 0 | 1 | 0/0 |
  | retrieval_recall (answerable) | 0.864 | 0.909 | +0.045 | 0.1951 | -- |
  | abstained | 0.277 | 0.262 | -- | -- | -- |
  | context_tokens | 1644.5 | 1472.8 | **-10.4%** | -- | -- |
  Hallucination events: chunk {Q036 unsup, Q064 unsup}; okf {Q070 contra}. Discordant
  pairs: Q036 & Q064 chunk-worse, Q070 okf-worse -> net okf better by ONE event.
- **v1 human, n=60 paired (frozen, `v1_reference/`):** hallucination chunk 0.0333 /
  okf 0.0833, delta +0.0500 (okf WORSE), p=0.3056, McNemar discordant 5/2 exact p=0.4531.
  f1 0.3151 / 0.2869. context_tokens 1615 / 1163 (-28%).
- **v1 vs v2 -- hallucination:**
  - **Direction FLIPPED** (v1 okf worse +0.050; v2 okf better -0.015).
  - **Neither significant** -- p=0.31 (v1), p=0.60 (v2); no McNemar near significance.
  - **Raw discordant counts** (what actually matters at this n): v1 = 5 okf-worse / 2
    chunk-worse; v2 = 1 okf-worse / 2 chunk-worse. Total hallucination events per arm:
    v1 chunk 2 okf 5; v2 chunk 2 okf 1. The estimate is riding on <=5 events either way.
- **COMBINED FINDING (abstract):** OKF curation produced no measurable reduction in
  hallucination under controlled conditions in EITHER configuration -- v1 (llama3.1:8b) or
  v2 (Nemotron-3.5-Lightning-30B-A3B, freshly re-extracted bundle, different-family
  non-self judge). The point estimate's SIGN was not stable between the weak and strong
  generator, and no test approached significance in either run; at these hallucination
  counts (1-5 events/arm) the difference is indistinguishable from noise. The one
  consistent, non-noisy effect is context cost: OKF-RAG answered the same questions on
  fewer retrieval tokens in both runs (-28% v1, -10% v2). f1/em: OKF ~= chunk in both.
- **Secondary (v2 human):**
  - context cost: okf 1472.8 vs chunk 1644.5 tok/question, **-10.4%** (efficiency claim
    holds, smaller than v1's -28% because this question set + Nemotron bundle retrieve
    differently).
  - calibration: both arms abstained correctly on all 10 unanswerable. On ANSWERABLE
    questions chunk abstained 8x, okf 7x -- **roughly equal**; the 2026-08-28 hint that
    "OKF abstains more honestly on retrieval misses" does NOT replicate here.
  - **9 reasoning-miss abstentions** (answer derivable from context, model said
    INSUFFICIENT CONTEXT): 3 full (chunk Q127, okf Q126, okf Q133) + 6 partial, almost all
    multi-hop -- BOTH arms; neither retrieval substrate clearly helps the model synthesise
    2-doc answers.
  - grounded-but-wrong / borderline: Q064 chunk `unsupported` (ungrounded closing
    generalisation), Q070 okf `contradicted` (attributes Service routing to
    kubelet/CCM vs the context's service-proxy) -- the sole okf hallucination.
- **Files:** `results/v2_kaggle/{table_main_human.csv, table_main_human.tex,
  table_hop_human.csv, table_expansion_human.csv, significance_human.txt,
  fig_main_human.png, fig_hop_human.png, fig_cost_human.png}` + the `_judge` set.
  `scored_okf_rag_v2_kaggle_full.csv` now carries the human labels + notes.
- **STATUS: v2 pipeline complete through analysis. Checklist items 7-10 done.** Remaining:
  write up; the paper's headline is the combined v1+v2 null on hallucination + the
  consistent context-cost reduction.
