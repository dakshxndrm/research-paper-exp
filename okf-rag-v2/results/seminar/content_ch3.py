# -*- coding: utf-8 -*-
CH3 = [
('h1', 'CHAPTER 3\nTOPIC DESCRIPTION AND WORK PERFORMED'),

('p', 'This chapter describes what was actually built and what it produced. It starts with the '
      'corpus and the questions, moves through bundle construction and the two retrieval pipelines, '
      'sets out the evaluation protocol, and ends with the results and their statistical treatment. '
      'The order matters, because several of the design decisions only make sense once you know what '
      'was being controlled for.'),

('h2', '3.1 Dataset Description'),
('h3', '3.1.1 The Corpus'),
('p', 'We used forty pages of Kubernetes documentation, totalling 30,102 words. Kubernetes was '
      'chosen over the usual benchmark corpora for four reasons, and each of them is a property of '
      'the domain rather than a convenience.'),
('p', 'The documentation is dense with named components whose responsibilities are precisely '
      'specified and easy to confuse. A kubelet, a kube-proxy, a controller-manager and a scheduler '
      'all do different things, and a model that has read documentation loosely will attribute one '
      'component’s job to another. That is a hallucination you can detect reliably, which is not '
      'true of vaguer domains where a wrong answer shades into an imprecise one.'),
('p', 'Second, the pages cross-reference each other heavily. A page on garbage collection refers to '
      'owner references, which are defined on a different page; a page on services refers to '
      'endpoint slices, which live elsewhere again. If curated cross-linking is ever going to help, '
      'a corpus with real cross-document structure is where it should show up. Choosing a corpus of '
      'unrelated articles would have stacked the deck against the hypothesis.'),
('p', 'Third, the material is public, stable and citable, so the experiment can be repeated. And '
      'fourth, a technical documentation assistant is one of the deployment scenarios listed in '
      'Chapter 1, so the corpus is representative of an actual use case rather than a toy.'),
('p', 'Document selection was recorded rather than improvised: a selection manifest lists every file '
      'and the reason it was included. Topics span cluster architecture, control-plane and node '
      'components, controllers, garbage collection, services and networking, dual-stack addressing, '
      'endpoint slices, scheduling and eviction, runtime classes, Windows networking, and a group of '
      'workload-API pages. The largest single document is about 11 KB, roughly 4,200 tokens, which '
      'set the input-side sizing for extraction.'),

('h3', '3.1.2 The Question Set'),
('p', 'One hundred questions were written by hand against the corpus, and later rounds added more, '
      'bringing the authored file to 122. Automating this stage was never an option. A question '
      'needs a verified gold answer, a list of the documents that answer it, and a hop type, and '
      'every one of those is a judgement about what the corpus actually says. A model asked to '
      'generate questions from a document generates questions that document answers, which is '
      'precisely the bias that would make the evaluation meaningless.'),
('p', 'Questions come in three kinds. A *single-hop* question is answerable from one document. A '
      '*multi-hop* question needs two, and neither one alone is sufficient. An *unanswerable* '
      'question is written to look answerable from the corpus but is not, and its gold answer is an '
      'abstention. That third category is the one that makes the evaluation honest, because a system '
      'can score well on the first two simply by being verbose. Only the unanswerable set '
      'distinguishes a system that knows what it does not know, and the idea is borrowed from the '
      'unanswerable-question design in SQuAD 2.0 [12].'),
('p', 'The active set for the second configuration contains 65 questions: 37 single-hop, 18 '
      'multi-hop and 10 unanswerable. Getting to that set involved throwing work away, which is '
      'worth describing because it is the least glamorous and most important part of the '
      'methodology.'),
('p', 'Seven questions were dropped after audit. Some had gold answers whose premise did not appear '
      'in the cited document. One asked for a configuration file and the gold answer supplied a '
      'directory. One was a two-part question whose gold answer addressed only one part. One was a '
      'duplicate of another question in the set. Each exclusion is recorded with its reason in a '
      'separate file, and none of them was made after seeing the results.'),
('p', 'The larger problem was with the multi-hop label itself. We re-audited every question labelled '
      'multi-hop using a *cover-one-up test*: read both cited documents, hide one, and check whether '
      'the gold answer is still derivable from the other. A surprising number failed. Of the 55 '
      'questions carrying the multi-hop label in the authored file, only 18 survived that test as '
      'genuinely requiring two documents. The rest cite two sources but are answerable from one, '
      'which means they were never testing multi-hop retrieval at all. Since link expansion is '
      'supposed to help exactly on multi-hop questions, using the unaudited label would have diluted '
      'the one measurement most likely to show an effect. The active set therefore uses only the 18 '
      'verified questions, and we state plainly that in this question set *hop_type is an authoring '
      'label, not a verified property* unless it has been through the cover-one-up test.'),
('p', 'One further property of the question set belongs in the record. Seventeen of the forty '
      'documents are cited as a gold source by at least one question. The other twenty-three are '
      'never the answer to anything; they sit in the index, get embedded, and compete for retrieval '
      'slots. That is a deliberate design decision rather than an oversight, because a retriever '
      'that only ever sees relevant documents is not being tested. But a reader should not assume '
      'the questions cover all forty pages, and so it is stated here.'),

('t', 'Table 3.1 Question set composition',
 [['Set', 'Single', 'Multi', 'Unanswerable', 'Total', 'Notes'],
  ['Authored file', '52', '55', '15', '122', 'All questions written by hand'],
  ['Configuration v1 labelled set', '39', '13', '8', '60', 'Human-labelled in both arms'],
  ['Configuration v2 active set', '37', '18', '10', '65', 'Multi-hop verified by cover-one-up test'],
  ['Excluded after audit', '—', '—', '—', '7', 'Content defects and one duplicate'],
 ]),

('h2', '3.2 Data Pre-processing'),
('h3', '3.2.1 The Chunk Baseline'),
('p', 'Preparing the baseline takes very little work, which is the point of a baseline. Each source '
      'document is cut into windows of 512 tokens with 64 tokens of overlap between consecutive '
      'windows, each window is embedded whole, and the identifier of a window records its source '
      'file and its position, for example ' + 'overview__components.md#chunk0' + '. At query time '
      'the eight nearest windows are fetched and packed into the context in rank order until the '
      '1,800-token budget is spent. In practice about three chunks fit, because a 512-token chunk '
      'plus formatting consumes a large share of the budget.'),
('p', 'No cleaning, no section detection, no heading propagation. This is the naive configuration on '
      'purpose, and it is what a team building a first internal assistant will ship.'),

('h3', '3.2.2 OKF Bundle Construction'),
('p', 'Building the bundle is a two-stage process, and the separation between the stages is the most '
      'important design decision in the project.'),
('p', 'In the first stage, a language model reads each source document in full and returns a JSON '
      'array of concepts. Each concept carries a type drawn from an open vocabulary, a title, a '
      'one-sentence description, a body of running prose, a tag list and a list of aliases — other '
      'names a reader might use for the same idea. The model is capped at twelve concepts per '
      'document and runs at temperature zero with a fixed seed. Extraction is the stage where a '
      'model is genuinely needed, because splitting a page into ideas is a judgement.'),
('p', 'In the second stage no model is involved whatsoever. Cross-linking scans every concept body '
      'for exact string occurrences of the title or of any alias of any other concept in the bundle, '
      'and rewrites each match as a markdown link to that concept’s file path. The match is '
      'literal, the pass is deterministic, and running it twice on the same concept set produces the '
      'same graph. This is not a performance optimisation. A model asked to propose links proposes '
      'plausible ones, and plausible-but-wrong edges in a link graph would silently corrupt every '
      'grounding measurement downstream. Keeping the linker dumb is what makes the link-precision '
      'audit in Section 3.6 meaningful.'),
('p', 'A short concept filter runs at the end, discarding units whose body falls below a minimum '
      'word count. In the first configuration that filter removed 108 of 479 extracted concepts, '
      'about 23%, and at least three of the discarded concepts were the correct answer to a question '
      'in the set. That is a real defect and Chapter 5 treats it as one.'),
('p', 'Table 3.2 gives the properties of the two bundles. They were extracted by different models in '
      'different sessions, and the provenance record confirms their tree hashes differ, so the second '
      'configuration is genuinely a second experiment rather than a re-scoring of the first.'),

('t', 'Table 3.2 Bundle properties in the two configurations',
 [['Property', 'Configuration v1', 'Configuration v2'],
  ['Extraction model', 'Llama 3.1 8B', 'Nemotron-3.5-Lightning-30B-A3B (Q4_K_M)'],
  ['Source documents', '40', '40'],
  ['Concept units', '371', '358'],
  ['Cross-links', '1,103', '1,031'],
  ['Links from alias match', '768', '806'],
  ['Links from title match', '335', '225'],
  ['Mean links per concept', '2.97', '2.88'],
  ['Mean aliases per concept', '2.03', '2.96'],
  ['Ambiguous aliases detected', '66', '82'],
  ['Mean body length (words)', '37.6', '72.8'],
  ['Retrieval top-k', '5', '5'],
  ['Top-k as % of bundle', '1.3%', '1.4%'],
 ]),
('p', 'Two differences in that table deserve comment. The second bundle’s concepts are almost '
      'twice as long, which follows from the stronger extraction model writing fuller bodies rather '
      'than from any change in configuration. And the second bundle leans more heavily on alias '
      'matching, 806 links against 225, which given the precision numbers reported later is not a '
      'favourable shift.'),

('h3', '3.2.3 Anatomy of a Concept Unit'),
('p', 'A concrete example is worth more than a description. The unit below is the one both arms '
      'would want for a question about cluster structure, reproduced from the second bundle.'),
('c', '---\n'
      'type: Definition\n'
      'title: Kubernetes Cluster Architecture Overview\n'
      'description: Describes the fundamental components of a Kubernetes cluster,\n'
      '  including the control plane and worker nodes, and their responsibilities.\n'
      'resource: source://architecture.md\n'
      'tags: [architecture, kubernetes, cluster]\n'
      'aliases:\n'
      '  - cluster architecture\n'
      '  - Kubernetes components\n'
      '  - cluster components\n'
      '---\n\n'
      'A Kubernetes cluster consists of a [control plane](/definition/control_plane_components.md)\n'
      'plus a set of worker machines, called nodes, that run containerized applications. Every\n'
      'cluster needs at least one worker node in order to run Pods. The control plane manages the\n'
      '[worker nodes](/definition/node_components.md) and the Pods in the cluster.'),
('p', 'Three things in that file do work a chunk cannot. The description is what gets embedded, so '
      'the vector encodes the unit’s subject rather than an average over its wording. The '
      'aliases give the linker several surface forms to match on. And the two bracketed links are '
      'the edges the expansion step will follow. Compare it with a 512-token chunk of the same page, '
      'which would begin wherever the previous window ended and would carry none of this.'),

('h2', '3.3 Algorithms and Process Model'),
('f', 'Figure 3.1 Experimental pipeline. Both arms read the same corpus and answer the same '
      'questions under the same context budget; only the retrieval substrate differs.',
      'fig/fig_pipeline.png'),

('h3', '3.3.1 Arm A — Chunk Retrieval'),
('p', 'The baseline follows the standard recipe. The query is embedded with the shared encoder, '
      'cosine similarity is computed against every chunk vector, the top eight are taken, and they '
      'are packed into the prompt in descending similarity order until adding the next one would '
      'exceed 1,800 tokens. The measured mean across the 65 active questions is 3.12 chunks and '
      '1,644.5 context tokens per question.'),

('h3', '3.3.2 Arm B — OKF Retrieval with Link Expansion'),
('p', 'The curated arm runs four steps rather than two.'),
('n', [
 'Seed retrieval. The query is embedded and compared against concept vectors built from the title '
 'and description only. The top five concepts are taken as seeds.',
 'Link expansion. Every outgoing markdown link from every seed is followed one hop. Linked concepts '
 'not already in the seed set are collected as expansion candidates, up to a cap of four.',
 'Budget packing. Seeds are placed first, then expansion candidates, until the same 1,800-token '
 'budget is spent. Seeds are never displaced by expansions, so expansion can only use headroom the '
 'seeds left behind.',
 'Prompt assembly. Each unit enters the context with its type, title and path, so the model can '
 'cite a specific concept rather than a document.',
]),
('p', 'Expansion fired on 64 of the 65 questions in the second configuration; on the remaining one '
      'the seeds alone consumed the budget and expansion was blocked. The mean number of units in '
      'context was 8.34 for this arm against 3.12 for the baseline, at 1,472.8 tokens against '
      '1,644.5. That is the efficiency result in one sentence: nearly three times as many '
      'independently addressable units, in about ten per cent less context.'),

('h3', '3.3.3 Controls Held Constant'),
('p', 'Everything in Table 3.3 is shared between the arms. This is what licenses the causal reading '
      'of any difference — or of the absence of one.'),
('t', 'Table 3.3 Variables held constant across both arms',
 [['Variable', 'Setting'],
  ['Source corpus', '40 Kubernetes documents, 30,102 words'],
  ['Question set', 'Identical 65 questions, answered by both arms'],
  ['Embedding model', 'all-MiniLM-L6-v2, shared'],
  ['Generator model', 'Identical within a configuration'],
  ['Temperature / seed', '0.0 / 42'],
  ['Context token budget', '1,800 tokens'],
  ['System prompt', 'Byte-identical, including the abstention instruction'],
  ['Judge model and rubric', 'Identical within a configuration'],
  ['Varied', 'Retrieval substrate only'],
 ]),

('h3', '3.3.4 The Two Configurations'),
('p', 'Configuration v1 used Llama 3.1 8B throughout — extraction, generation and judging — over a '
      '371-concept bundle, on a 60-question set that had been human-labelled in both arms. It is the '
      'weak-generator, self-judging configuration, and both of those properties are weaknesses.'),
('p', 'Configuration v2 was built to remove them. A stronger generator, a freshly extracted bundle, '
      'an independent judge from a different family, and an audited question set. Retrieval settings, '
      'embedding model, seed and context budget were carried over unchanged and verified by a '
      'flattened comparison of the two configuration files, so the only intended differences are the '
      'ones just listed.'),
('p', 'An important negative result from the development of v2 belongs here. A completed run was '
      'discarded because a provenance check revealed that the bundle it had generated against was '
      'byte-identical to the first configuration’s bundle rather than a fresh extraction. The '
      'chunk arm of that run was unaffected mechanically, but pairing it against an OKF arm from a '
      'different session would have confounded the paired comparison, so both arms were regenerated. '
      'That is the kind of error that a provenance hash catches and a casual workflow does not.'),

('h2', '3.4 Evaluation Protocol'),
('h3', '3.4.1 Metrics'),
('p', 'Five quantities are recorded for every generated answer.'),
('b', [
 '*Hallucination* is a binary flag derived from a grounding label. An answer is labelled supported, '
 'unsupported, contradicted or abstained; the first and last count as clean, the middle two count '
 'as a hallucination. Note what this measures: whether every claim is traceable to the context, not '
 'whether the answer is correct.',
 '*Exact match* and *token F1* compare the generated answer against the hand-written gold answer. '
 'Both are weak here, because the generator writes a paragraph where the gold answer is one '
 'sentence, and F1 punishes that heavily.',
 '*Retrieval recall* asks whether the retrieved units come from the documents the question was '
 'authored against.',
 '*Citation validity* checks that every source the answer cites was present in its own context.',
 '*Context tokens* records how much retrieval text the generator was given.',
]),
('p', 'A methodological point that must not be skipped: *supported does not mean correct*. The '
      'grounding rubric asks only whether the context backs the claims. An answer can be perfectly '
      'grounded and still be the wrong answer to the question, and in manual review we found '
      'examples of exactly that in both arms. Therefore one minus the hallucination rate is not an '
      'accuracy figure, and this report never presents it as one.'),

('h3', '3.4.2 Labelling'),
('p', 'Every row is graded twice. The LLM judge reads the question, the retrieved context and the '
      'answer, and returns one of the four labels under a fixed rubric. It grades all rows and is '
      'treated as a screening pass. Then every row is read by a human against the same rubric and '
      'the same reconstructed context, and the human label is what gets reported.'),
('p', 'For the second configuration all 130 rows — 65 questions in each of two arms — were '
      'hand-labelled, so human coverage is complete. In the first configuration it was 60 of 100 '
      'questions per arm. Contexts were rebuilt from the stored retrieval identifiers and verified '
      'to contain every unit the run recorded, so nobody was grading against a context the model '
      'never saw.'),
('p', 'One measurement from the development of this protocol is worth reporting even though it is '
      'not about OKF-RAG. On a discarded run, two capable judges from different families graded the '
      'identical 120 rows against the identical rubric and identical contexts. They agreed on 90% of '
      'rows, but Cohen’s kappa was only 0.518 — moderate agreement, on a binary-ish task, '
      'between two competent graders. That number is a warning about the whole literature of '
      'LLM-judged hallucination rates: a single judge carries judge-dependent variance large enough '
      'to swamp the effect sizes people typically report. It is also why this report leads with '
      'human labels.'),

('h3', '3.4.3 Statistical Treatment'),
('p', 'Because both arms answer identical questions, the comparison is paired and the pairing is '
      'used. A paired bootstrap resamples questions with replacement, recomputes the difference in '
      'arm means on each resample, and reports the two-sided proportion of resamples on the wrong '
      'side of zero [4]. McNemar’s exact test [11] is reported alongside for the binary '
      'hallucination flag, because it uses only the questions where the two arms disagree and is '
      'therefore honest about how thin the evidence is when the counts are small.'),

('h2', '3.5 Results'),
('h3', '3.5.1 Primary Outcome — Hallucination'),
('p', 'Table 3.4 gives the headline. Both rows are human labels on paired question sets.'),
('t', 'Table 3.4 Hallucination rate, human labels, both configurations',
 [['Configuration', 'n', 'Chunk', 'OKF', 'Delta', 'Bootstrap p', 'McNemar (discordant, exact p)'],
  ['v1 — Llama 3.1 8B', '60', '0.0333', '0.0833', '+0.0500 (OKF worse)', '0.3056', '5/2, p = 0.4531'],
  ['v2 — Nemotron 30B', '65', '0.0308', '0.0154', '−0.0154 (OKF better)', '0.6042', '1/2, p = 1.0000'],
 ]),
('f', 'Figure 3.2 Hallucination rate by arm in both configurations. The sign of the difference '
      'reverses between configurations and neither difference approaches significance.',
      'fig/fig_hallucination.png'),
('p', 'Read the table carefully, because the temptation is to read the second row as a win. It is '
      'not one. In the first configuration the curated arm produced five hallucinations against the '
      'baseline’s two. In the second it produced one against two. The point estimate changed '
      'sign, which is what an estimate does when it is sampling noise around zero. Bootstrap '
      'p-values of 0.31 and 0.60 are nowhere near any conventional threshold, and McNemar on the '
      'second configuration sees three disagreeing questions in total, which is not evidence of '
      'anything.'),
('p', 'The honest statement is therefore: *no detectable difference in hallucination in either '
      'configuration*. Not a reduction, and not an increase either. That conclusion survives a '
      'change of generator across roughly a factor of four in parameter count, a change of bundle '
      'provenance, a change of judge model family, and a change of question set. A finding that '
      'robust to configuration is worth reporting precisely because it is unlikely to be an artefact '
      'of any one of those choices.'),

('h3', '3.5.2 Secondary Outcome — Context Efficiency'),
('p', 'The efficiency result is the one place where the two configurations agree in direction and '
      'the effect is not a handful of events.'),
('t', 'Table 3.5 Retrieval context cost and answer quality (human-labelled sets)',
 [['Measure', 'v1 chunk', 'v1 OKF', 'v2 chunk', 'v2 OKF'],
  ['Context tokens per question', '1,615.4', '1,162.6', '1,644.5', '1,472.8'],
  ['Reduction', '—', '−28.0%', '—', '−10.4%'],
  ['Retrieval units in context', '3.08', '8.83', '3.12', '8.34'],
  ['Token F1', '0.3151', '0.2869', '0.2312', '0.2418'],
  ['Exact match', '0.0000', '0.0167', '0.0000', '0.0000'],
  ['Retrieval recall', '0.8558', '0.7981', '0.8636', '0.9091'],
  ['Citation validity', '1.000', '0.914', '1.000', '1.000'],
  ['Abstention rate', '0.150', '0.167', '0.277', '0.262'],
 ]),
('f', 'Figure 3.3 Mean retrieval context per question. The curated arm answers the same questions '
      'on fewer tokens in both configurations.',
      'fig/fig_tokens.png'),
('p', 'The curated arm spent 28.0% fewer retrieval tokens in the first configuration and 10.4% fewer '
      'in the second, while carrying almost three times as many independently retrievable units into '
      'the context. Answer quality did not pay for it: F1 moved by less than three points in either '
      'direction and exact match is effectively zero for both arms, since neither system produces '
      'one-sentence answers matching the gold string.'),
('p', 'Why the reduction shrank from 28% to 10% is worth explaining rather than glossing over. The '
      'second bundle’s concept bodies are nearly twice as long, 72.8 words against 37.6, so each '
      'retrieved unit costs more. The efficiency gain is real in both runs, but its size depends on '
      'how terse the extraction model writes, which is a property of the extractor and not of the '
      'OKF format itself. Anyone reproducing this should expect the number to move.'),
('p', 'One correction to an intuition we held mid-project. Because the curated arm reads fewer '
      'tokens, it seemed obvious that it would also generate faster. It does not. Mean generation '
      'time was 21.2 seconds for the baseline and 22.9 seconds for the curated arm, so the curated '
      'arm is marginally slower despite the smaller context. The saving is in tokens read, which is '
      'what an API bill measures, and not in wall-clock latency.'),

('h3', '3.5.3 Behaviour by Question Type'),
('p', 'Splitting the second configuration by hop type shows where the interesting behaviour hides.'),
('t', 'Table 3.6 Configuration v2 behaviour by question type (human labels)',
 [['Question type', 'n', 'Chunk halluc.', 'OKF halluc.', 'Chunk abstain', 'OKF abstain',
   'Chunk recall', 'OKF recall'],
  ['Single-hop', '37', '0.027', '0.000', '0.027', '0.054', '0.946', '0.973'],
  ['Multi-hop (verified)', '18', '0.056', '0.056', '0.389', '0.278', '0.694', '0.778'],
  ['Unanswerable', '10', '0.000', '0.000', '1.000', '1.000', '—', '—'],
 ]),
('f', 'Figure 3.4 Hallucination and abstention by question type, configuration v2.',
      'fig/fig_hop.png'),
('p', 'Start with the good news, which both arms share. On all ten unanswerable questions, both '
      'systems abstained. Not nine out of ten — ten. Whatever else is true, the abstention '
      'instruction in the shared system prompt works, and both retrieval substrates support it '
      'equally. Any claim that curation improves calibration has to survive that ceiling, and there '
      'is no headroom left for it to show in.'),
('p', 'Multi-hop is where the design was supposed to pay off, and the numbers are equivocal. '
      'Retrieval recall is better for the curated arm, 0.778 against 0.694, and it abstains less '
      'often, 0.278 against 0.389, which together say link expansion is surfacing more of the right '
      'material. But hallucination is identical at 0.056, one event each. Better retrieval did not '
      'translate into better grounding.'),
('p', 'Manual reading of those rows explains why, and the explanation is uncomfortable for the '
      'hypothesis. Nine abstentions across the two arms were *reasoning misses*: the answer was '
      'present in the context the model was given, and the model still replied that the context was '
      'insufficient. Almost all of them are multi-hop. Both arms suffer from it. The bottleneck on '
      'these questions is not that the evidence failed to arrive; it is that the generator did not '
      'join two pieces of evidence that were sitting in front of it. No change to the retrieval '
      'substrate fixes that.'),
('p', 'An earlier informal observation, that the curated arm abstains more honestly on retrieval '
      'misses, does not hold up in the final data. On answerable questions the baseline abstained '
      'eight times and the curated arm seven — effectively identical.'),

('h3', '3.5.4 The Individual Hallucination Events'),
('p', 'With three hallucination events across 130 rows, naming them is more informative than any '
      'aggregate. All three were borderline calls, and the labelling notes record the reasoning.'),
('b', [
 'Q036, baseline arm, *unsupported*. The context says that Pod network namespace setup is handled '
 'by system software implementing the Container Runtime Interface. The answer claims every runtime '
 'must provide the CRI, which the context does not say. The curated arm answered the same question '
 'cleanly.',
 'Q064, baseline arm, *unsupported*. The answer is grounded throughout except for a closing '
 'generalisation about continuous operation that the context does not support. Kept as a '
 'hallucination under a strict reading of the rule that any unsupported claim taints the row.',
 'Q070, curated arm, *contradicted*. The context assigns Service routing to the service-proxy '
 'implementation; the answer attributes it to the kubelet and the cloud-controller-manager. '
 'Unsupported would also have been defensible, but the context names an explicit alternative, so '
 'contradicted was used.',
]),
('p', 'Two observations follow. Every event is a borderline call, which means the measured '
      'difference between arms is at the mercy of labelling policy — and the judge-agreement kappa '
      'of 0.518 reported earlier says exactly the same thing from a different direction. And with '
      'three events total, a single relabelling decision would flip the sign of the headline. That '
      'is a statement about statistical power, and it is the honest frame for the whole comparison.'),

('h2', '3.6 Link Precision — Why the Effect Did Not Appear'),
('p', 'A null result is more useful when it comes with a mechanism, so we audited the link graph '
      'directly instead of speculating. A random sample of 100 links was drawn from the '
      '1,103-link bundle with a fixed seed and every one was graded by hand into three buckets: '
      '*correct* if the link connects genuinely related concepts, *borderline* if the connection is '
      'loose but not wrong, and *spurious* if the concepts are unrelated. Strict precision counts '
      'only correct; lenient precision counts correct plus borderline.'),
('t', 'Table 3.7 Link precision, 100-link random sample (seed 42)',
 [['Match type', 'Graded', 'Correct', 'Borderline', 'Spurious', 'Strict', 'Lenient'],
  ['All links', '100', '44', '35', '21', '0.440', '0.790'],
  ['Title match', '27', '21', '5', '1', '0.778', '0.963'],
  ['Alias match', '73', '23', '30', '20', '0.315', '0.726'],
 ]),
('f', 'Figure 3.5 Link precision by match type. Alias matching produces most of the graph and most '
      'of the errors.',
      'fig/fig_linkprec.png'),
('p', 'This is the most informative table in the report. Links created by matching a concept title '
      'are good: 77.8% strictly correct, 96.3% at least defensible, one spurious link in '
      'twenty-seven. Links created by matching an alias are not: 31.5% strictly correct, with one in '
      'five outright spurious.'),
('p', 'The damage comes from the mix. Alias matching produced 768 of the 1,103 links in the first '
      'bundle and 806 of 1,031 in the second, so the majority of the graph — and therefore the '
      'majority of what link expansion pulls into the context — rides on the low-precision rule. An '
      'expansion step that is right about a third of the time is not adding grounding. It is adding '
      'plausible-looking neighbouring text, which is a reasonable description of what causes '
      'hallucination in the first place.'),
('p', 'Why alias matching fails is not mysterious. Aliases are short, generic and frequently '
      'ambiguous: a single common word appearing in an unrelated concept body creates an edge '
      'between two concepts that have nothing to do with each other. The bundle builder already '
      'counts ambiguous aliases as a diagnostic — 66 in the first bundle, 82 in the second — but it '
      'does not act on the count. Nothing filters them out.'),
('p', 'A supporting comparison exists. A title-only bundle was built from the identical concept set '
      'with alias matching switched off. It has 387 links against 1,103, so link density falls from '
      '2.97 per concept to 1.04, but by the precision figures above almost every surviving link is '
      'sound. That bundle was never carried through to a full generation run, and doing so is the '
      'single highest-value follow-up this project has.'),
('p', 'Putting the pieces together gives a defensible account of the null. The mechanism the whole '
      'design rests on is link expansion. Link expansion is driven by a graph that is majority '
      'alias-derived. Alias links are correct less than a third of the time. So the mechanism was '
      'never operating at a quality where a grounding benefit could reasonably be expected. The '
      'hypothesis has not been refuted; it has been tested at a link precision too low to give it a '
      'fair hearing, and we now know the number that has to change.'),

('h2', '3.7 Judge Labels as a Screening Check'),
('p', 'Judge labels are reported here for completeness, with the standing caveat that they are a '
      'screening instrument and not the reported metric. In the second configuration the independent '
      'Qwen judge graded all 130 rows with no parsing failures and put both arms at 0.0154 '
      'hallucination — two events, dead even. In the first configuration, where the judge was the '
      'same model that wrote the answers, it reported 0.03 for the baseline and 0.05 for the curated '
      'arm across 600 rows.'),
('p', 'Direction of the judge estimate agrees with the human estimate in both configurations, which '
      'is mild reassurance that the human labelling is not idiosyncratic. Magnitudes differ, and '
      'given the kappa of 0.518 measured between two independent judges, nobody should read too much '
      'into either.'),

('h2', '3.8 Summary of Findings'),
('n', [
 'Curated OKF retrieval produced no statistically detectable change in hallucination rate in either '
 'configuration. Bootstrap p was 0.31 and 0.60; McNemar was 0.45 and 1.00.',
 'The sign of the point estimate reversed between configurations, which is behaviour consistent with '
 'noise around zero rather than with a small real effect.',
 'The curated arm answered the same questions on 28.0% and 10.4% less retrieval context, at '
 'unchanged answer quality, while carrying roughly 2.7 times as many addressable units.',
 'Both arms abstained on all ten unanswerable questions, so calibration is at ceiling and cannot '
 'distinguish the substrates.',
 'The curated arm retrieved better on verified multi-hop questions, recall 0.778 against 0.694, but '
 'did not hallucinate less on them; nine abstentions were reasoning misses on evidence that was '
 'already in context.',
 'Direct audit shows alias-derived links, which form the majority of the graph, are only 31.5% '
 'strictly precise against 77.8% for title-derived links. That gives a concrete mechanistic account '
 'of why the expansion step did not deliver a grounding benefit.',
]),
]
