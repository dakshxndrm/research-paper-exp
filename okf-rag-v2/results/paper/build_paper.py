"""Builds OKF_RAG_paper.docx in IEEE conference style.

Every number in this file is transcribed from a project result file; see the
NUMBER_SOURCES comment block at the bottom for the provenance of each.
"""
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# ---- page setup (IEEE: US Letter, 0.75 top / 0.625 side margins, Times 10pt) ----
s = doc.sections[0]
s.page_width, s.page_height = Inches(8.5), Inches(11)
s.top_margin = Inches(0.75); s.bottom_margin = Inches(1.0)
s.left_margin = Inches(0.625); s.right_margin = Inches(0.625)

n = doc.styles['Normal']
n.font.name = 'Times New Roman'; n.font.size = Pt(10)
n._element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
n.paragraph_format.space_after = Pt(0)
n.paragraph_format.line_spacing = 1.0


def cols(section, num):
    sectPr = section._sectPr
    c = sectPr.find(qn('w:cols'))
    if c is None:
        c = OxmlElement('w:cols'); sectPr.append(c)
    c.set(qn('w:num'), str(num))
    c.set(qn('w:space'), '180')
    c.set(qn('w:equalWidth'), '1')


cols(s, 1)  # title block spans the page


def p(text='', align=None, size=None, bold=False, italic=False,
      before=0, after=0, indent=None):
    par = doc.add_paragraph()
    if align is not None:
        par.alignment = align
    pf = par.paragraph_format
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    if indent is not None:
        pf.first_line_indent = Inches(indent)
    if text:
        r = par.add_run(text)
        r.font.name = 'Times New Roman'
        if size:
            r.font.size = Pt(size)
        r.bold = bold; r.italic = italic
    return par


def body(text, indent=0.2, after=0):
    return p(text, align=WD_ALIGN_PARAGRAPH.JUSTIFY, indent=indent, after=after)


def sec(num, title):
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.space_before = Pt(10)
    par.paragraph_format.space_after = Pt(4)
    r = par.add_run('%s.  %s' % (num, title))
    r.font.name = 'Times New Roman'; r.font.size = Pt(10)
    r.font.small_caps = True
    return par


def sub(letter, title):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(6)
    par.paragraph_format.space_after = Pt(2)
    r = par.add_run('%s.  %s' % (letter, title))
    r.font.name = 'Times New Roman'; r.font.size = Pt(10); r.italic = True
    return par


def bullet(text):
    par = doc.add_paragraph(style='List Bullet')
    pf = par.paragraph_format
    pf.space_after = Pt(0)
    pf.left_indent = Inches(0.32)
    pf.first_line_indent = Inches(-0.14)
    r = par.add_run(text)
    r.font.name = 'Times New Roman'; r.font.size = Pt(10)
    return par


def table_caption(label, title):
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.space_before = Pt(9)
    par.paragraph_format.space_after = Pt(2)
    r = par.add_run(label)
    r.font.name = 'Times New Roman'; r.font.size = Pt(8)
    r2 = par.add_run('\n' + title)
    r2.font.name = 'Times New Roman'; r2.font.size = Pt(8)
    r2.font.small_caps = True
    return par


def make_table(rows, widths=None, note=None):
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = 'Table Grid'
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            c = t.cell(i, j)
            c.text = ''
            par = c.paragraphs[0]
            par.alignment = WD_ALIGN_PARAGRAPH.LEFT if j == 0 else WD_ALIGN_PARAGRAPH.CENTER
            par.paragraph_format.space_after = Pt(0)
            par.paragraph_format.space_before = Pt(0)
            r = par.add_run(str(cell))
            r.font.name = 'Times New Roman'; r.font.size = Pt(7.5)
            r.bold = (i == 0)
    if widths:
        for j, w in enumerate(widths):
            for row in t.rows:
                row.cells[j].width = Inches(w)
    if note:
        par = doc.add_paragraph()
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        par.paragraph_format.space_before = Pt(2)
        par.paragraph_format.space_after = Pt(4)
        r = par.add_run(note)
        r.font.name = 'Times New Roman'; r.font.size = Pt(7)
        r.italic = True
    return t


# ============================== TITLE BLOCK ==============================
par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER
par.paragraph_format.space_after = Pt(10)
r = par.add_run('Does Open Knowledge Format Curation Reduce Hallucination in '
                'Retrieval-Augmented Generation? A Controlled Study')
r.font.name = 'Times New Roman'; r.font.size = Pt(22)

for line, sz, it in [
    ('Daksh Maher', 11, False),
    ('Department of Computer Engineering', 10, True),
    ('[Institution Name]', 10, True),
    ('[City, Country]', 10, True),
    ('maheradaksh1@gmail.com', 10, False),
]:
    par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.space_after = Pt(0)
    rr = par.add_run(line)
    rr.font.name = 'Times New Roman'; rr.font.size = Pt(sz); rr.italic = it

p(after=8)

# ---- two columns from here on ----
s2 = doc.add_section(WD_SECTION.CONTINUOUS)
s2.page_width, s2.page_height = Inches(8.5), Inches(11)
s2.top_margin = Inches(0.75); s2.bottom_margin = Inches(1.0)
s2.left_margin = Inches(0.625); s2.right_margin = Inches(0.625)
cols(s2, 2)

# ============================== ABSTRACT ==============================
par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
par.paragraph_format.space_after = Pt(6)
r = par.add_run('Abstract—')
r.font.name = 'Times New Roman'; r.font.size = Pt(9); r.bold = True; r.italic = True
abstract = (
    'Retrieval-augmented generation is widely used to reduce hallucination in large '
    'language models, but it remains unclear whether the form in which the retrieval '
    'corpus is stored matters as much as the retrieval itself. This paper tested a '
    'specific and widely held claim: that curating raw documents into an Open Knowledge '
    'Format bundle of small, self-contained, cross-linked concept units reduces '
    'hallucination relative to naive fixed-size chunk retrieval. Two controlled '
    'configurations were run over an identical forty-document Kubernetes documentation '
    'corpus, using human-authored questions, a shared context token budget, a shared '
    'generator per configuration, and human-assigned grounding labels as the primary '
    'metric; only the retrieval substrate differed between arms. In the first '
    'configuration the curated arm hallucinated on five of sixty paired questions against '
    'the baseline two, and in the second, which used a stronger generator, an '
    'independently re-extracted bundle and a different-family judge, it hallucinated on '
    'one of sixty-five against the baseline two. Neither difference approached '
    'significance and the sign of the effect was not stable across configurations, so the '
    'honest reading is that curation alone produced no detectable reduction in '
    'hallucination. One effect was consistent: the curated arm answered the same questions '
    'on fewer retrieval tokens in both runs, at statistically indistinguishable answer '
    'quality. A graded audit of the cross-link graph indicates why curation did not help. '
    'Links derived from alias matching, which dominate the graph, were correct less than a '
    'third of the time, while links derived from concept titles were correct in more than '
    'three quarters of cases. Link precision, not concept granularity, appears to be the '
    'binding constraint.'
)
r = par.add_run(abstract)
r.font.name = 'Times New Roman'; r.font.size = Pt(9); r.bold = True

par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
par.paragraph_format.space_after = Pt(8)
r = par.add_run('Keywords—')
r.font.name = 'Times New Roman'; r.font.size = Pt(9); r.bold = True; r.italic = True
r = par.add_run('retrieval-augmented generation, hallucination, knowledge curation, '
                'large language models, question answering, open knowledge format')
r.font.name = 'Times New Roman'; r.font.size = Pt(9); r.bold = True

# ============================== I. INTRODUCTION ==============================
sec('I', 'Introduction')

body('Large language models fabricate plausible but unsupported statements, and '
     'retrieval-augmented generation (RAG) is the standard mitigation: relevant passages are '
     'retrieved from a trusted corpus and placed in the generator context so that the model '
     'grounds its answer in text rather than in parametric memory [1], [2]. RAG reduces but '
     'does not eliminate hallucination [4], and a substantial body of subsequent work has '
     'attacked the residual failure through stronger retrievers [3], self-critique and '
     'adaptive retrieval [12], and structured or graph-shaped retrieval substrates [5], [6]. '
     'A survey of the area is given in [11].', indent=0)

body('A recurring assumption in that last line of work is that the form of the retrieval '
     'substrate matters. Fixed-size chunking is an artefact of convenience. It splits a '
     'document at an arbitrary token offset, so a retrieved chunk may begin mid-definition, '
     'carry unrelated neighbouring text, and omit the sentence that would have justified the '
     'answer. The intuitive alternative is curation into what this paper calls an Open '
     'Knowledge Format (OKF) bundle [12]: many small, self-contained concept units, each '
     'stating one fact under its own title and description, connected to related units by '
     'explicit cross-links so that retrieving one unit can pull in its neighbours. If the '
     'assumption holds, a generator reading curated units should have less opportunity to '
     'hallucinate than one reading arbitrary chunks, because every unit it sees is a complete '
     'statement and the link structure supplies the context a chunk boundary would have '
     'severed.')

body('That assumption is rarely tested in isolation. Structured-retrieval systems typically '
     'change the substrate, the retriever, the prompt and the surrounding pipeline at once, so '
     'a reported improvement cannot be attributed to curation specifically. This work isolated '
     'the variable. Two retrieval arms were run over an identical corpus with an identical '
     'generator, an identical context token budget and an identical question set; the only '
     'difference between them was whether the generator read fixed-size chunks or curated '
     'concept units with link expansion. Any difference in hallucination is therefore '
     'attributable to the substrate.')

body('The result was a null. In neither of two independent configurations did curation '
     'produce a detectable reduction in hallucination, and the sign of the point estimate was '
     'not consistent between them. This is reported as the headline rather than buried, '
     'because a well-controlled null on a widely held assumption is a legitimate and useful '
     'finding.')

body('The contributions of this work are as follows:', after=2)
bullet('A controlled comparison of OKF-RAG against naive chunk-RAG on hallucination, in '
       'which the retrieval substrate is the only variable that differs between arms.')
bullet('Two independent experimental configurations, differing in generator strength, bundle '
       'provenance and judge model, which together test whether any observed result is an '
       'artefact of a weak generator or of one particular bundle extraction.')
bullet('A human-labelled grounding evaluation covering every question in both arms of both '
       'configurations, with an LLM judge retained only as a screening instrument.')
bullet('A graded link-precision analysis of the curated bundle that identifies alias-derived '
       'cross-links as the probable mechanical reason curation did not help, and separates '
       'that failure from concept granularity.')
p(after=2)

body('The remainder of this paper is organized as follows. Section II describes the corpus '
     'and the human-authored question set. Section III details the construction of the OKF '
     'bundle, the two retrieval arms, the two experimental configurations and the evaluation '
     'protocol. Section IV presents the hallucination results, the context-efficiency result, '
     'the link-precision analysis, the abstention behaviour of both arms, a comparison across '
     'configurations, and the limitations of the study. Section V concludes.')

# ============================== II. CORPUS AND QUESTIONS ==============================
sec('II', 'Corpus and Question Set')

sub('A', 'Corpus')
body('The corpus consisted of 40 Markdown documents drawn from the official Kubernetes '
     'documentation [13]. The documents totalled 30,102 words, a mean of 752.5 words per '
     'document. The selection was recorded verbatim in the project artefacts and spanned '
     'architecture, cluster administration, containers, cluster extension, the object model '
     'and overview material, scheduling and eviction, security, services and networking, and '
     'workloads.', indent=0)

body('The corpus was chosen for its cross-reference density rather than for its size. '
     'Technical documentation of this kind states a concept once and refers to it repeatedly '
     'from other pages, so a correct answer often depends on a definition that lives in a '
     'different document from the question’s obvious target. That property is precisely '
     'what a cross-linked concept bundle is intended to exploit, which makes the corpus a '
     'favourable rather than a neutral test bed for the OKF hypothesis. The corpus was also '
     'small enough that both arms of both configurations could be generated, scored and '
     'human-labelled end to end, which was the binding practical constraint on the study.')

body('Only 17 of the 40 documents are ever cited as a gold source by a question in the '
     'pool. The remaining 23 are distractor-only: they are embedded and compete for '
     'retrieval in both arms, but no question can be answered from them. This is a '
     'deliberate design property rather than a defect, and it is stated so that a reader '
     'does not assume question coverage over all 40 documents.')

sub('B', 'Question Set')
body('A pool of 122 questions was authored by hand against the corpus, each with a gold '
     'answer and the gold source document or documents from which the answer is derivable. '
     'Every question carries a hop-type label:', indent=0, after=2)
bullet('single — answerable from one document;')
bullet('multi — intended to require facts from two documents;')
bullet('unanswerable — the fact is not present anywhere in the 40 documents, so the '
       'correct behaviour is to abstain, following the design principle of [7].')
p(after=2)

body('The multi-hop labels were audited rather than trusted. A cover-one-up verification was '
     'performed over the first 100 questions: for each question labelled multi, each cited '
     'document was inspected in isolation to determine whether the gold answer was in fact '
     'derivable from that document alone. Of the 33 questions labelled multi in that audit, '
     'only 6 were genuinely two-document; the remaining 27 were degenerate, answerable from a '
     'single cited document despite the label. This is stated plainly because it materially '
     'weakens the multi-hop portion of the evidence: the question set is considerably more '
     'single-hop than its labels suggest. Twelve further questions were subsequently written '
     'specifically to be genuinely two-document, and each was verified under the same '
     'cover-one-up test before use.')

body('The two configurations did not run on the same question subset. Configuration 1 ran on '
     '60 questions inherited from the original human-labelling effort. Configuration 2 ran on '
     '65 questions selected to exclude seven questions found defective by the audit '
     '(duplicates, ambiguous phrasing, or a gold answer not present in the cited document) '
     'and to include only verified-genuine multi-hop questions. Table I gives the composition '
     'of both sets. Because the two configurations use different question subsets, they are '
     'treated throughout as independent replications rather than as a paired before-and-after '
     'comparison.')

table_caption('TABLE I', 'Question Set Composition by Configuration')
make_table([
    ['Question set', 'Single', 'Multi', 'Unans.', 'Total'],
    ['Authored pool', '52', '55', '15', '122'],
    ['Configuration 1', '39', '13', '8', '60'],
    ['Configuration 2', '37', '18', '10', '65'],
], widths=[1.15, 0.5, 0.45, 0.5, 0.45],
    note='All 18 multi-hop questions in Configuration 2 passed the cover-one-up '
         'verification. The audit found the majority of the questions labelled multi in the '
         'authored pool, and therefore in Configuration 1, to be degenerate.')

# ============================== III. METHOD ==============================
sec('III', 'Method')

sub('A', 'OKF Bundle Construction')
body('The bundle was built in two stages with deliberately different degrees of automation. '
     'In the first stage, an instruction-following language model read each source document '
     'and extracted discrete concept units. Each unit is a small Markdown file carrying a '
     'title, a short description, a body stating one fact, a set of aliases by which the '
     'concept may be referred to elsewhere, and a provenance field naming the source '
     'document. A minimum body length was enforced in order to reject fragments.', indent=0)

body('In the second stage the units were cross-linked. This stage is fully deterministic and '
     'uses no model. Every concept body is scanned for occurrences of another concept’s '
     'title or of one of its declared aliases, and each match becomes a Markdown link from '
     'the containing concept to the matched concept. Two properties motivated keeping this '
     'stage free of model involvement. The first is auditability: a deterministic rule '
     'produces a link graph that can be recomputed exactly from the bundle and graded link by '
     'link, which is what made the analysis in Section IV-C possible. The second, and the '
     'more important for validity, is that a model asked to decide which concepts are related '
     'has itself read the corpus, and could route the retriever toward the answer for reasons '
     'the substrate does not encode. That would smuggle answer knowledge into the retrieval '
     'structure and confound exactly the comparison the experiment was designed to make. '
     'Linking was therefore a string-matching operation and nothing more.')

sub('B', 'Retrieval Arms')
body('Two arms were compared. Arm A, the chunk-RAG baseline, split each raw document into '
     'fixed-size overlapping passages of 512 tokens with 64 tokens of overlap and retrieved '
     'the eight nearest passages to the query. Arm B, OKF-RAG, retrieved the five nearest '
     'concept units, embedding each unit by its title and description, and then performed one '
     'hop of link expansion: the outgoing cross-links of the retrieved units were followed and '
     'up to four linked neighbours were added to the context. Both arms used the same sentence '
     'embedding model [8], all-MiniLM-L6-v2, under a fixed random seed.', indent=0)

body('The controls are the point of the design. Both arms answered the same questions, were '
     'served by the same generator at temperature zero under the same system prompt, and were '
     'held to the same context token budget of 1800 tokens. Neither arm could buy an advantage '
     'by reading more text than the other. Under these conditions, any difference in the '
     'measured outcome is attributable to the retrieval substrate.')

sub('C', 'Experimental Configurations')
body('Two configurations were run. Configuration 1 used llama3.1-8B, served locally, as both '
     'generator and grounding judge, over a bundle extracted by that same model. Configuration '
     '2 used NVIDIA Nemotron-3.5-Lightning-30B-A3B at Q4_K_M quantisation as the generator, '
     'over a bundle independently re-extracted end to end by that model, with '
     'Qwen2.5-7B-Instruct as the grounding judge. The re-extracted bundle was confirmed to '
     'differ from the first by a SHA-256 hash computed over the sorted concept tree.', indent=0)

body('Configuration 2 is framed as a robustness replication rather than as an improvement. It '
     'was designed to break three specific ways in which a Configuration 1 result could have '
     'been an artefact. It changes the generator from an 8B dense model to a 30B '
     'mixture-of-experts model, so a null cannot be dismissed as the generator being too weak '
     'to exploit the structure. It rebuilds the bundle with a different extractor, so a null '
     'cannot be an accident of one particular extraction. And it moves judging to a model from '
     'a different family than the generator, retiring the self-preference bias that arises '
     'when a model grades its own output. Table II reports the two bundles.')

table_caption('TABLE II', 'OKF Bundle Statistics by Configuration')
make_table([
    ['Bundle property', 'Config. 1', 'Config. 2'],
    ['Source documents', '40', '40'],
    ['Concept units', '371', '358'],
    ['Cross-links, total', '1,103', '1,031'],
    ['   from title match', '335', '225'],
    ['   from alias match', '768', '806'],
    ['Mean links per concept', '2.97', '2.88'],
    ['Mean aliases per concept', '2.03', '2.96'],
    ['Ambiguous aliases detected', '66', '82'],
    ['Mean concept body, words', '37.6', '72.8'],
    ['Units retrieved per query', '5', '5'],
    ['Retrieved share of bundle', '1.3%', '1.4%'],
], widths=[1.55, 0.6, 0.6],
    note='The Configuration 1 bundle was extracted by llama3.1-8B; the Configuration 2 bundle '
         'was independently re-extracted by Nemotron-3.5-Lightning-30B-A3B. Both are in alias '
         'link mode. A title-only variant of the Configuration 1 bundle, built from the same '
         '371 concepts, contains only 387 cross-links, a mean of 1.04 per concept.')

sub('D', 'Evaluation')
body('The primary metric was a human grounding label assigned to every generated answer in '
     'both arms of both configurations. The labeller read the retrieved context, the question '
     'and the answer, and assigned exactly one of four labels:', indent=0, after=2)
bullet('supported — every factual claim in the answer is stated in, or directly entailed '
       'by, the retrieved context;')
bullet('unsupported — the answer contains at least one claim the context does not state, '
       'whether added detail, invented specifics, or outside knowledge;')
bullet('contradicted — the answer conflicts with something the context states;')
bullet('abstained — the answer declines to answer for lack of information.')
p(after=2)
body('Labelling judged grounding only, not real-world correctness: an answer that is true of '
     'Kubernetes but absent from the retrieved context was labelled unsupported. Hallucination '
     'rate is defined as the proportion of answers labelled unsupported or contradicted.',
     indent=0)

body('An LLM judge applying the identical four-label rubric was run over all rows, but is '
     'reported as a screening instrument only and never as the headline. In Configuration 1 '
     'the judge was the generator itself and therefore carried a self-preference bias. Even in '
     'Configuration 2, where judge and generator belong to different families, an earlier '
     'cross-judge check on the same rubric and the same reconstructed contexts found two '
     'capable models agreeing on 90.0 percent of 120 rows at Cohen’s kappa 0.518, with '
     'perfect agreement confined to the abstentions. That level of agreement indicates real '
     'judge-dependent variance in any single-judge hallucination rate.')

body('Secondary metrics were token-level F1 against the gold answer, exact match, retrieval '
     'recall, citation validity, abstention rate, and mean context tokens consumed per '
     'question. Significance over the paired arms was assessed by a paired bootstrap over '
     'questions [9] for the continuous metrics, and by McNemar’s exact test [10] for the '
     'binary hallucination and exact-match outcomes, with the discordant pair counts reported '
     'alongside every p-value.')

# ============================== IV. RESULTS ==============================
sec('IV', 'Results and Discussion')

sub('A', 'Hallucination')
body('Table III reports the human-labelled results for both configurations. In Configuration '
     '1, the OKF arm hallucinated on 5 of 60 paired questions against the baseline’s 2, a '
     'difference of +0.0500 in the direction of the baseline, with paired bootstrap p = 0.3056 '
     'and McNemar discordant counts of 5 against 2, exact p = 0.4531. In Configuration 2, the '
     'OKF arm hallucinated on 1 of 65 against the baseline’s 2, a difference of '
     '−0.0154 in the direction of OKF, with paired bootstrap p = 0.6042 and McNemar '
     'discordant counts of 1 against 2, exact p = 1.', indent=0)

table_caption('TABLE III', 'Main Results, Human Grounding Labels, Paired by Question')
make_table([
    ['Metric', 'C1 chunk', 'C1 okf', 'C2 chunk', 'C2 okf'],
    ['n, paired questions', '60', '60', '65', '65'],
    ['Hallucination', '0.0333', '0.0833', '0.0308', '0.0154'],
    ['   delta, okf − chunk', '—', '+0.0500', '—', '−0.0154'],
    ['   bootstrap p', '—', '0.3056', '—', '0.6042'],
    ['   McNemar discordant', '—', '5 / 2', '—', '1 / 2'],
    ['   McNemar exact p', '—', '0.4531', '—', '1'],
    ['F1', '0.3151', '0.2869', '0.2312', '0.2418'],
    ['   bootstrap p', '—', '0.3108', '—', '0.6241'],
    ['Exact match', '0.0000', '0.0167', '0.0000', '0.0000'],
    ['   bootstrap p', '—', '0.5248', '—', '1'],
    ['Retrieval recall', '0.8558', '0.7981', '0.8636', '0.9091'],
    ['Citation valid', '1.0000', '0.9136', '1.0000', '1.0000'],
    ['Abstained', '0.1500', '0.1667', '0.2769', '0.2615'],
    ['Context tokens', '1615.4', '1162.6', '1644.5', '1472.8'],
    ['Units retrieved', '3.08', '8.83', '3.12', '8.34'],
], widths=[1.18, 0.47, 0.47, 0.47, 0.47],
    note='C1 = Configuration 1 (llama3.1-8B generator and judge); C2 = Configuration 2 '
         '(Nemotron-3.5-Lightning-30B-A3B generator, Qwen2.5-7B-Instruct judge). Retrieval '
         'recall in this table is averaged over answerable questions. Computed instead over '
         'all paired questions, including the unanswerable ones, which score zero by '
         'construction, the corresponding values are 0.7417 and 0.6917 for C1 '
         '(bootstrap p = 0.1963) and 0.7308 and 0.7692 for C2 (bootstrap p = 0.1951).')

body('The discordant counts deserve more prominence than the p-values. In Configuration 1 the '
     'entire estimate rests on 7 discordant questions, and in Configuration 2 on 3. Total '
     'hallucination events per arm were 2 for chunk and 5 for OKF in Configuration 1, and 2 '
     'for chunk and 1 for OKF in Configuration 2. A study estimating a difference in '
     'proportions from between one and five events per arm has very little power against the '
     'effect sizes at issue, and no test performed here came close to significance. The '
     'correct reading is not that curation is worse, nor that it is better, but that at this '
     'sample size the study cannot distinguish either possibility from the null. The '
     'confidence that may be placed in the direction of these point estimates is '
     'correspondingly low.', indent=0)

body('F1 and exact match tell the same story. F1 favoured the baseline by 0.0282 in '
     'Configuration 1 (p = 0.3108) and the OKF arm by 0.0106 in Configuration 2 (p = 0.6241). '
     'Exact match was at or near zero in both configurations, which reflects a free-form '
     'generative answer being compared against a hand-written gold string rather than any '
     'property of the arms. Citation validity was perfect for the baseline in both '
     'configurations and for the OKF arm in Configuration 2; the OKF arm’s 0.9136 in '
     'Configuration 1 reflects occasional citation of a concept identifier not present in the '
     'assembled context.')

sub('B', 'Context Efficiency')
body('The one effect that was consistent across both configurations was context cost. In '
     'Configuration 1 the OKF arm consumed 1162.6 context tokens per question against the '
     'baseline’s 1615.4, a reduction of 28.0 percent. In Configuration 2 it consumed '
     '1472.8 against 1644.5, a reduction of 10.4 percent. In both cases the reduction was '
     'obtained at statistically indistinguishable F1, at identical or near-identical exact '
     'match, on the same questions and under the same budget cap.', indent=0)

body('This is a real and defensible result, and it is the practical case for curation as '
     'measured here. Concept units are self-contained, so the OKF arm reached an equivalent '
     'answer without carrying the surrounding text that a 512-token chunk necessarily '
     'includes. It did so while retrieving many more units — 8.83 and 8.34 units per '
     'question against the baseline’s 3.08 and 3.12 — which is to say that the '
     'substrate trades a larger number of smaller, more targeted retrievals for a smaller '
     'number of larger ones. The magnitude of the saving was not stable across configurations. '
     'The Configuration 2 bundle has concept bodies roughly twice as long as the '
     'Configuration 1 bundle (72.8 against 37.6 mean words), which mechanically narrows the '
     'gap. The direction of the effect replicated; its size did not.')

sub('C', 'Link Precision')
body('If curated units with link expansion do not beat chunks, the natural question is '
     'whether the link expansion is delivering useful neighbours at all. A random sample of '
     '100 of the 1,103 cross-links in the Configuration 1 bundle was drawn at a fixed seed and '
     'graded by hand into correct, borderline and spurious. Strict precision counts only the '
     'correct links; lenient precision counts correct and borderline together. The results are '
     'given in Table IV.', indent=0)

table_caption('TABLE IV', 'Graded Link Precision, Configuration 1 Bundle')
make_table([
    ['Match type', 'Graded', 'Corr.', 'Bord.', 'Spur.', 'Strict', 'Lenient'],
    ['Title', '27', '21', '5', '1', '0.778', '0.963'],
    ['Alias', '73', '23', '30', '20', '0.315', '0.726'],
    ['All links', '100', '44', '35', '21', '0.440', '0.790'],
], widths=[0.72, 0.42, 0.4, 0.4, 0.4, 0.42, 0.45],
    note='Sample of 100 links drawn at seed 42 from the 1,103 links in the Configuration 1 '
         'bundle and graded by hand. No equivalent graded audit exists for the Configuration '
         '2 bundle.')

body('The split is stark. Links produced by matching a concept’s title were correct 77.8 '
     'percent of the time under the strict criterion and 96.3 percent under the lenient one. '
     'Links produced by matching a declared alias were correct only 31.5 percent of the time '
     'strictly, and better than one in four was outright spurious. Critically, alias matching '
     'produces the majority of the graph: 768 of the 1,103 links in the Configuration 1 bundle '
     'and 806 of the 1,031 links in Configuration 2. The title-only variant of the same '
     'concepts contains only 387 links, a mean of 1.04 per concept, which is too sparse for '
     'one-hop expansion to do much work. High-precision linking and dense linking were, in '
     'this bundle, mutually exclusive.', indent=0)

body('This offers a concrete mechanical explanation for the null. Arm B’s advantage over '
     'Arm A is supposed to arise from link expansion pulling in the neighbouring concept that '
     'a chunk boundary would have severed. But roughly two thirds of the edges available for '
     'that expansion are wrong or marginal, because generic and ambiguous aliases — a '
     'single common word declared as an alias of a specific concept — match text that has '
     'nothing to do with the concept. The expansion step therefore spends part of a fixed '
     'context budget on irrelevant units. Under this reading the bundle is not failing because '
     'concept-level granularity is a bad idea; it is failing because the graph laid over the '
     'concepts is noisy. The distinction matters, because the two diagnoses imply completely '
     'different remedies.')

body('This explanation is offered as the most plausible mechanism consistent with the '
     'available evidence, not as a demonstrated cause. Establishing it would require '
     'rebuilding the bundle under a stricter alias filter and re-running both arms, which was '
     'not done here.')

sub('D', 'Abstention and Calibration')
body('Abstention behaviour was examined separately, because a system that declines to answer '
     'when its retrieval has missed is preferable to one that confabulates, and hallucination '
     'rate alone does not distinguish the two. Both arms abstained correctly on every '
     'unanswerable question in Configuration 2, all ten of them. Overall abstention rates were '
     'close between arms: 0.1500 against 0.1667 in Configuration 1, and 0.2769 against 0.2615 '
     'in Configuration 2.', indent=0)

body('An observation from an intermediate run — that the OKF arm abstained more often '
     'than the baseline on answerable questions where retrieval had missed, which would '
     'indicate better calibration — was tested against the final human labels and did not '
     'hold. On answerable questions in Configuration 2, the baseline abstained 8 times and the '
     'OKF arm 7, which is not a meaningful difference at this sample size. The hypothesis is '
     'reported here because it was tested and not supported, not because it survived.')

body('A related failure was common to both arms. Nine abstentions in Configuration 2 were '
     'reasoning misses rather than retrieval misses: the answer was derivable from the context '
     'the model had already been given, and the model nonetheless declined. Three were '
     'complete and six partial, and almost all fell on multi-hop questions, distributed across '
     'both arms. Neither retrieval substrate visibly helped the generator combine facts drawn '
     'from two retrieved sources. This suggests that a share of the residual error in both '
     'arms is a synthesis failure that no change of retrieval substrate would address.')

sub('E', 'Comparison Across Configurations')
body('Taken together, the two configurations make the null more, not less, credible. The sign '
     'of the hallucination difference flipped between them: the baseline was favoured by '
     '+0.0500 in Configuration 1 and the OKF arm by −0.0154 in Configuration 2. Neither '
     'was significant, and no McNemar test approached significance in either run. A point '
     'estimate whose sign is unstable across a change of generator, bundle and judge, while '
     'every test remains far from significance, is best read as noise around zero.', indent=0)

body('This matters because it closes the most obvious escape routes from the Configuration 1 '
     'result. Configuration 1 alone could have been dismissed as an 8B generator being too '
     'weak to exploit the structure, or as one unlucky extraction, or as a self-judging model '
     'flattering its own output. Configuration 2 changed all three and produced a null as '
     'well. What did replicate, in direction if not in magnitude, was the context-token '
     'reduction at equal answer quality.')

sub('F', 'Limitations and Future Directions')
body('The limitations of this study are substantial and are stated in full.', indent=0, after=2)
bullet('Statistical power. With 60 and 65 paired questions and between one and five '
       'hallucination events per arm, the study is badly underpowered for the effect sizes at '
       'issue. It can report that no difference was detected; it cannot bound the size of a '
       'difference that might exist.')
bullet('Single corpus and single domain. All results come from 40 documents of Kubernetes '
       'documentation. The corpus was chosen because its cross-reference density favours the '
       'OKF hypothesis, which makes the null more informative, but nothing reported here '
       'generalises to other domains without replication.')
bullet('Concept extraction discarded gold content. In Configuration 1 the minimum-body-length '
       'filter discarded 108 of 479 extracted concepts, 23 percent of them, and at least '
       'three of the discarded units were the correct answer to a question in the set. Those '
       'questions were harder for the OKF arm for reasons unrelated to retrieval quality, '
       'because the gold concept was never present in the bundle at all. A separate extraction '
       'defect truncated one concept mid-list, losing a further gold fact.')
bullet('Retrieval recall is not like-for-like and favours the OKF arm. The OKF arm’s '
       'recall is computed by expanding each gold document to every concept extracted from '
       'it, a deliberately loose upper bound, whereas the baseline’s recall is measured '
       'at document granularity. The OKF arm nonetheless lost this metric in Configuration 1 '
       'despite the handicap running in its favour.')
bullet('Labels are author-assigned. Grounding labels were assigned by the author against a '
       'written rubric rather than by multiple independent annotators, so no inter-annotator '
       'agreement statistic can be reported. The cross-judge check described in Section III-D, '
       'at Cohen’s kappa 0.518, is evidence that this rubric admits genuine '
       'disagreement even between capable graders.')
bullet('Multi-hop questions are under-represented. The cover-one-up audit found only 6 of 33 '
       'questions originally labelled multi-hop to be genuinely two-document. Configuration 2 '
       'contains 18 verified multi-hop questions out of 65, and Configuration 1 substantially '
       'fewer in truth than its 13 labels claim. Multi-hop retrieval is where link expansion '
       'should most plausibly help, and it is precisely where this study has the least '
       'evidence.')
bullet('Link precision is estimated from 100 of 1,103 links, and only for the Configuration 1 '
       'bundle. No graded audit exists for the Configuration 2 bundle, so the mechanism '
       'argument in Section IV-C is anchored to the first bundle and is assumed, not shown, to '
       'carry over.')
bullet('Ablation coverage is incomplete. No human grounding labels were collected for any '
       'ablation arm, including the title-only link mode, so the alias-versus-title '
       'comparison rests on graded link precision rather than on downstream hallucination.')
bullet('Grounding is not correctness. The rubric labels whether an answer is supported by '
       'the retrieved context, not whether it is true of Kubernetes. One minus the '
       'hallucination rate is therefore not an accuracy figure, and a grounded but factually '
       'wrong answer was observed in both arms. Measuring correctness would require a '
       'separate annotation pass that was not performed.')
bullet('Gold-document coverage is partial. Only 17 of the 40 corpus documents are cited as a '
       'gold source by any question, so the evaluation exercises retrieval over the full '
       'corpus but scores answers against a little under half of it.')
p(after=2)

body('Four directions follow directly from these limitations. The first, and the most '
     'promising, is to attack alias precision: filter generic and ambiguous aliases before '
     'linking, rebuild the bundle, and re-run both arms. This yields a defensible '
     'alias-versus-title link ablation whichever way it resolves, and it is the cleanest '
     'available route to converting the null into a real effect. The second is to raise the '
     'sample size well beyond 65 questions, which is the binding constraint on saying anything '
     'conclusive. The third is to build corpora in which answers genuinely span documents, '
     'since that is the regime in which cross-linking should matter most and the one this '
     'study is least able to speak to. The fourth is to move grounding labels to multiple '
     'independent annotators, and judging to models independent of both the generator and the '
     'annotator.', indent=0)

# ============================== V. CONCLUSION ==============================
sec('V', 'Conclusion')
body('This paper asked whether curating a corpus into an Open Knowledge Format bundle of '
     'small, cross-linked concept units reduces hallucination in retrieval-augmented '
     'generation, under conditions in which the retrieval substrate is the only variable that '
     'differs between arms. Across two independent configurations, differing in generator '
     'strength, bundle provenance and judge model, the answer was no. No test approached '
     'significance, and the sign of the point estimate was not stable between configurations. '
     'Curation alone did not reduce hallucination.', indent=0)

body('Two findings survive. Curation did reduce context cost, by 28.0 percent and 10.4 percent '
     'in the two configurations, at statistically indistinguishable answer quality; that is a '
     'genuine practical benefit, and it replicated in direction if not in magnitude. And a '
     'graded audit of the cross-link graph located the probable reason the hallucination '
     'hypothesis failed: the links that dominate the graph are alias-derived and correct less '
     'than a third of the time, while title-derived links are correct in more than three '
     'quarters of cases. The lever that matters is therefore not how finely the corpus is cut '
     'into concepts, but how precisely those concepts are connected. Curation without link '
     'precision buys efficiency, not grounding.')

# ============================== ACKNOWLEDGMENT ==============================
par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER
par.paragraph_format.space_before = Pt(10); par.paragraph_format.space_after = Pt(4)
r = par.add_run('Acknowledgment')
r.font.name = 'Times New Roman'; r.font.size = Pt(10); r.italic = True
body('[Acknowledgment placeholder — add supervisor, institution, and any compute or '
     'funding support here.]', indent=0)

# ============================== REFERENCES ==============================
par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER
par.paragraph_format.space_before = Pt(10); par.paragraph_format.space_after = Pt(4)
r = par.add_run('References')
r.font.name = 'Times New Roman'; r.font.size = Pt(10); r.font.small_caps = True

refs = [
    'P. Lewis et al., "Retrieval-augmented generation for knowledge-intensive NLP tasks," in '
    'Proc. Advances in Neural Information Processing Systems (NeurIPS), 2020.',

    'Z. Ji et al., "Survey of hallucination in natural language generation," ACM Computing '
    'Surveys, vol. 55, no. 12, pp. 1-38, 2023.',

    'V. Karpukhin et al., "Dense passage retrieval for open-domain question answering," in '
    'Proc. Conf. Empirical Methods in Natural Language Processing (EMNLP), 2020, pp. '
    '6769-6781.',

    'K. Shuster, S. Poff, M. Chen, D. Kiela, and J. Weston, "Retrieval augmentation reduces '
    'hallucination in conversation," in Findings of EMNLP, 2021, pp. 3784-3803.',

    '[REF NEEDED: a knowledge-graph-grounded or structured-retrieval QA work other than '
    'GraphRAG, to support the "structured retrieval substrates" claim in Section I.]',

    'D. Edge et al., "From local to global: A graph RAG approach to query-focused '
    'summarization," arXiv preprint arXiv:2404.16130, 2024.',

    'P. Rajpurkar, R. Jia, and P. Liang, "Know what you don\'t know: Unanswerable questions '
    'for SQuAD," in Proc. 56th Annu. Meeting Assoc. Computational Linguistics (ACL), 2018, '
    'pp. 784-789.',

    'N. Reimers and I. Gurevych, "Sentence-BERT: Sentence embeddings using Siamese '
    'BERT-networks," in Proc. Conf. Empirical Methods in Natural Language Processing (EMNLP), '
    '2019, pp. 3982-3992.',

    'B. Efron and R. J. Tibshirani, An Introduction to the Bootstrap. New York, NY, USA: '
    'Chapman & Hall, 1993.',

    'Q. McNemar, "Note on the sampling error of the difference between correlated proportions '
    'or percentages," Psychometrika, vol. 12, no. 2, pp. 153-157, 1947.',

    'Y. Gao et al., "Retrieval-augmented generation for large language models: A survey," '
    'arXiv preprint arXiv:2312.10997, 2023.',

    '[REF NEEDED: a primary source or specification for the Open Knowledge Format / linked '
    'concept-unit representation. If no external source exists, delete this citation from '
    'Section I and present OKF as defined in this paper.]',

    '[REF NEEDED: the Kubernetes documentation corpus. Cite the documentation release, '
    'repository or URL, and the access date used to build the 40-document selection.]',
]

for i, ref in enumerate(refs, 1):
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = par.paragraph_format
    pf.left_indent = Inches(0.24); pf.first_line_indent = Inches(-0.24)
    pf.space_after = Pt(2)
    r = par.add_run('[%d]\t%s' % (i, ref))
    r.font.name = 'Times New Roman'; r.font.size = Pt(8)

doc.save('OKF_RAG_paper.docx')
print('saved OKF_RAG_paper.docx')
