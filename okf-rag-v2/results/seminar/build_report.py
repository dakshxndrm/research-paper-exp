# -*- coding: utf-8 -*-
"""Builds OKF_RAG_Seminar_Report.docx in the PIET final-year seminar format.

Body: Times New Roman 12, 1.5 line spacing, justified, 1 inch margins.
Chapter headings TNR 16 bold; subtitles TNR 14 bold; terms in italic.
Front matter numbered i, ii, iii...; main report restarts at 1.
"""
import re
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

from content_front import *
from content_ch1 import CH1
from content_ch2 import CH2
from content_ch3 import CH3
from content_ch4 import CH4, CH5, CH6, CH7
from content_appx import APPX

TNR = 'Times New Roman'
doc = Document()

# ------------------------------------------------------------------ styles
st = doc.styles['Normal']
st.font.name = TNR
st.font.size = Pt(12)
st._element.rPr.rFonts.set(qn('w:eastAsia'), TNR)
st.paragraph_format.line_spacing = 1.5
st.paragraph_format.space_after = Pt(6)

sec = doc.sections[0]
for s_ in doc.sections:
    s_.top_margin = s_.bottom_margin = s_.left_margin = s_.right_margin = Inches(1)


def _font(run, size=12, bold=False, italic=False, name=TNR):
    run.font.name = name
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run._element.rPr.rFonts.set(qn('w:eastAsia'), name)
    return run


ALIGN = {'l': WD_ALIGN_PARAGRAPH.LEFT, 'c': WD_ALIGN_PARAGRAPH.CENTER,
         'r': WD_ALIGN_PARAGRAPH.RIGHT, 'j': WD_ALIGN_PARAGRAPH.JUSTIFY}


def para(text='', align='j', size=12, bold=False, italic=False, name=TNR,
         spacing=1.5, before=0, after=6, indent=None, left=None, hang=None):
    p = doc.add_paragraph()
    p.alignment = ALIGN[align]
    pf = p.paragraph_format
    pf.line_spacing = spacing
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    if indent is not None:
        pf.first_line_indent = Inches(indent)
    if left is not None:
        pf.left_indent = Inches(left)
    if hang is not None:
        pf.first_line_indent = Inches(-hang)
    if text:
        _font(p.add_run(text), size, bold, italic, name)
    return p


def rich(text, align='j', size=12, **kw):
    """Body paragraph; *word* renders italic (PIET: terms/definitions italicised)."""
    p = doc.add_paragraph()
    p.alignment = ALIGN[align]
    pf = p.paragraph_format
    pf.line_spacing = kw.get('spacing', 1.5)
    pf.space_before = Pt(kw.get('before', 0))
    pf.space_after = Pt(kw.get('after', 6))
    if kw.get('left') is not None:
        pf.left_indent = Inches(kw['left'])
    if kw.get('hang') is not None:
        pf.first_line_indent = Inches(-kw['hang'])
    for part in re.split(r'(\*[^*]+\*)', text):
        if not part:
            continue
        if part.startswith('*') and part.endswith('*') and len(part) > 2:
            _font(p.add_run(part[1:-1]), size, False, True)
        else:
            _font(p.add_run(part), size)
    return p


def pagebreak():
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def field(par, instr, size=12, bold=False):
    r = par.add_run()
    _font(r, size, bold)
    fc = OxmlElement('w:fldChar'); fc.set(qn('w:fldCharType'), 'begin')
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = instr
    fc2 = OxmlElement('w:fldChar'); fc2.set(qn('w:fldCharType'), 'end')
    r._r.append(fc); r._r.append(it); r._r.append(fc2)


def set_numbering(section, fmt, start=None):
    sectPr = section._sectPr
    pg = sectPr.find(qn('w:pgNumType'))
    if pg is None:
        pg = OxmlElement('w:pgNumType'); sectPr.append(pg)
    pg.set(qn('w:fmt'), fmt)
    if start is not None:
        pg.set(qn('w:start'), str(start))


# ------------------------------------------------------------------ blocks
def heading1(text):
    lines = text.split('\n')
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(18)
    for i, ln in enumerate(lines):
        if i:
            p.add_run().add_break()
        _font(p.add_run(ln), 16, bold=True)
    return p


def heading2(text):
    return para(text, 'l', 14, bold=True, before=14, after=8)


def heading3(text):
    return para(text, 'l', 12, bold=True, before=10, after=6)


def bullets(items, numbered=False):
    for i, it in enumerate(items, 1):
        marker = ('%d. ' % i) if numbered else '•  '
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        pf = p.paragraph_format
        pf.line_spacing = 1.5
        pf.left_indent = Inches(0.45)
        pf.first_line_indent = Inches(-0.3)
        pf.space_after = Pt(6)
        _font(p.add_run(marker), 12)
        for part in re.split(r'(\*[^*]+\*)', it):
            if not part:
                continue
            if part.startswith('*') and part.endswith('*') and len(part) > 2:
                _font(p.add_run(part[1:-1]), 12, False, True)
            else:
                _font(p.add_run(part), 12)


def caption(text, before=4, after=10):
    return para(text, 'c', 10, italic=True, spacing=1.0, before=before, after=after)


def table(cap, rows, size=9.5):
    caption(cap, before=10, after=4)
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            c = t.cell(i, j)
            c.text = ''
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            _font(p.add_run(str(cell)), size, bold=(i == 0))
    para('', after=8)
    return t


def figure(cap, path, width=5.3):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.add_run().add_picture(path, width=Inches(width))
    caption(cap)


def code(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.line_spacing = 1.0
    pf.left_indent = Inches(0.35)
    pf.space_before = Pt(6)
    pf.space_after = Pt(10)
    _font(p.add_run(text), 9.5, name='Consolas')
    return p


def placeholder(text):
    p = para(text, 'c', 11, bold=True, before=8, after=10, spacing=1.0)
    for r in p.runs:
        r.font.color.rgb = RGBColor(0x99, 0x00, 0x00)
    return p


def render(blocks):
    for b in blocks:
        k = b[0]
        if k == 'h1':
            heading1(b[1])
        elif k == 'h2':
            heading2(b[1])
        elif k == 'h3':
            heading3(b[1])
        elif k == 'p':
            rich(b[1])
        elif k == 'b':
            bullets(b[1])
        elif k == 'n':
            bullets(b[1], numbered=True)
        elif k == 't':
            table(b[1], b[2])
        elif k == 'f':
            figure(b[1], b[2])
        elif k == 'c':
            code(b[1])
        elif k == 'ph':
            placeholder(b[1])
        else:
            raise ValueError(k)


# ================================================================ FRONT MATTER
set_numbering(sec, 'lowerRoman', 1)

# --- 1. cover page
para('FINAL YEAR TECHNICAL SEMINAR REPORT', 'c', 11, bold=True, before=24, after=24)
placeholder('[PIET LOGO — insert the institute logo image here]')
para('', after=18)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.5; p.paragraph_format.space_after = Pt(30)
_font(p.add_run(TITLE), 14, bold=True, name='Cambria')
para('SUBMITTED BY', 'c', 11, after=6)
para(STUDENT, 'c', 11, bold=True, after=2)
para('REGISTRATION NO. ' + REGNO, 'c', 11, bold=True, after=36)
para(DEPT, 'c', 11, after=4)
para(INST, 'c', 11, after=4)
para('RAJASTHAN TECHNICAL UNIVERSITY, KOTA', 'c', 11, after=24)
para(YEAR, 'c', 11, after=0)

# --- 2. title page
pagebreak()
para('FINAL YEAR TECHNICAL SEMINAR REPORT', 'c', 11, bold=True, before=18, after=18)
placeholder('[PIET LOGO — insert the institute logo image here]')
para('', after=12)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.5; p.paragraph_format.space_after = Pt(26)
_font(p.add_run(TITLE), 14, bold=True, name='Cambria')
para('SUBMITTED BY', 'c', 11, after=6)
para(STUDENT, 'c', 11, bold=True, after=2)
para('REGISTRATION NO. ' + REGNO, 'c', 11, bold=True, after=24)
para('Submitted under the guidance of:', 'l', 10, after=2)
para(GUIDE + ', ' + GUIDE_DESIG, 'l', 10, bold=True, after=2)
para('Department of Computer Engineering', 'l', 10, after=14)
para('Deliverables: Final Year Technical Seminar Report and Seminar Presentation, submitted in '
     'partial fulfilment of the requirements for the degree of Bachelor of Technology in Computer '
     'Engineering, Rajasthan Technical University, Kota.', 'l', 10, after=20)
para(DEPT, 'c', 11, after=4)
para(INST, 'c', 11, after=14)
para(YEAR, 'c', 11, after=0)

# --- 3. certificate
pagebreak()
para(INST, 'c', 12, bold=True, before=6, after=4)
para(DEPT, 'c', 12, bold=True, after=20)
para('CERTIFICATE', 'c', 16, bold=True, after=20)
rich(CERTIFICATE, 'j', 12, after=12)
rich(CERTIFICATE2, 'j', 12, after=36)
para('Date: ______________', 'l', 12, after=4)
para('Place: Jaipur', 'l', 12, after=48)
t = doc.add_table(rows=1, cols=2)
for j, (nm, role) in enumerate([(HOD, 'Head of Department\nDepartment of Computer Engineering'),
                                (DIRECTOR, 'Director\nPIET, Jaipur')]):
    c = t.cell(0, j); c.text = ''
    for line, bold in [('_______________________', False), (nm, True)] + \
                      [(x, False) for x in role.split('\n')]:
        pp = c.add_paragraph() if c.paragraphs[0].runs or c.paragraphs[0].text else c.paragraphs[0]
        pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pp.paragraph_format.line_spacing = 1.0
        pp.paragraph_format.space_after = Pt(0)
        _font(pp.add_run(line), 11, bold=bold)
placeholder('[SIGNATURE — to be signed and stamped before submission]')

# --- 4. declaration
pagebreak()
para('DECLARATION', 'c', 16, bold=True, before=12, after=24)
rich(DECLARATION, 'j', 12, after=12)
rich(DECLARATION2, 'j', 12, after=48)
para('Place: Jaipur', 'l', 12, after=4)
para('Date: ______________', 'l', 12, after=42)
para('_______________________', 'r', 12, after=2)
para(STUDENT.title(), 'r', 12, bold=True, after=2)
para('Registration No. ' + REGNO, 'r', 12, after=2)
para('B.Tech. Computer Engineering', 'r', 12, after=0)

# --- 5. acknowledgement
pagebreak()
para('ACKNOWLEDGEMENT', 'c', 16, bold=True, before=12, after=22)
for t_ in ACK:
    rich(t_, 'j', 12, after=10)
para('', after=30)
para('_______________________', 'r', 12, after=2)
para('Daksh Mahera', 'r', 12, bold=True, after=2)
para('Registration No. ' + REGNO, 'r', 12, after=0)

# --- 6. abstract
pagebreak()
para('ABSTRACT', 'c', 16, bold=True, before=12, after=18)
rich(ABSTRACT, 'j', 10, spacing=1.5, after=14)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.line_spacing = 1.5; p.paragraph_format.space_after = Pt(10)
_font(p.add_run('Keywords: '), 10, bold=True); _font(p.add_run(KEYWORDS), 10)
para('Subject Descriptors:', 'l', 10, bold=True, after=2)
for d in SUBJECT_DESCRIPTORS:
    para('•  ' + d, 'l', 10, spacing=1.5, left=0.35, after=2)
para('', after=6)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.line_spacing = 1.5; p.paragraph_format.space_after = Pt(8)
_font(p.add_run('Implementation Software: '), 10, bold=True); _font(p.add_run(IMPL_SW), 10)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.line_spacing = 1.5; p.paragraph_format.space_after = Pt(8)
_font(p.add_run('Implementation Hardware: '), 10, bold=True); _font(p.add_run(IMPL_HW), 10)

# --- 7. table of contents
pagebreak()
para('TABLE OF CONTENTS', 'c', 16, bold=True, before=12, after=18)
t = doc.add_table(rows=len(TOC) + 1, cols=2)
t.columns[0].width = Inches(5.3); t.columns[1].width = Inches(1.0)
hdr = [(1, 'Title', 'Page No.')]
for i, (lvl, txt, pg) in enumerate(hdr + TOC):
    for j, val in enumerate((txt, pg)):
        c = t.cell(i, j); c.text = ''
        pp = c.paragraphs[0]
        pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT if j else WD_ALIGN_PARAGRAPH.LEFT
        pp.paragraph_format.line_spacing = 1.15
        pp.paragraph_format.space_after = Pt(2)
        if j == 0 and i and TOC[i - 1][0] == 2:
            pp.paragraph_format.left_indent = Inches(0.32)
        _font(pp.add_run(str(val)), 11, bold=(i == 0 or (i and TOC[i - 1][0] <= 1)))

# --- 8. list of tables
pagebreak()
para('LIST OF TABLES', 'c', 16, bold=True, before=12, after=18)
t = doc.add_table(rows=len(LIST_TABLES) + 1, cols=3)
for i, row in enumerate([('Table No.', 'Title', 'Page No.')] + LIST_TABLES):
    for j, val in enumerate(row):
        c = t.cell(i, j); c.text = ''
        pp = c.paragraphs[0]
        pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT if j == 2 else WD_ALIGN_PARAGRAPH.LEFT
        pp.paragraph_format.line_spacing = 1.15
        pp.paragraph_format.space_after = Pt(2)
        _font(pp.add_run(str(val)), 11, bold=(i == 0))

# --- 9. list of figures
pagebreak()
para('LIST OF FIGURES', 'c', 16, bold=True, before=12, after=18)
t = doc.add_table(rows=len(LIST_FIGURES) + 1, cols=3)
for i, row in enumerate([('Figure No.', 'Title', 'Page No.')] + LIST_FIGURES):
    for j, val in enumerate(row):
        c = t.cell(i, j); c.text = ''
        pp = c.paragraphs[0]
        pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT if j == 2 else WD_ALIGN_PARAGRAPH.LEFT
        pp.paragraph_format.line_spacing = 1.15
        pp.paragraph_format.space_after = Pt(2)
        _font(pp.add_run(str(val)), 11, bold=(i == 0))

# --- 10. list of abbreviations
pagebreak()
para('LIST OF ABBREVIATIONS', 'c', 16, bold=True, before=12, after=18)
t = doc.add_table(rows=len(ABBREVIATIONS) + 1, cols=2)
t.columns[0].width = Inches(1.3)
for i, (ab, full) in enumerate([('Abbreviation', 'Expansion')] + ABBREVIATIONS):
    for j, val in enumerate((ab, full)):
        c = t.cell(i, j); c.text = ''
        pp = c.paragraphs[0]
        pp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pp.paragraph_format.line_spacing = 1.15
        pp.paragraph_format.space_after = Pt(2)
        _font(pp.add_run(str(val)), 11, bold=(i == 0))

# ================================================================ MAIN SECTION
main = doc.add_section(WD_SECTION.NEW_PAGE)
main.top_margin = main.bottom_margin = main.left_margin = main.right_margin = Inches(1)
set_numbering(main, 'decimal', 1)
main.header.is_linked_to_previous = False
main.footer.is_linked_to_previous = False

hp = main.header.paragraphs[0]
hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
hp.paragraph_format.space_after = Pt(2)
_font(hp.add_run('OKF-RAG: Mitigating Hallucination in Retrieval-Augmented Generation'), 10, italic=True)
pb = OxmlElement('w:pBdr'); bot = OxmlElement('w:bottom')
bot.set(qn('w:val'), 'single'); bot.set(qn('w:sz'), '6'); bot.set(qn('w:space'), '1')
bot.set(qn('w:color'), '808080'); pb.append(bot); hp._p.get_or_add_pPr().append(pb)

fp = main.footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
_font(fp.add_run('Department of Computer Engineering, PIET Jaipur    |    '), 10)
field(fp, 'PAGE', 10)

for blocks in (CH1, CH2, CH3, CH4, CH5, CH6, CH7):
    render(blocks)

# --- references
pagebreak()
heading1('REFERENCES')
para('References are listed alphabetically by the surname of the first author, in IEEE style, and '
     'are cited in the text by bracketed number.', 'j', 12, after=12)
for i, ref in enumerate(REFERENCES, 1):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = p.paragraph_format
    pf.line_spacing = 1.5
    pf.left_indent = Inches(0.45)
    pf.first_line_indent = Inches(-0.45)
    pf.space_after = Pt(8)
    _font(p.add_run('[%d]   ' % i), 12)
    _font(p.add_run(ref), 12)

render(APPX)

doc.save('OKF_RAG_Seminar_Report.docx')
print('saved OKF_RAG_Seminar_Report.docx')
