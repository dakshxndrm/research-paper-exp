# -*- coding: utf-8 -*-
APPX = [
('h1', 'APPENDIX A\nCONFIGURATION EXCERPT'),
('p', 'The configuration below is the flattened record written by the second configuration’s run, '
      'reproduced from ' + 'runmeta_okf_rag_v2_kaggle_full.json' + '. It is the authoritative '
      'statement of what the experiment ran with, because it is emitted by the driver after all '
      'overrides have been resolved rather than written by hand.'),
('c', 'experiment:\n'
      '  name: okf_rag_v2_kaggle\n'
      '  seed: 42\n\n'
      'embedding:\n'
      '  model: sentence-transformers/all-MiniLM-L6-v2\n'
      '  batch_size: 32\n\n'
      'retrieval:\n'
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
      '  model: huggingface.co/lmstudio-community/\n'
      '         NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF:Q4_K_M\n'
      '  temperature: 0.0\n'
      '  max_tokens: 8000\n'
      '  timeout_s: 600\n'
      '  retries: 5\n'
      '  seed: 42\n\n'
      'judge:\n'
      '  enabled: true\n'
      '  model: qwen2.5:7b-instruct\n'
      '  temperature: 0.0\n'
      '  max_tokens: 1500\n'
      '  seed: 42\n\n'
      'bundle_builder:\n'
      '  model: (same as generation)\n'
      '  temperature: 0.0\n'
      '  max_concepts_per_doc: 12\n'
      '  min_concept_words: 15\n'
      '  max_tokens: 16000\n'
      '  link_mode: alias\n'
      '  reasoning_effort: none\n'
      '  seed: 42'),
('p', 'Two entries in that block are worth pointing at. The *reasoning_effort* key is set to none for '
      'bundle construction and is absent from the generation block, which is the asymmetry described '
      'in Section 2.2.3: extraction fails without it and generation fails with it. And '
      '*min_concept_words* is the filter discussed in Section 5.3, which discarded roughly a quarter '
      'of the extracted concepts.'),

('h1', 'APPENDIX B\nSAMPLE QUESTIONS'),
('p', 'Nine of the 65 active questions are reproduced below, three from each category, to show what '
      'the evaluation actually asks. Gold answers are the hand-written reference strings used for '
      'exact match and token F1; gold concepts name the source documents a correct retrieval should '
      'reach.'),
('t', 'Table B.1 Sample questions from the active set',
 [['ID', 'Type', 'Question', 'Gold answer', 'Gold documents'],
  ['Q001', 'single', 'What are the two major parts of a Kubernetes cluster?',
   'A Kubernetes cluster consists of a control plane and one or more worker nodes.',
   'architecture.md'],
  ['Q004', 'single', 'What is the primary responsibility of the kube-scheduler?',
   'The kube-scheduler assigns unscheduled Pods to suitable Nodes.',
   'scheduling-eviction__kube-scheduler.md'],
  ['Q005', 'single', 'Which component ensures that Pods are running on every node?',
   'The kubelet ensures that Pods and their containers are running on each node.',
   'overview__components.md'],
  ['Q056', 'multi', 'Which component assigns IP addresses to Services, and which component '
   'forwards traffic to those Services?',
   'The kube-apiserver assigns Service IP addresses, while kube-proxy (or an equivalent network '
   'plugin) forwards traffic.',
   'cluster-administration__networking.md; architecture.md'],
  ['Q057', 'multi', 'How does Kubernetes ensure that Pods continue running after the scheduler '
   'assigns them to a node?',
   'The scheduler binds the Pod to a node, and the kubelet continuously monitors and restarts '
   'containers if necessary.',
   'scheduling-eviction__kube-scheduler.md; architecture__self-healing.md'],
  ['Q064', 'multi', 'How does Kubernetes maintain application availability when a Pod in a '
   'Deployment fails after it has already been scheduled?',
   'The Deployment controller creates a replacement Pod, and the kube-scheduler assigns the '
   'replacement Pod to a suitable node.',
   'architecture__self-healing.md; scheduling-eviction__kube-scheduler.md'],
  ['Q081', 'unanswerable', 'What is the maximum number of containers that a single Kubernetes Pod '
   'can contain?', 'UNANSWERABLE', '—'],
  ['Q082', 'unanswerable', 'Which Kubernetes version first introduced the Deployment resource?',
   'UNANSWERABLE', '—'],
  ['Q083', 'unanswerable', 'What is the default timeout value for the kube-apiserver when '
   'processing requests?', 'UNANSWERABLE', '—'],
 ]),
('p', 'The three unanswerable questions illustrate the design principle behind that category. Each '
      'asks something a reader might reasonably expect Kubernetes documentation to state, and each '
      'is something these forty pages do not state. A system that answers them has invented a number, '
      'a version or a limit. Both arms abstained on all ten in the second configuration.'),
]
