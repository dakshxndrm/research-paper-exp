# -*- coding: utf-8 -*-
CH2 = [
('h1', 'CHAPTER 2\nTECHNOLOGY SPECIFICATION AND\nLITERATURE REVIEW'),

('p', 'Everything described in this report is software. There is no hardware component, no sensor, '
      'no FPGA and no custom silicon; the only physical constraint that mattered was the amount of '
      'video memory available on the GPUs used for inference, and that constraint shaped several '
      'design decisions described below. This chapter records the stack, explains why each piece was '
      'chosen, and then reviews the five papers that sit closest to this work.'),

('h2', '2.1 Implementation Language'),
('p', 'The whole project is written in Python 3.11. That choice was not really a choice. Every '
      'library in the modern retrieval and language-model ecosystem publishes a Python interface '
      'first, and often only a Python interface: sentence-transformers for embeddings, the OpenAI-'
      'compatible client protocol that local inference servers speak, pandas for the result tables, '
      'matplotlib for the figures, and the statistical routines used for the bootstrap. Writing the '
      'pipeline in anything else would have meant reimplementing all of that at the cost of the time '
      'the experiment itself needed.'),
('p', 'Two properties of Python mattered more than the library ecosystem, though. The first is that '
      'the code reads like the method description, so a reviewer can check that the experiment '
      'matches the paper by reading the source. The second is that the standard library was enough '
      'for almost all of the glue. Checkpointing, configuration loading, hashing and the CSV '
      'round-trips all use modules that ship with the interpreter, which keeps the dependency list '
      'short and the whole thing reproducible on a fresh machine.'),
('p', 'The source tree is small on purpose. Nine modules under ' + 'src/' + ' carry the entire '
      'system: configuration and checkpointing, the language-model client, the chunk pipeline, the '
      'OKF pipeline, bundle construction, the experiment driver, scoring, analysis and a small set '
      'of shared helpers. Configuration lives in YAML files rather than in command-line flags, with '
      'an *extends* mechanism so that a variant configuration states only what it changes. That '
      'detail turned out to matter: it is how we could prove that the second configuration reused '
      'the first configuration’s retrieval settings byte for byte.'),

('h2', '2.2 Tools and Techniques Used'),
('h3', '2.2.1 Embedding and Vector Search'),
('p', 'Both arms embed their retrieval units with *all-MiniLM-L6-v2*, a 384-dimensional '
      'sentence-transformer from the Sentence-BERT family [13]. It is small, it runs on CPU in '
      'seconds for a corpus of this size, and, most importantly for a controlled comparison, it is '
      'identical across the two arms. Similarity is plain cosine over normalised vectors, computed '
      'exactly rather than approximately. With 358 concepts on one side and a few hundred chunks on '
      'the other, an approximate index such as FAISS or HNSW would have added a tunable component '
      'with no measurable speed benefit, and a tunable component is the last thing a controlled '
      'comparison needs.'),
('h3', '2.2.2 Local Inference with Ollama'),
('p', 'All generation and judging ran through Ollama, which serves quantised models over an '
      'OpenAI-compatible HTTP endpoint. Two reasons drove that decision. Earlier attempts to use '
      'hosted APIs kept hitting quota walls in the middle of runs, and a run that dies two thirds of '
      'the way through because a provider cut the account off is a run that has to be repeated. '
      'Running locally also makes the experiment reproducible by anyone with the same weights, '
      'because nothing depends on a provider’s current model routing.'),
('p', 'Because Ollama speaks the OpenAI chat protocol, the client module in this project needed no '
      'changes at all when generation moved from a hosted API to local weights. The same client code '
      'talks to both.'),
('h3', '2.2.3 Generator and Judge Models'),
('p', 'The first configuration used *Llama 3.1 8B* for both bundle extraction and answer generation, '
      'and used the same model again as the LLM judge. That last point is a genuine weakness, and it '
      'is recorded as such: a model scoring its own output has an obvious self-preference bias, which '
      'is why human labels rather than judge labels are reported as the headline in both '
      'configurations.'),
('p', 'The second configuration was built specifically to remove that weakness and to raise the '
      'capability ceiling. Extraction and generation moved to *NVIDIA Nemotron-3.5-Lightning-30B-A3B*, '
      'a hybrid Mamba-2 and mixture-of-experts model, served at Q4_K_M quantisation from a GGUF '
      'build. Judging moved to *Qwen 2.5 7B Instruct*, which comes from an entirely different model '
      'family and had no part in producing the answers it grades. Those two changes together retire '
      'the self-judging caveat for the second configuration.'),
('p', 'Nemotron is a reasoning-tuned model, and that caused a concrete engineering problem worth '
      'recording. During bundle extraction the model would consume its entire token budget on hidden '
      'reasoning and return an empty completion, so extraction runs with the reasoning effort set to '
      'none. Answer generation is the opposite case. Disabling reasoning there collapsed the model '
      'into a keyword extractor that emitted one-word answers, ignored the required citation format, '
      'and stopped abstaining on unanswerable questions entirely, so that run was discarded and '
      'generation kept reasoning enabled with the output cap raised to 8,000 tokens. One answer in '
      'the final run finished at 7,135 tokens, which shows the raised cap was not academic.'),
('h3', '2.2.4 Compute Environment'),
('p', 'The second configuration ran on a Kaggle notebook with two NVIDIA T4 GPUs, roughly 30 GiB of '
      'combined video memory. The 24.5 GB Q4_K_M quantisation of Nemotron was the only build of that '
      'model that fits, and the fit is tight enough that the notebook checks loaded memory before '
      'starting a long run. Model choice here was constrained by hardware and we say so: a much '
      'stronger judge was considered and rejected because no quantisation of it fits in 32 GiB.'),
('p', 'Only one model is resident at a time, and the server context window is capped, because '
      'holding the generator and the judge in memory simultaneously exhausts the cards. Generation '
      'and scoring are checkpointed on a composite key of arm and question identifier, so a crash '
      'or a timeout costs only the row in flight. That checkpointing earned its keep more than once '
      'during development.'),
('h3', '2.2.5 Evaluation Tooling'),
('p', 'Scoring combines four automatic metrics with two layers of labelling. Exact match and token '
      'F1 compare the generated answer against a hand-written gold answer. Retrieval recall asks '
      'whether the units the retriever returned came from the documents the question was authored '
      'against. Citation validity checks that every source the model cited is one that was actually '
      'in its context. On top of those sit the LLM judge, which grades grounding on every row and '
      'serves as a screening pass, and the human labels, which are what the report treats as ground '
      'truth.'),
('p', 'Significance testing uses a paired bootstrap over question-level differences [4] and '
      'McNemar’s exact test [11] on the discordant pairs. The bootstrap is appropriate because '
      'the two arms answer identical questions, so the pairing carries real information; McNemar is '
      'reported alongside it because with hallucination counts in the single digits the bootstrap '
      'alone can look more precise than the data warrants.'),
('h3', '2.2.6 Version Control and Reproducibility'),
('p', 'Configuration, corpus, questions and code are versioned together, and every run writes a '
      'metadata file recording the exact flattened configuration it used. The bundle carries a '
      'provenance record with a SHA-256 hash computed over the sorted concept tree, the model that '
      'built it, and the hash of the earlier bundle for comparison. That record is how we can state '
      'with confidence that the second configuration’s bundle genuinely differs from the '
      'first’s rather than being an accidental copy — an error that was in fact caught by '
      'exactly this check during development and forced an entire completed run to be discarded.'),
('p', 'One honest caveat about reproducibility belongs here. Mixture-of-experts routing means the '
      'extraction step is not bit-reproducible even at temperature zero. Two rebuilds from identical '
      'inputs produced identical concept and link counts, 358 and 1,031, but different tree hashes. '
      'The structure is stable; the bytes are not, and we do not claim otherwise.'),

('t', 'Table 2.1 Implementation stack',
 [['Layer', 'Component', 'Role in the experiment'],
  ['Language', 'Python 3.11', 'Entire pipeline, analysis and figures'],
  ['Embedding', 'all-MiniLM-L6-v2 (384-d)', 'Shared by both retrieval arms'],
  ['Similarity', 'Exact cosine, NumPy', 'No approximate index, no tunable parameter'],
  ['Inference server', 'Ollama (OpenAI-compatible)', 'Serves generator and judge locally'],
  ['Generator (v1)', 'Llama 3.1 8B', 'Extraction, generation and judging'],
  ['Generator (v2)', 'Nemotron-3.5-Lightning-30B-A3B (Q4_K_M)', 'Extraction and generation'],
  ['Judge (v2)', 'Qwen 2.5 7B Instruct', 'Independent grounding judge, different family'],
  ['Hardware', 'Kaggle 2 × NVIDIA T4, ~30 GiB VRAM', 'Second-configuration runs'],
  ['Data handling', 'pandas, CSV checkpoints', 'Resumable generation and scoring'],
  ['Statistics', 'Paired bootstrap, McNemar exact', 'Significance testing'],
  ['Figures', 'matplotlib', 'All plots in Chapter 3'],
  ['Configuration', 'YAML with an extends mechanism', 'Provable variable control between runs'],
 ]),

('h2', '2.3 Literature Review'),
('p', 'Five pieces of work define the space this project sits in. They are summarised in Table 2.2 '
      'and then discussed individually, with attention to what each one holds fixed and what it '
      'varies, because that is the axis along which OKF-RAG differs from all of them.'),

('t', 'Table 2.2 Comparison of closely related work',
 [['Ref.', 'Work and year', 'Core idea', 'What it changes', 'Reported benefit', 'Gap it leaves'],
  ['[10]', 'Lewis et al., RAG, 2020',
   'Dense retriever feeding a seq2seq generator, trained end to end',
   'Adds non-parametric memory to generation',
   'Higher factual accuracy on knowledge-intensive tasks than a parametric model',
   'Retrieved unit is an undifferentiated passage'],
  ['[7]', 'Jiang et al., FLARE, 2023',
   'Retrieve again mid-generation whenever the next sentence is low-confidence',
   'The retrieval schedule',
   'Better grounding on long-form generation',
   'Substrate untouched; cost rises with extra retrieval rounds'],
  ['[1]', 'Asai et al., Self-RAG, 2023',
   'Model emits reflection tokens deciding when to retrieve and whether output is supported',
   'The model, through additional training',
   'Improved factuality and self-assessed citation quality',
   'Requires fine-tuning; assumes passage-shaped evidence'],
  ['[2]', 'Bechard and Ayala, 2024',
   'RAG combined with schema-constrained structured output',
   'The shape of the generated output',
   'Lower hallucination in workflow generation',
   'Structure on the output, not on the retrieved unit'],
  ['[15]', 'ReRAG / tuning-based retrieval augmentation',
   'Adapt retriever or reranker to the downstream task',
   'Ranking quality within the existing substrate',
   'Better passage ordering and relevance',
   'Still ranks chunks; no cross-unit relations'],
  ['—', 'OKF-RAG (this work)',
   'Curated, self-contained, cross-linked concept units with one-hop link expansion',
   'The atomic retrieved unit itself',
   'No significant hallucination change; 10–28% less context consumed',
   'Link precision limits the expansion benefit'],
 ]),

('h3', '2.3.1 Lewis et al. (2020) — the RAG baseline'),
('p', 'The original RAG paper [10] pairs a dense retriever over a Wikipedia index with a '
      'sequence-to-sequence generator and trains both jointly, marginalising over retrieved passages '
      'during decoding. Its lasting contribution is architectural rather than numerical: it '
      'established that a model can be given a non-parametric memory it consults at inference time, '
      'and that doing so improves factual accuracy on knowledge-intensive tasks. Everything since '
      'has been a variation. The relevant limitation for this project is that the retrieved object '
      'is a passage of running prose, with no internal structure and no declared relationship to any '
      'other passage. Retrieval returns a ranked list and the generator sees a concatenation.'),
('h3', '2.3.2 FLARE (2023) — changing when to retrieve'),
('p', 'FLARE [7] observes that retrieving once at the beginning is a poor fit for long-form '
      'generation, because what the model needs at sentence twelve is rarely what the original '
      'question asked for. It generates a tentative next sentence, inspects the token probabilities, '
      'and if confidence is low it discards the sentence, uses it as a retrieval query, and '
      'regenerates with the new evidence. Grounding improves. The cost is extra retrieval rounds and '
      'a decoding loop that must be interrupted and resumed. For our purposes the notable thing is '
      'that FLARE treats the corpus as given: the units it retrieves are the same chunks any other '
      'system would retrieve. Adaptive scheduling and curated units are orthogonal, and in principle '
      'could be combined.'),
('h3', '2.3.3 Self-RAG (2023) — changing the model'),
('p', 'Self-RAG [1] trains a model to emit special reflection tokens that decide whether retrieval '
      'is needed for the current segment, and, after generating, whether the segment is supported by '
      'the retrieved evidence and whether it is useful. Critique is internalised rather than bolted '
      'on afterwards, and the reported gains in factuality and citation quality are substantial. The '
      'price is a fine-tuning pipeline and a training corpus annotated with those tokens, which puts '
      'the method out of reach for a project running quantised open weights on two consumer GPUs. '
      'Self-RAG also assumes the evidence arrives as passages; a better-shaped unit would help it '
      'too, which again suggests the two directions are complementary.'),
('h3', '2.3.4 Bechard and Ayala (2024) — structure on the output'),
('p', 'This is the closest of the five to the present work in spirit [2]. Working on a '
      'workflow-generation task, the authors combine retrieval with schema-constrained decoding so '
      'that the model must emit a valid structured object, and they report a clear drop in '
      'hallucination compared with free-form generation plus retrieval. The result is good evidence '
      'that *structure helps grounding*. But the structure is imposed at the output end. The '
      'retrieved evidence remains unstructured text, and the constraint prevents malformed answers '
      'rather than improving what the model has to reason over. OKF-RAG applies the same intuition '
      'to the other end of the pipeline, and the null result reported in Chapter 3 is therefore '
      'genuinely interesting: structure on the output helped, structure on the input did not, at '
      'least not in this configuration and at this link precision.'),
('h3', '2.3.5 Tuning-based retrieval augmentation'),
('p', 'The final family adapts the retrieval components themselves, training or tuning a reranker so '
      'that the passages surfaced for a query are better ordered for the downstream generator [15]. '
      'Gains here are real and cheap to obtain relative to fine-tuning the generator. The substrate '
      'is untouched: a better-ranked list of chunks is still a list of chunks, and no relationship '
      'between two retrieved items is ever made explicit. A question whose answer requires joining '
      'two documents is served, at best, by hoping both rank in the top-k.'),
('h3', '2.3.6 Where OKF-RAG Sits'),
('p', 'Reading the five together, a pattern shows up. Four of the five improve grounding by changing '
      'something other than the retrieved unit: the schedule, the model, the output format, or the '
      'ranking. The fifth, GraphRAG [3], does change the index, but it does so by building an entity '
      'graph for query-focused summarisation rather than by reshaping the atomic unit that reaches '
      'the generator. OKF-RAG occupies the remaining cell. It leaves the schedule, the model, the '
      'output format and the ranker exactly as they are, and changes only what a retrieved item is.'),
('p', 'That position is what makes a null result publishable. Because the design isolates one '
      'variable, the absence of an effect is attributable to that variable rather than to an '
      'unmeasured confound. And because we audited the link graph directly, we can go further and '
      'say which part of the variable failed. Chapter 3 gives the numbers.'),
]
