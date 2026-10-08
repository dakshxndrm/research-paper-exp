# -*- coding: utf-8 -*-
"""Builds the 10-slide PIET technical seminar presentation."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

NAVY = RGBColor(0x1F, 0x3A, 0x5F)
ACC = RGBColor(0xC4, 0x4E, 0x52)
GREY = RGBColor(0x44, 0x44, 0x44)
W, H = Inches(13.333), Inches(7.5)

prs = Presentation()
prs.slide_width, prs.slide_height = W, H
BLANK = prs.slide_layouts[6]


def slide(title=None, num=None):
    s = prs.slides.add_slide(BLANK)
    if title:
        tb = s.shapes.add_textbox(Inches(0.6), Inches(0.35), Inches(12.1), Inches(0.9))
        p = tb.text_frame.paragraphs[0]
        r = p.add_run(); r.text = title
        r.font.size = Pt(34); r.font.bold = True; r.font.color.rgb = NAVY
        r.font.name = 'Calibri'
        ln = s.shapes.add_shape(1, Inches(0.6), Inches(1.28), Inches(12.1), Pt(3))
        ln.fill.solid(); ln.fill.fore_color.rgb = ACC; ln.line.fill.background()
        ln.shadow.inherit = False
    if num:
        tb = s.shapes.add_textbox(Inches(12.3), Inches(6.95), Inches(0.8), Inches(0.4))
        p = tb.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.RIGHT
        r = p.add_run(); r.text = str(num)
        r.font.size = Pt(12); r.font.color.rgb = GREY
    return s


def body(s, items, top=1.7, left=0.85, width=11.6, size=20, height=5.0):
    tb = s.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = tb.text_frame; tf.word_wrap = True
    first = True
    for it in items:
        lvl, txt = (it if isinstance(it, tuple) else (0, it))
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.level = min(max(lvl, 0), 4)
        p.space_after = Pt(10 if lvl == 0 else 5)
        if txt == '':
            continue
        bullet = '' if lvl < 0 else ('▪  ' if lvl == 0 else '–  ')
        r = p.add_run(); r.text = bullet + txt
        r.font.size = Pt(size if lvl == 0 else size - 3)
        r.font.name = 'Calibri'
        r.font.color.rgb = NAVY if lvl == 0 else GREY
        if lvl < 0:
            r.font.bold = True; r.font.color.rgb = ACC
    return tb


def tbl(s, rows, left=0.85, top=1.75, width=11.6, height=3.2, size=13):
    shp = s.shapes.add_table(len(rows), len(rows[0]), Inches(left), Inches(top),
                             Inches(width), Inches(height))
    t = shp.table
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = t.cell(i, j)
            c.text = ''
            p = c.text_frame.paragraphs[0]
            r = p.add_run(); r.text = str(val)
            r.font.size = Pt(size); r.font.name = 'Calibri'
            r.font.bold = (i == 0)
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF) if i == 0 else NAVY
    return t


def note(s, txt, top=6.35):
    tb = s.shapes.add_textbox(Inches(0.85), Inches(top), Inches(11.6), Inches(0.7))
    tb.text_frame.word_wrap = True
    p = tb.text_frame.paragraphs[0]
    r = p.add_run(); r.text = txt
    r.font.size = Pt(15); r.font.italic = True; r.font.color.rgb = ACC
    r.font.name = 'Calibri'


# ------------------------------------------------------------------ 1. Title
s = slide()
bar = s.shapes.add_shape(1, 0, 0, W, Inches(0.28))
bar.fill.solid(); bar.fill.fore_color.rgb = NAVY; bar.line.fill.background()
bar.shadow.inherit = False


def line(txt, top, size, bold=False, color=NAVY, italic=False, left=0.7, width=11.9):
    tb = s.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(0.9))
    tb.text_frame.word_wrap = True
    p = tb.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = txt
    r.font.size = Pt(size); r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color; r.font.name = 'Calibri'
    return tb


line('Presentation on', 0.55, 18, italic=True, color=GREY)
line('“OKF-RAG: Mitigating Hallucination in Retrieval-Augmented Generation '
     'using Curated Open Knowledge Format Bundles”', 0.95, 27, bold=True)
line('for Technical Seminar–(7CS7-40)', 2.35, 20, bold=True, color=ACC)
line('Submitted in partial fulfilment of the degree of Bachelor of Technology,\n'
     'Rajasthan Technical University', 2.9, 16, color=GREY)
line('ACADEMIC SESSION 2026-2027 (ODD SEMESTER)', 3.75, 16, bold=True, color=GREY)
line('DEPARTMENT OF COMPUTER ENGINEERING', 4.15, 16, bold=True)
line('Poornima Institute of Engineering & Technology, Jaipur', 4.5, 16, color=GREY)

tb = s.shapes.add_textbox(Inches(0.9), Inches(5.4), Inches(5.6), Inches(1.5))
tf = tb.text_frame; tf.word_wrap = True
for i, (lab, val) in enumerate([('Submitted to:', ''),
                                ('Madhav Sharma', ''),
                                ('Technical Seminar Coordinator', '')]):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    r = p.add_run(); r.text = lab
    r.font.size = Pt(17 if i else 15); r.font.bold = (i == 1)
    r.font.color.rgb = GREY if i != 1 else NAVY; r.font.name = 'Calibri'

tb = s.shapes.add_textbox(Inches(7.0), Inches(5.4), Inches(5.6), Inches(1.5))
tf = tb.text_frame; tf.word_wrap = True
for i, lab in enumerate(['Presented By:', 'Daksh Mahera', 'PIET23CS041']):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.alignment = PP_ALIGN.RIGHT
    r = p.add_run(); r.text = lab
    r.font.size = Pt(17 if i else 15); r.font.bold = (i == 1)
    r.font.color.rgb = GREY if i != 1 else NAVY; r.font.name = 'Calibri'

# ------------------------------------------------------------------ 2. Contents
s = slide('Contents', 2)
body(s, ['Objective',
         'Literature Review',
         'Problem Identification & Definition',
         'Proposed Methodology',
         'Tools / Simulator Used',
         'Result',
         'Conclusion & Future Work',
         'References'], top=1.85, size=24)

# ------------------------------------------------------------------ 3. Objective
s = slide('Objective', 3)
body(s, [
 'Test whether curating documents into an Open Knowledge Format (OKF) bundle — small, '
 'self-contained, cross-linked concept units — reduces hallucination in RAG',
 'Compare against a conventional fixed-size chunk baseline under strict control',
 (1, 'Same 40-document Kubernetes corpus, same questions, same generator'),
 (1, 'Same temperature (0.0), seed (42) and 1,800-token context budget'),
 (1, 'Only the retrieval substrate differs'),
 'Reproduce the comparison in a second configuration: stronger generator, freshly '
 'extracted bundle, independent judge from a different model family',
 'Audit link-graph precision directly, so any result has a mechanism behind it',
 'Report the outcome as measured, including a null result',
], top=1.75, size=19)

# ------------------------------------------------------------------ 4. Literature
s = slide('Literature Review', 4)
tbl(s, [
 ['Ref.', 'Work', 'Core idea', 'What it changes', 'Gap left'],
 ['[10]', 'Lewis et al. (2020) — RAG',
  'Dense retriever + seq2seq generator, trained jointly',
  'Adds non-parametric memory', 'Retrieved unit is a plain passage'],
 ['[7]', 'Jiang et al. (2023) — FLARE',
  'Re-retrieve mid-generation on low-confidence sentences',
  'The retrieval schedule', 'Substrate untouched; extra cost'],
 ['[1]', 'Asai et al. (2023) — Self-RAG',
  'Reflection tokens decide when to retrieve and if output is supported',
  'The model, via fine-tuning', 'Needs training; assumes passages'],
 ['[2]', 'Bechard & Ayala (2024)',
  'RAG + schema-constrained structured output',
  'Shape of the OUTPUT', 'Input evidence still unstructured'],
 ['[15]', 'ReRAG / tuning-based',
  'Tune retriever or reranker to the task',
  'Ranking within the substrate', 'Still ranks chunks; no relations'],
 ['—', 'OKF-RAG (this work)',
  'Curated, cross-linked concept units + one-hop link expansion',
  'The retrieved UNIT itself', 'Link precision limits the benefit'],
], size=12, height=4.0)
note(s, 'Four of five improve grounding by changing something other than the retrieved unit. '
        'OKF-RAG occupies the remaining cell.', top=6.15)

# ------------------------------------------------------------------ 5. Problem
s = slide('Problem Identification & Definition', 5)
body(s, [
 (-1, 'Problem'),
 'LLMs fabricate confident, well-formed but unsupported claims. RAG reduces this but does '
 'not eliminate it.',
 (-1, 'Identification'),
 'Almost every deployed RAG system retrieves fixed-size chunks. That design was never chosen '
 'on merit — it is simply easy to implement.',
 (1, 'A 512-token window starts mid-sentence and loses its section context'),
 (1, 'Two unrelated topics can share one chunk merely by page adjacency'),
 (1, 'No relationship between retrieved items is ever made explicit'),
 (-1, 'Definition'),
 'Does replacing chunks with curated, self-contained, cross-linked concept units reduce '
 'hallucination, holding every other variable constant?',
], top=1.7, size=18)

# ------------------------------------------------------------------ 6. Methodology
s = slide('Proposed Methodology', 6)
body(s, [
 (-1, 'Arm A — Chunk baseline'),
 '512-token windows, 64-token overlap → embed → top-8 cosine → pack to 1,800 tokens '
 '(~3.1 chunks/question)',
 (-1, 'Arm B — OKF-RAG'),
 'Bundle build: LLM extracts concepts (title, description, body, aliases); cross-linking is '
 'exact string matching — deterministic, no LLM',
 'Retrieval: embed title+description → top-5 seeds → follow links one hop (max 4 expansions) '
 '→ pack to the same 1,800 tokens (~8.3 units/question)',
 (-1, 'Two configurations'),
 'v1 — Llama 3.1 8B, 371 concepts / 1,103 links, n=60, self-judged',
 'v2 — Nemotron-3.5-Lightning-30B, 358 concepts / 1,031 links, n=65, judged by Qwen 2.5 7B '
 '(different family)',
 (-1, 'Evaluation'),
 'EM, token F1, retrieval recall, citation validity, context tokens; LLM judge for screening, '
 'human labels reported; paired bootstrap + McNemar exact',
], top=1.62, size=16.5)

# ------------------------------------------------------------------ 7. Tools
s = slide('Tools / Simulator Used', 7)
tbl(s, [
 ['Layer', 'Component', 'Role'],
 ['Language', 'Python 3.11', 'Entire pipeline, analysis, figures'],
 ['Embedding', 'all-MiniLM-L6-v2 (384-d)', 'Shared by both arms'],
 ['Similarity', 'Exact cosine (NumPy)', 'No approximate index, no tunable knob'],
 ['Inference server', 'Ollama (OpenAI-compatible)', 'Serves generator and judge locally'],
 ['Generator v1', 'Llama 3.1 8B', 'Extraction, generation, judging'],
 ['Generator v2', 'Nemotron-3.5-Lightning-30B-A3B (Q4_K_M)', 'Extraction and generation'],
 ['Judge v2', 'Qwen 2.5 7B Instruct', 'Independent judge, different family'],
 ['Hardware', 'Kaggle 2 × NVIDIA T4 (~30 GiB VRAM)', 'Configuration v2 runs'],
 ['Data / stats', 'pandas, paired bootstrap, McNemar', 'Scoring and significance'],
 ['Config / VCS', 'YAML (extends), Git, SHA-256 provenance', 'Provable variable control'],
], size=13, height=4.3)
note(s, 'Pure-software stack. Hosted APIs (Groq, Gemini, NVIDIA NIM) were abandoned after '
        'quota exhaustion mid-run.', top=6.35)

# ------------------------------------------------------------------ 8. Results
s = slide('Result', 8)
tbl(s, [
 ['Configuration', 'n', 'Chunk', 'OKF', 'Delta', 'Bootstrap p', 'McNemar'],
 ['v1 — Llama 3.1 8B', '60', '0.0333', '0.0833', '+0.0500 (OKF worse)', '0.3056',
  '5/2, p = 0.4531'],
 ['v2 — Nemotron 30B', '65', '0.0308', '0.0154', '−0.0154 (OKF better)', '0.6042',
  '1/2, p = 1.0000'],
], size=14, height=1.2, top=1.70)
body(s, [
 (-1, 'Headline: no statistically significant hallucination difference in EITHER configuration'),
 'The sign of the point estimate reverses between runs — behaviour consistent with noise '
 'around zero. Event counts are 1–5 per arm.',
 (-1, 'Efficiency — the one solid win'),
 'Context tokens per question: 1,615 → 1,163 (−28.0%) in v1; 1,645 → 1,473 (−10.4%) in v2, at '
 'unchanged F1/EM and ~2.7× more addressable units',
 (-1, 'Mechanism — link precision (100-link hand-graded sample)'),
 'Title-matched links 0.778 strict; alias-matched links only 0.315 strict — and alias links are '
 '~78% of the graph. Link expansion was running on a mostly wrong graph.',
 (-1, 'Also measured'),
 'Both arms abstained on 10/10 unanswerable questions; 9 abstentions were reasoning misses on '
 'evidence already in context; judge-vs-judge Cohen’s κ = 0.518',
], top=3.45, size=15, height=3.4)

# ------------------------------------------------------------------ 9. Conclusion
s = slide('Conclusion and Future Work', 9)
body(s, [
 (-1, 'Conclusion'),
 'Curation did not reduce hallucination — in either configuration, across a change of '
 'generator scale, bundle provenance, judge family and question set',
 'Three contributions survive the null: (i) a rigorously controlled negative result, '
 '(ii) a real 10–28% context-cost reduction at equal answer quality, (iii) a mechanistic '
 'explanation via link precision',
 'The study was underpowered: at 1–5 hallucination events per arm, one relabelled row flips '
 'the sign. The honest claim is “no difference detected”, not “no difference exists”.',
 (-1, 'Future Work'),
 'Filter ambiguous and generic aliases, rebuild, rerun — highest value, one rule + one rebuild',
 'Carry the existing title-only bundle (387 high-precision links) through a full run',
 'Author several hundred questions; prioritise verified multi-hop (only 18 exist today)',
 'Concept-level gold annotations for like-for-like retrieval recall',
 'Two or three independent judges, reporting agreement alongside the rate',
 'Target the reasoning bottleneck: evidence arrived, the model failed to join it',
], top=1.68, size=16.5)

# ------------------------------------------------------------------ 10. References
s = slide('References', 10)
body(s, [
 (-1, 'Asai, A., Wu, Z., Wang, Y., Sil, A., Hajishirzi, H. (2024). Self-RAG: Learning to '
      'Retrieve, Generate and Critique through Self-Reflection. ICLR.'),
 (-1, 'Bechard, P., Ayala, O. M. (2024). Reducing Hallucination in Structured Outputs via '
      'Retrieval-Augmented Generation. NAACL (Industry Track), 228–238.'),
 (-1, 'Edge, D. et al. (2024). From Local to Global: A Graph RAG Approach to Query-Focused '
      'Summarization. arXiv:2404.16130.'),
 (-1, 'Gao, Y. et al. (2023). Retrieval-Augmented Generation for Large Language Models: '
      'A Survey. arXiv:2312.10997.'),
 (-1, 'Ji, Z. et al. (2023). Survey of Hallucination in Natural Language Generation. '
      'ACM Computing Surveys, 55(12), 1–38.'),
 (-1, 'Jiang, Z. et al. (2023). Active Retrieval Augmented Generation. EMNLP, 7969–7992.'),
 (-1, 'Lewis, P. et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP '
      'Tasks. NeurIPS 33, 9459–9474.'),
 (-1, 'Reimers, N., Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese '
      'BERT-Networks. EMNLP, 3982–3992.'),
 (-1, 'Shuster, K. et al. (2021). Retrieval Augmentation Reduces Hallucination in '
      'Conversation. Findings of EMNLP, 3784–3803.'),
 (-1, 'Kubernetes Authors. Kubernetes Documentation: Concepts. https://kubernetes.io/docs/'
      'concepts/ [accessed: TO BE FILLED]'),
], top=1.7, size=14)

prs.save('OKF_RAG_Seminar_PPT.pptx')
print('saved OKF_RAG_Seminar_PPT.pptx  slides=%d' % len(prs.slides))
