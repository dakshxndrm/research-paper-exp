# -*- coding: utf-8 -*-
CH1 = [
('h1', 'CHAPTER 1\nINTRODUCTION'),

('p', 'Large language models answer questions fluently, and that fluency is exactly the problem. '
      'A model trained only on its own parameters will happily produce a version number, an API '
      'field, or a legal clause that never existed, and it will do so in the same confident tone it '
      'uses for facts it actually knows. The literature calls this *hallucination*, and the survey '
      'by Ji and colleagues [6] treats it as a property of the generation process rather than a bug '
      'that a bigger model eventually outgrows. Retrieval-Augmented Generation, introduced by Lewis '
      'and co-authors in 2020 [10], attacks the problem from a different direction: instead of asking '
      'the model to recall, you hand it the relevant source text at inference time and ask it to '
      'read. The model still writes the answer, but the evidence sits in the prompt where it can be '
      'checked.'),
('p', 'RAG has become the default architecture for grounded question answering, and it works well '
      'enough that most production systems use some variant of it. What has received less attention '
      'is the shape of the retrieved material. Almost every deployed system slices its documents '
      'into fixed-size windows of a few hundred tokens, embeds each window, and returns the nearest '
      'neighbours of the query. Nobody chose that design because it was good; it was chosen because '
      'it is trivial to implement and it never fails outright. A 512-token window drawn from the '
      'middle of a reference page will often begin mid-sentence, carry no indication of which '
      'section it came from, and mix two unrelated topics that happened to be adjacent on the page.'),
('p', 'The work reported here asks a narrow question about that design choice. If the retrieved '
      'material were curated instead of cut, would the generator hallucinate less? To answer it we '
      'built an *Open Knowledge Format* (OKF) bundle: a set of small, self-contained concept units, '
      'each carrying a title, a one-line description, a short body, a list of aliases, and explicit '
      'markdown links to related units. Then we ran a controlled comparison against an ordinary '
      'chunk-based pipeline on the same corpus, with the same generator, the same context budget, '
      'and the same questions. Only the retrieval substrate differed.'),
('p', 'This report presents the result honestly, which means reporting that the hypothesis did not '
      'hold. Across two independent configurations, separated by a generation of model capability '
      'and built on two separately extracted bundles, curation produced no statistically detectable '
      'change in hallucination rate. It did produce a consistent reduction in retrieval context '
      'cost, and a link-precision audit explains mechanically why the grounding benefit failed to '
      'appear. Those three findings, taken together, are the contribution.'),

('h2', '1.1 Area of Work and Its Applications'),
('p', 'Grounded question answering over a private document collection is now a standard engineering '
      'requirement rather than a research curiosity. Any organisation that holds more text than a '
      'person can read wants a system that will answer questions from that text and, crucially, will '
      'not invent an answer when the text is silent. The areas below are the ones where a measurable '
      'reduction in hallucination changes whether the system can be deployed at all.'),
('n', [
 'Clinical and medical question answering. A model that summarises a drug interaction from a '
 'formulary must not add a contraindication that is not in the source. Regulatory review of such '
 'systems turns almost entirely on traceability of each generated statement back to a document.',
 'Legal research and contract review. Case citations are the classic hallucination failure: a '
 'fabricated case name is syntactically indistinguishable from a real one, and courts have already '
 'sanctioned filings containing them. Retrieval with verifiable citation is the only workable fix.',
 'Enterprise customer support. Support assistants answer from product manuals and past tickets. An '
 'invented refund policy or an invented configuration flag creates a support cost larger than the '
 'one the assistant was deployed to reduce.',
 'Technical documentation assistants. This is the domain used in the present study. Developers ask '
 'precise questions about APIs, default values and component responsibilities, and a wrong default '
 'value is worse than no answer, because it will be pasted straight into a configuration file.',
 'Programming and code assistance. Retrieval over a repository lets an assistant answer questions '
 'about internal functions it was never trained on. Hallucinated function signatures fail loudly at '
 'compile time, but hallucinated behavioural claims about a function fail silently in production.',
 'Education and tutoring systems. A tutor grounded in a prescribed syllabus can be held to that '
 'syllabus. Without grounding, the system will confidently teach material that contradicts the '
 'textbook the student is being examined on.',
 'Scientific literature review. Retrieval over paper collections supports evidence synthesis, but '
 'only if every claim in the synthesis is attributable. A fabricated effect size in a summary can '
 'propagate into a real meta-analysis.',
 'Financial analysis and regulatory reporting. Figures drawn from filings must match the filings. '
 'Here hallucination is not merely embarrassing; misstating a reported number carries legal weight.',
 'Government and public-policy question answering. Citizen-facing assistants answering questions '
 'about eligibility rules, tax provisions or statutory deadlines have to be exactly right, and have '
 'to be able to show which paragraph of which notification they used.',
 'Internal knowledge search in large engineering organisations. Runbooks, design documents and '
 'incident postmortems accumulate faster than anyone reads them. Grounded search over that pile is '
 'one of the highest-value applications of RAG, and also one where the source text is messiest.',
 'Multilingual and low-resource question answering. When a language is thinly represented in '
 'pre-training data, parametric recall is weak and retrieval carries almost the entire factual '
 'load, which raises the stakes on retrieval quality.',
 'Conversational agents over evolving knowledge. Product catalogues, pricing and API surfaces change '
 'weekly. Retrieval lets a frozen model stay current, provided the retrieved snippet is actually the '
 'right one.',
]),
('p', 'Two things are common to all twelve. First, the cost of a confident wrong answer is much '
      'higher than the cost of an honest refusal. Second, the system is only as good as the material '
      'that reaches the generator, which is why the retrieval substrate deserves the scrutiny this '
      'study gives it.'),

('h2', '1.2 Historical Development'),
('p', 'It is worth tracing how the field arrived at the current design, because the chunk-and-embed '
      'pipeline that this study treats as a baseline was never really designed. It accumulated.'),
('h3', '1.2.1 Purely Parametric Models'),
('p', 'Early transformer language models stored everything they knew in their weights. Scaling those '
      'weights improved recall of common facts, but it also made the failure mode worse: a larger '
      'model produces a more plausible fabrication. Updating a fact meant retraining, and there was '
      'no way to ask the model where a claim had come from. Neither property is acceptable in the '
      'application areas listed above.'),
('h3', '1.2.2 Dense Retrieval and the Original RAG'),
('p', 'Dense Passage Retrieval [8] showed that a learned dual-encoder could beat keyword search on '
      'open-domain question answering by embedding passages and queries into a shared vector space. '
      'Lewis and colleagues then combined a dense retriever with a sequence-to-sequence generator and '
      'trained the two together [10], and the resulting architecture is what the field now calls RAG. '
      'A companion result from Shuster and co-authors measured the effect directly and found that '
      'retrieval augmentation cuts hallucination in dialogue [14]. That pairing, a retriever feeding '
      'a generator, is the ancestor of essentially every system discussed in this report.'),
('h3', '1.2.3 Adaptive and Self-Critical Retrieval'),
('p', 'The next wave of work noticed that retrieving once, at the start, is often the wrong schedule. '
      'FLARE [7] watches the generator as it writes and triggers a fresh retrieval whenever the next '
      'sentence is predicted with low confidence, using the tentative sentence itself as the query. '
      'Self-RAG [1] goes further and trains the model to emit reflection tokens that decide whether '
      'to retrieve at all and whether each generated segment is actually supported by what was '
      'retrieved. Both lines improve grounding, and both do it by changing *when* and *whether* to '
      'retrieve rather than changing what the retrieved unit looks like.'),
('h3', '1.2.4 Structure in the Retrieval Substrate'),
('p', 'A smaller body of work does touch the substrate. Bechard and Ayala [2] constrain the model to '
      'emit structured output and show that retrieval plus schema constraints reduces hallucination '
      'in a workflow-generation task, which is evidence that structure imposed on the *output* helps. '
      'GraphRAG [3] builds an entity graph over the corpus and summarises communities within it, '
      'which is structure imposed on the *index*. Tuning-based approaches such as ReRAG [15] adjust '
      'the retriever or the reranker to the downstream task. What none of these do is restructure the '
      'atomic retrieved unit itself into a curated, cross-linked concept record, which is the gap '
      'OKF-RAG was built to probe.'),
('p', 'The survey by Gao and co-authors [5] organises this history into naive, advanced and modular '
      'RAG. By that taxonomy the baseline used here is deliberately naive, because a naive baseline '
      'is what the majority of deployed systems actually run, and beating a strawman would prove '
      'nothing.'),

('h2', '1.3 Description of the Topic'),
('p', 'An OKF bundle is a directory of small markdown files. Each file is one concept. The front '
      'matter carries a type, a title, a one-sentence description, the source document it was drawn '
      'from, a handful of tags and a list of aliases; the body is a short paragraph, averaging 72.8 '
      'words in the bundle used for the second configuration. Inside the body, any mention of another '
      'concept in the bundle is rewritten as a markdown link to that concept file. Nothing in the '
      'file assumes surrounding context, which is precisely the property a chunk lacks.'),
('p', 'Retrieval over such a bundle works differently from retrieval over chunks in two ways. The '
      'embedding is computed over the title and description rather than the whole body, so the vector '
      'describes what the unit is about instead of averaging over incidental wording. And once the '
      'top-ranked units are selected, the system follows their outgoing links one hop and pulls in '
      'the linked concepts as well, up to a cap, so that a question whose answer spans two ideas can '
      'be served even when only one of them ranked highly. We call that step *link expansion*, and it '
      'is the mechanism the whole design rests on.'),
('p', 'Building the bundle is the expensive part. Concept boundaries and alias lists are produced by '
      'a language model reading each source document, because deciding where one idea ends and the '
      'next begins is a judgement call. Cross-linking, by contrast, is done by exact string matching '
      'against titles and aliases with no model in the loop at all. That split is deliberate. A model '
      'asked to invent links will invent plausible ones, and a link graph containing invented edges '
      'would make any grounding measurement meaningless.'),

('h2', '1.4 Significance of the Work'),
('p', 'Most published comparisons of retrieval strategies change several things at once, which makes '
      'it hard to say what caused an improvement. The design here is unusually tight. Both arms read '
      'the same forty source documents, answer the same questions, use the same generator at '
      'temperature zero, and are held to the same 1,800-token retrieval budget. The only difference '
      'is the shape of the retrieved unit. If a difference in hallucination appears, there is nowhere '
      'else for it to have come from; if none appears, that too is informative.'),
('p', 'None appeared. In the first configuration the curated arm looked slightly worse, in the second '
      'it looked slightly better, and neither gap came close to significance. Reporting that is the '
      'point. A field that only publishes the configurations that worked accumulates a literature in '
      'which every idea helps, which is not a useful literature. The link-precision audit reported in '
      'Chapter 3 goes one step further and identifies which part of the design is responsible: the '
      'alias-matching rule that generates most of the link graph is correct only 31.5% of the time '
      'under strict grading, so the expansion step is mostly pulling in loosely related material. '
      'That is a concrete, testable explanation, and it points at a specific repair rather than at a '
      'vague call for more work.'),
('p', 'The efficiency result stands on its own. Answering the same questions at the same measured '
      'answer quality while reading 10% to 28% fewer retrieval tokens is a real operational gain, '
      'because context length is what an inference bill is mostly made of.'),

('h2', '1.5 Objectives'),
('n', [
 'Construct an Open Knowledge Format bundle from a fixed technical corpus, using a language model '
 'for concept extraction and a purely deterministic procedure for cross-linking.',
 'Implement two retrieval pipelines over that corpus: a conventional fixed-size chunk baseline and '
 'an OKF-based pipeline with one-hop link expansion.',
 'Hold every variable other than the retrieval substrate constant across the two arms, including '
 'generator, temperature, seed, context budget and question set.',
 'Measure hallucination with an LLM judge for screening and with human labels as the reported '
 'metric, and test the paired difference using a bootstrap and McNemar’s exact test.',
 'Repeat the entire comparison in a second configuration with a different, stronger generator, a '
 'freshly extracted bundle and an independent judge from a different model family.',
 'Audit the quality of the cross-link graph directly, so that any observed effect, or absence of '
 'one, can be attributed to a mechanism rather than guessed at.',
 'Report the outcome as measured, including the null result, and identify the specific component '
 'that would have to be repaired for the hypothesis to get a fair second hearing.',
]),

('h2', '1.6 Organisation of the Report'),
('p', 'Chapter 2 covers the implementation stack and reviews five closely related pieces of work. '
      'Chapter 3 is the substance of the seminar: the corpus, the bundle construction procedure, both '
      'retrieval pipelines, the evaluation protocol, and the results with their statistical treatment. '
      'Chapter 4 shows the artefacts the pipeline produces and marks where screenshots belong. '
      'Chapter 5 states the limitations plainly, Chapter 6 lists what should be tried next, and '
      'Chapter 7 concludes.'),
]
