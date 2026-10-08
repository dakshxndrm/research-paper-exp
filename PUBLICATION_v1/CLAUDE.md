# OKF-RAG — project guide

Read `PROJECT_MAP.md` first if you're picking the project back up after a
gap. For the file-by-file audit see `results/DETAILED_AUDIT.md`
(the old `results/INVENTORY.md` is superseded, now in `archive/`).

**v1 outputs are frozen in `results/v1_FINAL/` — do not rewrite them. v2 runs
write to `results/v2_IN_PROGRESS/`.**

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
| Human labels — both arms | **PASS** | 120 labelled rows in `v1_FINAL/scored_okf_rag_v1_full.csv` (60 okf + 60 chunk). Source sheets: `v1_FINAL/human_labels_okf_rag_v1_full_OKF.csv`, `..._CHUNK.csv`. |
| Paired human comparison | **PASS — 60 paired questions** | `v1_FINAL/significance_human.txt`. |
| Link precision | **PASS** | 100-link seed-42 sample fully graded; merged into `v1_FINAL/bundle_stats_alias.json`. |
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
    v1_FINAL/scored_okf_rag_v1_full.csv v1_FINAL/scored_okf_rag_v1_no_expansion.csv \
    v1_FINAL/scored_okf_rag_v1_embed_full_body.csv v1_FINAL/scored_okf_rag_v1_two_hop.csv \
    v1_FINAL/scored_okf_rag_v1_title_only.csv

# Analyze — HUMAN labels, the headline -> *_human.*
python -m src.analyze --inputs v1_FINAL/scored_okf_rag_v1_full.csv --label-col human_label

# Link precision (grade a link_audit_*.csv `verdict` column first)
python scripts/link_precision.py --input v1_FINAL/link_audit_RANDOM100.csv \
    --stats v1_FINAL/bundle_stats_alias.json

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
- Moved v1's 33 output artefacts to `results/v1_FINAL/`, logs to `results/logs/`,
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
- Extracted the 60 human-labelled qids from `v1_FINAL/scored_okf_rag_v1_full.csv`;
  okf and chunk label the identical qid set. Written to
  `results/v2_IN_PROGRESS/v2_qids.txt` (39 single / 13 multi / 8 unanswerable).
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
  rows of `v1_FINAL/scored_okf_rag_v1_full.csv`; verified locally to match
  `v2_IN_PROGRESS/v2_qids.txt` exactly), both arms = 120 generations + 120 judge calls.
  Writes to `results/v2_kaggle/`, nowhere near `v1_FINAL/`.
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
  `data/okf_bundle/`, `questions/questions.csv`, `results/v1_FINAL/scored_okf_rag_v1_full.csv`,
  `src/`, `config.yaml`, `pyproject.toml`.
