# OKF-RAG v1 — Publication Evidence

This folder contains everything needed to prove and reproduce the v1 result.
Every file here is a **copy**; the originals remain in the working project and
were not modified. Nothing in this folder comes from v2.

## Headline result

Paired comparison on the **60 human-labelled questions** (both arms answered the
identical qid set), `ablation=full`, `link_mode=alias`. Source:
`results/significance_HUMAN.txt`, `results/table_main_HUMAN.csv`.

| metric | chunk | okf | delta (okf − chunk) | bootstrap p | McNemar exact p |
|---|---|---|---|---|---|
| **hallucination** | 0.0333 | 0.0833 | **+0.0500** (okf worse) | 0.3056 | 0.4531 (discordant 5/2) |
| f1 | 0.3151 | 0.2869 | −0.0282 | 0.3108 | — |
| em | 0.0000 | 0.0167 | +0.0167 | 0.5248 | 1.0 (discordant 1/0) |
| retrieval_recall | 0.7417 | 0.6917 | −0.0500 | 0.1963 | — |

n = 60 paired questions per arm (120 human-labelled rows total).

**The headline result is a null.** Nothing is significant. The honest reading is
"no detectable difference, with the point estimate favouring the chunk baseline"
— not "OKF-RAG is worse".

OKF-RAG does win decisively on **context cost**: **1,162.6 tokens/question vs the
baseline's 1,615.4 — a 28% reduction** — while answering the same questions.
That is the defensible positive claim in this data.

Judge labels (all 600 rows, `results/table_ablation.csv`) agree on direction:
chunk 0.03 vs okf 0.05 hallucination. The v1 judge is the same model as the v1
generator, so it is a screening tool only (see Known limitations).

## What's in this folder

| Path | Contents | Why it is here |
|---|---|---|
| `config.yaml` | main (alias-mode) experiment config | fixes retrieval, embedding, budget and seed for both arms |
| `config_title_only.yaml` | title-only ablation config | the only config delta for the title_only bundle |
| `questions/questions.csv` | the 100 human-authored questions | one of the two human-input stages; 52 single / 33 multi / 15 unanswerable |
| `data/raw/` | the 40 source Kubernetes docs | the shared corpus — both arms retrieve over exactly this |
| `data/corpus_selection.json` | the selected doc paths | records which 40 docs were chosen, and therefore why |
| `bundle/okf_bundle_stats.json` | alias bundle stats + graded link precision | 371 concepts, 1,103 cross-links; carries the link-precision block |
| `bundle/okf_bundle_title_only_stats.json` | title-only bundle stats | 371 concepts, 387 cross-links |
| `bundle/okf_bundle/` | the 371 concept units themselves, across 57 type folders | the OKF retrieval substrate — the thing Arm B actually retrieves over |
| `bundle/concept_paths.txt` | manifest of the 371 concept files | flat index of the bundle, for checking the count and the type distribution at a glance |
| `results/scored_okf_rag_v1_full.csv` | 200 scored rows, 120 with `human_label` merged in | **the primary evidence file** — every number above derives from it |
| `results/table_main_HUMAN.csv` | per-arm human-label means | the headline table |
| `results/table_hop_HUMAN.csv` | human-label means split by hop_type | single / multi / unanswerable breakdown |
| `results/table_expansion_HUMAN.csv` | human-label means by expansion status | whether link expansion actually fired |
| `results/significance_HUMAN.txt` | bootstrap + McNemar output | the paired significance test |
| `results/table_ablation.csv` | judge-label means, all 5 ablation groups | the ablation sweep (judge labels; no human labels exist on ablation arms) |
| `results/link_audit_RANDOM100.csv` | the graded 100-link sample (seed 42) | the evidence behind the link-precision numbers |
| `results/link_audit_alias_FROZEN.csv` | full 1,103-link audit snapshot | the population the 100-link sample was drawn from |
| `results/fig_*_HUMAN.png` | main / hop / cost figures | the human-label analysis figures |
| `results/table_main_HUMAN.tex` | LaTeX form of the main table | paste-ready |
| `human_labelling/human_labelling_sheet_FINAL.csv` | OKF arm, 60 labelled rows | the raw human labelling sheet |
| `human_labelling/human_labelling_sheet_CHUNK_FINAL.csv` | chunk arm, 60 labelled rows | the raw human labelling sheet |
| `src/` | the pipeline code that produced these results | reproducibility |
| `scripts/` | `preflight.py`, `link_precision.py` | the two scripts the verification commands below call |
| `CLAUDE.md` | full project log | the running record of decisions, blockers and caveats |

**Deliberately excluded:** `raw_*.csv` (pre-scoring intermediates), `bundle_debug/`
(LLM extraction cache, not evidence), `archive/`, run logs, scratch and probe
files, `.env`, and everything under `results/v2_IN_PROGRESS/`.

## How to verify these numbers yourself

Run these **from the original project root**, not from inside this folder — the
code expects the project's `results/` layout and an editable install.

```bash
# One-time: make src/ importable
pip install -e .

# Sanity check corpus, questions, embedder, generator LLM and bundle
python scripts/preflight.py

# Reproduce the HEADLINE (human-label) tables, figures and significance test
python -m src.analyze --inputs v1_FINAL/scored_okf_rag_v1_full.csv --label-col human_label

# Reproduce the ablation table (judge labels, all 5 groups)
python -m src.analyze --inputs \
    v1_FINAL/scored_okf_rag_v1_full.csv v1_FINAL/scored_okf_rag_v1_no_expansion.csv \
    v1_FINAL/scored_okf_rag_v1_embed_full_body.csv v1_FINAL/scored_okf_rag_v1_two_hop.csv \
    v1_FINAL/scored_okf_rag_v1_title_only.csv

# Reproduce the link-precision block inside bundle/okf_bundle_stats.json
python scripts/link_precision.py --input v1_FINAL/link_audit_RANDOM100.csv \
    --stats v1_FINAL/bundle_stats_alias.json

# Regression tests (no model download, no LLM calls)
python tests/test_logic.py && python tests/test_expansion.py
```

Two naming notes, so the comparison is unambiguous:

- `analyze.py` writes **lowercase** `_human` / `_judge` suffixes
  (`table_main_human.csv`, `significance_human.txt`, `fig_main_human.png`).
  Those files were copied here under **uppercase** `_HUMAN` names for legibility.
  The contents are byte-identical — compare content, not filename.
- `results/table_ablation.csv` here is the file `analyze.py` emits as
  `table_ablation_judge.csv`.

The ablation sweep also needs the four other `scored_okf_rag_v1_*.csv` files,
which live in the project's `results/v1_FINAL/` and are not duplicated here —
only the main 200-row scored file is publication evidence.

## Known limitations

These must appear in the paper.

- **The headline result is null.** No metric is significant at n=60. Report it as
  "no detectable difference, point estimate favouring the baseline".
- **Link precision in alias mode is poor.** Over the graded 100-link sample:
  strict 0.44, lenient 0.79. Split by match type, `title` links are 0.778 strict /
  0.963 lenient but `alias` links are only **0.315 strict** / 0.726 lenient. Alias
  matching produces most of the graph (1,103 links vs title_only's 387), so most
  of Arm B's link expansion runs on low-precision edges. This is the most likely
  mechanical explanation for the null result and should be stated as such.
- **Concept extraction used multiple models across sessions** because of API quota
  exhaustion. Groq `gpt-oss-120b` and Gemini `2.5-flash` were tried first and hit
  hard quota walls; the corpus was ultimately re-extracted end-to-end on **local
  Ollama `llama3.1:8b`**, which produced the bundle these numbers come from.
- **Generation and judging both ran on the same model** (`llama3.1:8b`, local
  Ollama), so the v1 LLM judge has a self-preference bias. **Human labels are the
  trustworthy metric; `judge_label` is a screening tool only.**
- **`min_concept_words` filtering discarded 108 of 479 extracted concepts (23%)**,
  including at least 3 that were the correct answer to a question (Q003 etcd,
  Q005 kubelet, Q096 kube-apiserver). Some questions are therefore harder for the
  OKF arm than intended, independent of retrieval quality — the gold concept never
  made it into the bundle at all.
- **`retrieval_recall` for the OKF arm uses a document→concept mapping layer**
  (`src/evaluate.py:expand_gold_to_concepts`), expanding each gold document to
  every concept extracted from it (median ~11). This is a deliberately **loose,
  optimistic upper bound for OKF** and is **not like-for-like** against the chunk
  arm's document-granularity recall. OKF still loses on this metric despite the
  handicap being in its favour.
- **Human labelling covers 60 of 100 questions per arm**, and **0 rows on any
  ablation arm** — the ablation table is judge-labelled only.
- **Link precision is estimated from 100 of 1,103 links** (seed 42), so it carries
  no meaningful confidence interval yet.

## Relationship to v2

v2 is a separate, independent replication of this experiment, not a continuation
of it. It reuses v1's corpus, bundle, question set (the same 60 human-labelled
qids) and pipeline code unchanged, and varies only the model pair: v2 runs
stronger, hallucination-benchmarked generator and judge models drawn from
**different model families**, which retires v1's self-preference-bias caveat. It
executes on Kaggle via a notebook rather than on local Ollama. Its purpose is to
test whether the v1 null holds under a different model pair. **v2 lives entirely
outside this folder, writes to its own results directory, and is not part of the
v1 evidence.** No v2 output should ever be cited as backing a number in this
folder.
