# OKF-RAG: Does the Open Knowledge Format reduce hallucination in RAG?

Experimental harness comparing two retrieval substrates over the **same corpus**,
the **same generator model**, and the **same context token budget**:

| Arm | Retrieval substrate |
|---|---|
| **A — baseline** | fixed-size overlapping text chunks over raw documents |
| **B — OKF-RAG** | curated OKF v0.1 concept bundle + markdown cross-link expansion |

Only the substrate differs. Everything else is held constant, which is what
makes any observed difference attributable to OKF.

---

## 0. Requirements

- Python 3.10+
- ~4 GB free RAM
- A generator LLM. Cheapest path is **Ollama** running locally:

```bash
# install ollama from https://ollama.com, then:
ollama pull llama3.1:8b
ollama serve
```

No GPU? Use `llama3.2:3b` instead, or switch `generation.provider` to `gemini`
in `config.yaml` and export a free AI Studio key:

```bash
export LLM_API_KEY="your-key-here"
```

Install:

```bash
pip install -r requirements.txt
```

---

## 1. Get your corpus in

Drop 30–50 `.md` or `.txt` documents into `data/raw/`.

**Corpus selection is the single most important decision in this project.**
It must have genuine cross-references between documents — Document A mentions a
rule defined in Document B. Without that, link expansion has nothing to expand
and OKF-RAG collapses into ordinary RAG.

Good candidates:
- your college's academic regulations + examination + hostel + fee handbooks
- an open-source project's docs (API reference + guides + changelog)
- a government scheme's guidelines + eligibility + application procedure documents

Bad candidates: news articles, blog posts, anything where each document stands
completely alone.

**Smoke test first.** Copy the two toy documents in and verify the whole
pipeline runs end to end before investing in the real corpus:

```bash
cp data/sample_corpus/*.md data/raw/
```

---

## 2. Write the question set

Edit `questions/questions.csv`. Delete the example rows. Target **80–100
questions**:

| hop_type | how many | what it tests |
|---|---|---|
| `single` | ~50 | fact stated in one place |
| `multi` | ~30 | needs two documents/concepts combined — **where OKF should win** |
| `unanswerable` | ~15 | corpus is silent; correct answer is `INSUFFICIENT CONTEXT` |

Columns:
- `gold_answer` — the short correct answer, or the literal string `UNANSWERABLE`
- `gold_concepts` — semicolon-separated units that *should* be retrieved. Use
  concept paths for OKF (`policies/attendance_requirement.md`) or source
  filenames for chunks. Substring matching handles both.

**Write these before you look at any model output.** Writing questions after
seeing what the system answers well is how you accidentally rig your own study.

---

## 3. Run it

```bash
python scripts/preflight.py          # verify everything is reachable
python -m src.build_bundle           # raw docs -> OKF bundle
python -m src.run_experiment --limit 5   # smoke test on 5 questions
python -m src.run_experiment         # full main run, both arms
```

Or everything including ablations:

```bash
bash scripts/run_all.sh
```

Then score and aggregate:

```bash
python -m src.evaluate --input raw_okf_rag_v1_full.csv
python -m src.analyze --inputs scored_okf_rag_v1_full.csv
```

---

## 4. Hand-label the sample — do not skip this

`src/evaluate.py` writes `results/human_labelling_sheet.csv`. Fill the
`human_label` column yourself with `supported` / `unsupported` /
`contradicted` / `abstained`. Then:

```bash
python -m src.analyze --inputs scored_okf_rag_v1_full.csv --label-col human_label
```

The LLM judge is a screening tool. An 8B model judging an 8B model's output is
not a trustworthy ground truth, and a reviewer will say so. **Report human
labels as the headline number** and report the judge's agreement with your
labels as a secondary validity check.

---

## 5. What to send me for the paper

Zip and upload `results/` — specifically:

- `table_main.csv`, `table_hop.csv`, `table_ablation.csv`
- `significance.txt`
- `bundle_stats.json`
- `fig_main.png`, `fig_hop.png`, `fig_cost.png`
- the scored CSVs (with `human_label` filled in)
- your final `config.yaml` and `questions/questions.csv`

Plus a note on: which corpus you used, how many documents, and anything that
broke or surprised you. Then the paper gets written around whatever those
numbers actually say.

---

## Methodology notes (these go into the paper)

**Controlled variables.** Same generator, temperature 0.0, fixed seed, identical
system prompt, identical context token budget (`retrieval.context_token_budget`).
Token counting uses a 4-chars-per-token approximation applied identically to
both arms.

**Deterministic cross-linking.** Concept *extraction* is LLM-assisted; concept
*linking* is pure rule-based title matching (`src/build_bundle.py:cross_link`).
This is deliberate — link expansion is the mechanism the paper claims credit
for, so it must be auditable and cannot be accused of smuggling in answers.

**Ablations available** (`--ablation`): `no_expansion`, `embed_full_body`,
`two_hop`, `with_freshness`. `no_expansion` is the important one: if OKF-RAG's
advantage survives with expansion disabled, the win comes from concept
granularity; if it disappears, the win comes from the link graph. Either result
is a real finding.

**Statistics.** `src/analyze.py` runs a paired bootstrap (10,000 resamples) and
an exact McNemar test on the binary outcomes. With ~100 questions, expect wide
confidence intervals. A non-significant result is a legitimate finding — report
it honestly rather than quietly dropping it.

**Known threats to validity**, to state in the paper's limitations section:
1. Bundle quality depends on the extraction LLM; a weak extractor caps Arm B.
2. Single corpus, single domain — external validity is limited.
3. Approximate token counting.
4. Question set authored by the same person running the experiment.
5. LLM-judge self-preference bias, partially mitigated by human labels.
