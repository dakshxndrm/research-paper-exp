!!! SUPERSEDED - INVALID: these results were generated against the V1 BUNDLE
!!! (data/okf_bundle was a byte-identical copy of PUBLICATION_v1's bundle).
!!! Superseded by a fresh-bundle rerun. Kept for reference only - do not cite.
!!! See _SUPERSEDED_README.md in this directory.

# `claude_label` — a third independent judge on v2 (2026-08-28)

## What this is, and what it is NOT

**It is NOT `human_label`.** No human graded these 120 rows. I graded them.
`human_labelling_sheet_v2.csv` is still blank and still needs you.

`claude_label` is a **third independent LLM judge**, deliberately named for what it
actually is. Its value is that it is a *different model family* from both the
generator (`Nemotron-3-Nano-30B-A3B`) and the v2 judge (`qwen2.5:7b-instruct`), so
agreement/disagreement between the two judges is a real, reportable signal about
judge reliability. It is **not ground truth** and must not be substituted for
`human_label` in the paper.

If you read these labels and agree with them, promoting them to `human_label` is
your call to make explicitly — that decision is not mine to make silently.

## Method (identical rubric to the pipeline's judge)

- I used **`JUDGE_SYSTEM` from `src/evaluate.py` verbatim**: classify each answer as
  `supported` / `unsupported` / `contradicted` / `abstained`, judging **grounding in
  the retrieved context only**, explicitly *not* real-world correctness.
- I judged against **the exact context the generator and Qwen saw**, reconstructed
  with `evaluate.rebuild_contexts()` (retrieval is deterministic). Verified: all 120
  rebuilt contexts contain every id in that row's `retrieved_ids` — 0 mismatches.
- I read all 120 rows in full. Every label has a note in `claude_note`; borderline
  calls are marked `BORDERLINE`, clear ones `CLEAR`.

## Result — OKF hallucinates MORE, same direction as v1 and as the Qwen judge

Paired on the same 60 questions, `n_boot=10000`, `seed=42` (pipeline's own
`paired_bootstrap`):

| metric | chunk | okf | delta | bootstrap p | McNemar |
|---|---|---|---|---|---|
| **claude_hallucination** | 0.1000 | 0.1833 | **+0.0833 (okf worse)** | 0.1333 | 8/3, p=0.2266 |
| judge_hallucination (Qwen) | 0.0667 | 0.1167 | +0.0500 (okf worse) | 0.2953 | 5/2, p=0.4531 |
| f1 | 0.3440 | 0.3008 | −0.0432 | 0.1295 | — |
| em | 0.0000 | 0.0000 | 0.0000 | 1 | no discordant pairs |
| retrieval_recall (n=52 answerable) | 0.8558 | 0.7981 | −0.0577 | 0.2762 | — |

Answerable questions only (n=52): chunk 0.1154 vs okf 0.2115, delta +0.0962, p=0.1585.

**Nothing is significant at n=60.** The honest reading is unchanged from v1: *no
detectable difference, with the point estimate favouring the chunk baseline* — now
reproduced on a stronger, different-family generator/judge pair, and by a third
judge that is stricter than either.

## Judge-vs-judge agreement (the actually novel number here)

120 rows, `claude_label` vs Qwen `judge_label`:

- **exact label agreement 0.900 (108/120)**
- binary hallucination agreement 0.900, **Cohen's κ = 0.518** (moderate)
- perfect agreement on all 22 abstentions
- I am **stricter**: I flag 17 hallucinations, Qwen flags 11. I overturned 3 of
  Qwen's `unsupported` calls to `supported`, and flagged 9 rows Qwen called
  `supported` (7 unsupported + 2 contradicted).

κ = 0.52 between two capable, different-family judges on the same rubric and the
same contexts is itself a finding: **single-judge hallucination rates on this task
carry real judge-dependent variance**, which strengthens rather than weakens the
project's standing caveat that human labels are the trustworthy metric.

## Calibration: OKF abstains more, and mostly for the right reason

| arm | abstentions | on the 8 unanswerable | on answerable |
|---|---|---|---|
| chunk | 9 | 8/8 | 1 (Q007) |
| okf | 13 | 8/8 | 5 (Q016, Q017, Q028, Q029, Q066) |

Both arms abstained correctly on **all 8** unanswerable questions. OKF's 5 extra
abstentions are retrieval misses it handled honestly rather than confabulating —
including **Q066, where the chunk arm hallucinated** and OKF correctly said
`INSUFFICIENT CONTEXT`. That is a genuine OKF advantage the hallucination rate alone
hides.

## Where the arms actually diverge (11 questions)

Favouring **chunk** (8): Q005, Q013, Q045, Q067, Q070, Q074, Q078, Q079
Favouring **okf** (3): Q012, Q073, Q066(okf abstained vs chunk hallucinated)

Worth reading before you label:

- **Q073** — OKF's best win. It got *both* halves (PV `Terminating` finalizer +
  `blockOwnerDeletion`); chunk missed the finalizer entirely. Exactly the multi-hop
  case OKF is designed for.
- **Q056, Q039, Q007, Q012** — OKF answered correctly where chunk retrieved the
  wrong chunk or abstained.
- **Q013** — OKF's worst failure. The Job-controller concept was never retrieved
  (it got Service-controller and TTL-controller concepts instead) and the model
  confabulated "the Job controller … creates Jobs". Retrieval miss → hallucination.
- **Q078** — chunk got `Permit` right from its chunk; OKF invented "the Gang
  Scheduler" as an extension point because the `Permit` concept wasn't retrieved.

## Two substrate defects this surfaced (independent of retrieval quality)

1. **A truncated concept.** `/process/how_finalizers_work.md` ends literally with
   `does the following: ...` — the enumerated list (which contains the `202` answer
   to **Q029**) was cut at extraction time. OKF abstained on Q029; chunk answered it
   correctly. This is a **bundle defect, not a retrieval failure**, and it is a
   concrete instance of the extraction-quality problem beyond the known
   `min_concept_words` issue.
2. **Cross-link markup leaking into answers.** Q020's answer contains
   `metadata.[ownerReferences]` — the OKF markdown link syntax bled into generated
   text. Cosmetic here, but it means link markup is reaching the generator.

## Caveat that matters for interpreting `supported`

The rubric grades **grounding, not correctness**. Several rows are `supported` while
being the *wrong answer to the question*, because the model faithfully reported
whatever was retrieved:

- **Q048 (okf)** — correctly reports the retrieved 4-attribute identity concept;
  gold is `UID`, whose concept wasn't retrieved. Grounded, wrong.
- **Q039 (chunk)** — grounded in the retrieved dual-stack chunks, answers about
  Service `ipFamilyPolicy` rather than cluster IP families.

So `1 − hallucination` is **not** accuracy. If the paper wants accuracy, that needs
a separate correctness pass — which the human labelling sheet can capture.

## Files

- `scored_okf_rag_v2_kaggle_full_CLAUDE.csv` — the 120 scored rows plus
  `claude_label`, `claude_note`, `claude_hallucination`
- `significance_CLAUDE.txt` — full paired output, agreement crosstab, abstention
  breakdown
- `human_labelling_sheet_v2.csv` — **still blank, still yours**
