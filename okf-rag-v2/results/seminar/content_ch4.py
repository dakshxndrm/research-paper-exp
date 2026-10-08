# -*- coding: utf-8 -*-
CH4 = [
('h1', 'CHAPTER 4\nSNAPSHOTS AND SYSTEM ARTEFACTS'),

('p', 'The system has no graphical interface. Everything runs from the command line and writes files, '
      'so what follows are the artefacts a run produces rather than screen layouts. Each section '
      'shows the artefact and marks where a live screenshot should be pasted before submission.'),

('h2', '4.1 Project Layout'),
('p', 'Source, data, questions and results are separated so that a reader can tell at a glance which '
      'files are inputs and which are outputs. The frozen results of the first configuration live in '
      'a read-only reference directory that nothing in the pipeline writes to.'),
('c', 'okf-rag-v2/\n'
      '  config.yaml                     base configuration\n'
      '  config_v2_kaggle.yaml           v2 overrides (extends config.yaml)\n'
      '  data/raw/                       40 Kubernetes source documents\n'
      '  data/okf_bundle/                358 concept units, 78 type directories\n'
      '  questions/questions.csv         122 hand-authored questions\n'
      '  src/                            9 modules: config, llm, chunk_rag, okf_rag,\n'
      '                                  build_bundle, run_experiment, evaluate, analyze\n'
      '  results/v1_reference/           frozen configuration-v1 evidence (read-only)\n'
      '  results/v2_kaggle/              configuration-v2 outputs\n'
      '  results/v2_active_qids_v2.txt   the 65 active question ids'),
('ph', '[SCREENSHOT: terminal output of the project directory listing]'),

('h2', '4.2 Configuration File'),
('p', 'Configuration is declarative and versioned. The extract below is the retrieval block, which '
      'is byte-identical between the two configurations; that identity is what allows the second run '
      'to be described as a change of models rather than a change of method.'),
('c', 'retrieval:\n'
      '  context_token_budget: 1800\n'
      '  chunk:\n'
      '    chunk_size_tokens: 512\n'
      '    chunk_overlap_tokens: 64\n'
      '    top_k: 8\n'
      '  okf:\n'
      '    top_k: 5\n'
      '    hop_expansion: 1\n'
      '    max_expanded: 4\n'
      '    embed_field: title_description\n\n'
      'generation:\n'
      '  model: "...NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF:Q4_K_M"\n'
      '  temperature: 0.0\n'
      '  max_tokens: 8000\n'
      '  seed: 42\n\n'
      'judge:\n'
      '  enabled: true\n'
      '  model: "qwen2.5:7b-instruct"\n'
      '  temperature: 0.0'),
('ph', '[SCREENSHOT: config_v2_kaggle.yaml open in the editor]'),

('h2', '4.3 Running the Pipeline'),
('p', 'Each stage is a module invocation. Generation and scoring are resumable, so re-issuing the '
      'same command after a crash picks up where the previous attempt stopped instead of paying for '
      'completed rows twice.'),
('c', '# build the bundle from the raw corpus\n'
      'python -m src.build_bundle\n\n'
      '# generate answers for both arms on the active question set\n'
      'python -m src.run_experiment --qids-file results/v2_active_qids_v2.txt\n\n'
      '# score and judge\n'
      'python -m src.evaluate --input raw_okf_rag_v2_kaggle_full.csv\n\n'
      '# merge the completed human labelling sheet back into the scored file\n'
      'python scripts/merge_human_labels.py \\\n'
      '    --sheet  v2_kaggle/human_labels_okf_rag_v2_kaggle_full.csv \\\n'
      '    --scored v2_kaggle/scored_okf_rag_v2_kaggle_full.csv\n\n'
      '# tables, significance tests and figures from the human labels\n'
      'python -m src.analyze --inputs v2_kaggle/scored_okf_rag_v2_kaggle_full.csv \\\n'
      '    --label-col human_label'),
('ph', '[SCREENSHOT: terminal showing a generation run in progress with the per-row progress bar]'),
('ph', '[SCREENSHOT: the Kaggle notebook GPU panel showing both T4 accelerators active]'),

('h2', '4.4 A Retrieved Context, Side by Side'),
('p', 'Question Q001 asks what the two major parts of a Kubernetes cluster are. Both arms answer it '
      'correctly, and comparing what each was given is the clearest illustration of the difference '
      'between the substrates.'),
('h3', '4.4.1 Baseline Arm'),
('c', 'retrieved_ids:\n'
      '  overview__components.md#chunk0\n'
      '  architecture__controller.md#chunk2\n'
      '  architecture.md#chunk3\n'
      '  overview.md#chunk4\n\n'
      'answer:\n'
      '  The two major parts of a Kubernetes cluster are the control plane and\n'
      '  one or more worker nodes.\n'
      '  SOURCES: [overview__components.md#chunk0]'),
('h3', '4.4.2 Curated Arm'),
('c', 'retrieved_ids (5 seeds + 4 expanded):\n'
      '  definition/kubernetes_cluster_architecture_overview.md\n'
      '  entity/node_components.md\n'
      '  section/managing_a_kubernetes_cluster.md\n'
      '  policy/cluster_administration_overview.md\n'
      '  entity/control_plane_components.md\n'
      '  definition/node_components.md          <- expanded\n'
      '  definition/control_plane_components.md <- expanded\n'
      '  definition/kube_apiserver.md           <- expanded\n'
      '  definition/etcd.md                     <- expanded\n\n'
      'answer:\n'
      '  A Kubernetes cluster consists of a control plane and worker nodes (also\n'
      '  called nodes). The control plane manages the overall state of the cluster,\n'
      '  while the worker nodes run containerized applications in the form of Pods.\n'
      '  SOURCES: [concept: /definition/kubernetes_cluster_architecture_overview.md]'),
('p', 'Four of the nine curated units arrived through link expansion rather than through similarity '
      'ranking, and the citation points at a specific concept file rather than at a numbered slice '
      'of a page. That is the finer-grained attribution the format buys. Whether it buys grounding '
      'is the question Chapter 3 answers, and the answer is no.'),
('ph', '[SCREENSHOT: scored_okf_rag_v2_kaggle_full.csv open in a spreadsheet, showing the '
       'question, answer, retrieved_ids, judge_label and human_label columns for a few rows]'),

('h2', '4.5 Output Artefacts'),
('p', 'A completed run leaves a fixed set of files, and every filename records what produced it so '
      'that one run cannot silently overwrite another. Table 4.1 lists them.'),
('t', 'Table 4.1 Artefacts produced by a full run',
 [['File', 'Contents'],
  ['raw_<run>.csv', 'One row per arm and question: answer, retrieved ids, timings, token counts'],
  ['scored_<run>.csv', 'The raw rows plus EM, F1, recall, citation validity, judge and human labels'],
  ['human_labels_<run>.csv', 'Blank labelling sheet, refuses to overwrite a sheet already filled in'],
  ['runmeta_<run>.json', 'Flattened configuration exactly as the run used it'],
  ['bundle_stats_<mode>.json', 'Concept and link counts, alias diagnostics, link precision'],
  ['bundle_provenance.json', 'Tree hash, builder model, and comparison against the v1 hash'],
  ['link_audit_<mode>.csv', 'Every link with its match type; carries hand-graded verdicts forward'],
  ['table_*_human.csv / .tex', 'Analysis tables, human-label variant'],
  ['significance_human.txt', 'Bootstrap and McNemar results for the paired comparison'],
  ['fig_*_human.png', 'Generated figures'],
 ]),
('ph', '[SCREENSHOT: the results/v2_kaggle directory listing showing the generated artefacts]'),

('h2', '4.6 The Labelling Sheet'),
('p', 'Human labelling is done on a generated sheet rather than by editing the scored file directly, '
      'so that the labels can be merged back in a separate, repeatable step. The sheet carries the '
      'question, the answer and a blank label column; a merge script keyed on arm, ablation and '
      'question identifier writes the labels into the scored file and refuses to proceed if the keys '
      'do not line up.'),
('c', 'arm,ablation,qid,question,answer,human_label,human_notes\n'
      'chunk,full,Q001,"What are the two major parts of a Kubernetes cluster?",...,,\n'
      'okf,full,Q001,"What are the two major parts of a Kubernetes cluster?",...,,\n'
      '...\n'
      '# 130 rows: 65 questions x 2 arms, human_label blank'),
('ph', '[SCREENSHOT: the completed labelling sheet with human_label and human_notes filled in]'),
('ph', '[SCREENSHOT: the plotted figures fig_main_human.png and fig_hop_human.png as generated '
       'by the analysis stage]'),
]

CH5 = [
('h1', 'CHAPTER 5\nLIMITATIONS'),

('p', 'A null result places a heavier burden on the limitations section than a positive one does, '
      'because a reader is entitled to ask whether the effect was simply missed. What follows is '
      'every reason we know of to doubt the conclusion, stated without softening.'),

('h2', '5.1 Statistical Power'),
('p', 'This is the binding constraint on everything else. With 60 and 65 paired questions and '
      'hallucination rates between one and eight per cent, the actual number of events is tiny: five '
      'and two in the first configuration, one and two in the second. Any comparison resting on three '
      'to seven events is underpowered for the effect sizes anyone would care about.'),
('p', 'The practical consequence is worth spelling out. In the second configuration, relabelling a '
      'single borderline row would change the sign of the headline difference, and all three '
      'hallucination events in that run were borderline calls. So the correct reading is not '
      '*OKF-RAG does not reduce hallucination*; it is *this experiment could not have detected a '
      'reduction of the size that is plausible here*. Distinguishing a three-point difference from '
      'zero at these base rates needs several hundred questions per arm, which is an order of '
      'magnitude more hand-authoring than this project could fund.'),

('h2', '5.2 Link Precision Limits the Mechanism'),
('p', 'Section 3.6 is a limitation as much as it is a finding. Link expansion is the mechanism the '
      'whole design depends on, and it was running on a graph whose majority component is correct '
      '31.5% of the time. The hypothesis was therefore tested in a degraded form. A fair test needs '
      'the alias filter built and the run repeated, and until that happens the null should be read as '
      '*not demonstrated at this link precision* rather than as a refutation.'),

('h2', '5.3 The Concept Filter Discards Answers'),
('p', 'The minimum-word filter applied after extraction removed 108 of 479 concepts in the first '
      'configuration, about 23% of everything the extractor produced. Three of the discarded units '
      'were the correct answer to a question in the set — the concepts covering etcd, the kubelet '
      'and the kube-apiserver. Those questions were unanswerable for the curated arm no matter how '
      'good its retrieval was, because the gold material never entered the bundle. The filter '
      'handicaps the arm it was meant to clean up, and lowering or removing it is an obvious repair.'),

('h2', '5.4 Retrieval Recall Is Not Measured Like for Like'),
('p', 'The baseline is credited with a retrieval hit when it returns a chunk from a gold document. '
      'The curated arm is credited when it returns any concept extracted from a gold document, and a '
      'gold document typically yields around eleven concepts. That mapping is deliberately generous '
      'to the curated arm, and the recall figures in Tables 3.5 and 3.6 are therefore an optimistic '
      'upper bound for it and not a fair comparison. Note the direction of the bias: the curated arm '
      'still lost this metric in the first configuration despite the handicap running in its favour. '
      'A like-for-like measurement requires concept-level gold annotations, which do not exist yet.'),

('h2', '5.5 Labelling Is Author-Performed and Single-Annotator'),
('p', 'All human labels in both configurations were assigned by the author of the system. There was '
      'no second annotator and therefore no inter-annotator agreement statistic. The risk of '
      'unconscious bias toward the curated arm is real and cannot be measured from inside the study.'),
('p', 'Three things partly offset it, and none of them removes it. Labels were assigned strictly '
      'against reconstructed retrieved context under the same written rubric the judge used, with '
      'the rubric fixed before labelling began. Every context was verified to contain each unit the '
      'run recorded. And the notes on all three hallucination events record the reasoning explicitly, '
      'including the cases where the opposite label was defensible, so the decisions can be audited '
      'and overturned by a reader. An independent second annotator remains the correct fix.'),

('h2', '5.6 Judge Variance'),
('p', 'The kappa of 0.518 measured between two independent judges grading identical rows against an '
      'identical rubric is a limitation of the measurement instrument and not merely a curiosity. It '
      'says that LLM-judged hallucination rates carry judge-dependent variance comparable in size to '
      'the effects being measured. It applies to this study, and it applies to any study that reports '
      'a single-judge hallucination number without a second grader.'),

('h2', '5.7 Multi-Hop Under-Representation'),
('p', 'Verified multi-hop questions make up 18 of 65, or 27.7%, of the active set. That is below the '
      'share intended when the corpus was chosen, and multi-hop is precisely the category where link '
      'expansion has the strongest theoretical claim. The ceiling is hard rather than budgetary: only '
      '18 questions in the authored file survive the cover-one-up test, so raising the proportion '
      'would mean cutting single-hop questions and shrinking an already small sample. Both options '
      'are bad, and the one chosen is recorded here.'),

('h2', '5.8 Single Corpus and Single Domain'),
('p', 'All results come from forty pages of Kubernetes documentation. That corpus was picked because '
      'it is favourable to the hypothesis — dense, heavily cross-referenced technical prose is where '
      'curated linking should help most — so the null is arguably stronger evidence than it would be '
      'on neutral material. But nothing here establishes what happens on legal text, clinical notes '
      'or conversational logs, and it would be wrong to extrapolate.'),

('h2', '5.9 Model Mixing During Bundle Construction'),
('p', 'The first configuration’s bundle went through a messy production history. Two hosted models '
      'were tried and abandoned when their quotas ran out mid-extraction, and the bundle that was '
      'finally used came from a local Llama 3.1 8B run end to end. The second configuration was '
      'built cleanly in one session on a single model, and its provenance record proves it. The first '
      'configuration’s history is recorded because it is a caveat on that configuration alone.'),

('h2', '5.10 Known Bundle Defects'),
('p', 'Two defects found by manual reading are extraction problems rather than retrieval problems, '
      'and both were observed in the first configuration’s bundle. One concept file was truncated '
      'mid-sentence, which destroyed the answer to a question at extraction time. In another case '
      'the markdown cross-link syntax leaked into the generated answer text, so the model reproduced '
      'bracket markup it should have read through. Neither defect reappeared in spot checks of the '
      'second bundle, but no systematic re-check was run, and that check is outstanding.'),

('h2', '5.11 Metric Scope'),
('p', 'The grounding rubric measures whether claims are traceable to the context. It does not measure '
      'whether the answer is right. We found grounded-but-wrong answers in both arms during manual '
      'review, so one minus the hallucination rate should never be read as accuracy. A correctness '
      'evaluation would need a separate labelling pass against the gold answers, and that pass was '
      'not run.'),
]

CH6 = [
('h1', 'CHAPTER 6\nFUTURE SCOPE'),

('p', 'The work suggests a fairly clear order of operations, and the ordering is driven by what is '
      'cheap and what is decisive rather than by what is interesting. The first two items are both.'),

('h2', '6.1 Filter Ambiguous Aliases and Rerun'),
('p', 'This is the single highest-value follow-up. Alias-derived links are 31.5% strictly precise '
      'against 77.8% for title-derived links, and they form the bulk of the graph, so the expansion '
      'step is mostly delivering loosely related material. The bundle builder already counts '
      'ambiguous aliases as a diagnostic — 66 in the first bundle, 82 in the second — and does '
      'nothing with the count. Adding a rule that drops generic single-word aliases and any alias '
      'mapping to more than one concept, rebuilding, and rerunning both arms costs one rule and one '
      'rebuild.'),
('p', 'The outcome is informative either way. If hallucination falls, the null was an artefact of '
      'link quality and the hypothesis deserves a proper test. If it does not, the design is wrong on '
      'its own terms and that is worth knowing. A stronger version of the same experiment already '
      'exists in partial form: the title-only bundle, 387 high-precision links against 1,103, was '
      'built but never carried through to a generation run.'),

('h2', '6.2 Enlarge the Question Set'),
('p', 'Power is the binding constraint, and no amount of cleverness in analysis substitutes for '
      'events. Detecting a three-point difference at a base rate of three per cent needs several '
      'hundred paired questions rather than sixty-five. Authoring is slow — each question needs a '
      'verified gold answer, a document list and a cover-one-up check — but it is the one '
      'intervention that unambiguously improves every number in the report.'),
('p', 'Priority inside that expansion should go to verified multi-hop questions, since that is where '
      'the mechanism has its strongest claim and where the current sample is thinnest at eighteen.'),

('h2', '6.3 Concept-Level Gold Annotations'),
('p', 'Replacing the document-to-concept expansion with hand-annotated gold concepts would make '
      'retrieval recall comparable between the arms for the first time. It would remove a known bias '
      'that currently favours the curated arm, and it would let retrieval quality be separated '
      'cleanly from generation quality — which matters because the reasoning misses reported in '
      'Section 3.5.3 suggest generation, not retrieval, is the real bottleneck on multi-hop '
      'questions. The cost is hand-annotating every answerable question.'),

('h2', '6.4 Independent and Multiple Judges'),
('p', 'Given a kappa of 0.518 between two graders, a single judge is not a sufficient instrument. '
      'Running two or three judges from different families and reporting agreement alongside the rate '
      'would put an honest error bar on every hallucination figure. Since the judges disagree most on '
      'exactly the borderline rows that drive the headline, this is not a cosmetic improvement.'),

('h2', '6.5 Remove or Lower the Concept Filter'),
('p', 'Recovering the 108 filtered concepts, including three that directly answer questions, closes a '
      'hole that handicaps the curated arm for reasons unrelated to retrieval. The tradeoff is more '
      'short, low-content units competing for retrieval slots, which is why a sweep over the '
      'threshold is better than simply setting it to zero.'),

('h2', '6.6 Corpora Beyond Kubernetes'),
('p', 'Running the identical protocol over a legal corpus, a clinical corpus and a conversational '
      'one would establish whether the null generalises or is a property of dense technical prose. '
      'The protocol transfers without change; only the corpus and the questions need rebuilding, and '
      'the questions are the expensive half.'),

('h2', '6.7 Combining OKF with Adaptive Retrieval'),
('p', 'The methods reviewed in Chapter 2 vary the retrieval schedule, the model or the output format. '
      'This one varies the unit. They are orthogonal, and a system that retrieves curated concept '
      'units on a FLARE-style confidence trigger, or that lets a Self-RAG-style critic decide which '
      'links to follow, has never been built. Whether the combination beats either part alone is an '
      'open question, and answering it needs the link-precision repair first.'),

('h2', '6.8 Addressing the Reasoning Bottleneck'),
('p', 'Nine abstentions in the second configuration were cases where the answer was present in the '
      'context and the model said the context was insufficient. Both arms suffered from it and almost '
      'all were multi-hop. No retrieval change fixes that. Prompting that explicitly instructs the '
      'model to combine evidence across units, or a decomposition step that answers each half of a '
      'multi-hop question separately before joining, would target it directly — and the target is '
      'larger than the hallucination difference the study set out to measure.'),
]

CH7 = [
('h1', 'CHAPTER 7\nCONCLUSION'),

('p', 'We set out to test whether curating documents into small, self-contained, cross-linked concept '
      'units reduces hallucination in retrieval-augmented generation. The comparison was built to be '
      'tight: the same forty-document corpus, the same questions, the same generator at temperature '
      'zero, the same 1,800-token context budget, with the retrieval substrate as the only thing that '
      'changed. Then the whole thing was repeated with a different generator, a freshly extracted '
      'bundle and an independent judge.'),
('p', 'Curation did not reduce hallucination. In the first configuration the curated arm was worse by '
      'five points with a bootstrap p of 0.31; in the second it was better by one and a half points '
      'with a p of 0.60. The sign flipped, nothing approached significance, and the underlying event '
      'counts are in the single digits. The defensible statement is that no difference was detected '
      'in either configuration, and that the study was not powerful enough to detect one of the size '
      'that would matter.'),
('p', 'Three results survive that null, and they are the contribution.'),
('p', 'The first is the controlled null itself. Because the design isolates one variable, the absence '
      'of an effect is attributable to that variable, and because it reproduced across a change of '
      'generator scale, bundle provenance, judge family and question set, it is unlikely to be an '
      'artefact of any single choice. Work of this kind tends not to get written up, which is why the '
      'published literature gives the impression that every retrieval idea helps.'),
('p', 'The second is efficiency, and it is the one claim the data supports without hedging. The '
      'curated arm answered the same questions on 28.0% less retrieval context in the first '
      'configuration and 10.4% less in the second, while carrying roughly 2.7 times as many '
      'independently addressable units, at unchanged token F1 and exact match. Context length is what '
      'inference cost is mostly made of, so a substrate that delivers more distinct evidence in fewer '
      'tokens is worth having even with no grounding benefit attached.'),
('p', 'The third is mechanistic, and it is what stops the null from being a dead end. Grading a '
      'hundred randomly sampled links by hand showed that title-derived links are 77.8% strictly '
      'precise while alias-derived links, which form the majority of the graph, are 31.5%. Link '
      'expansion — the mechanism the entire design rests on — was therefore operating on a graph that '
      'is wrong most of the time. The hypothesis has not been refuted so much as tested in a degraded '
      'form, and the specific number that has to change is now known.'),
('p', 'What we would tell someone starting this again is short. Build the alias filter first and '
      'measure link precision before measuring anything downstream, because a grounding experiment '
      'run on a 31%-precise graph cannot answer the question it was built to ask. Author several '
      'hundred questions rather than sixty-five, since power is the binding constraint on every '
      'number in this report. Use two judges and report their agreement. And check whether the '
      'generator can actually combine two pieces of evidence before assuming that getting both pieces '
      'in front of it is the hard part — on the evidence of the nine reasoning misses reported here, '
      'it very often is not.'),
]
