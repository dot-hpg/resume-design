"""Builds Hari_Prasad_Guntuku_Cover_Letter_v2.docx (python-docx).

v2 keeps the layout and voice of v1 (the user's own letter) and aligns the
content with data-analyst resume v5. Only facts from that resume are used.
PDF: soffice --headless --convert-to pdf <docx>
"""
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Hari_Prasad_Guntuku_Cover_Letter_v2.docx")
FONT = "Arial"
NAVY = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x55, 0x5F, 0x6B)
TEXT = RGBColor(0x22, 0x22, 0x22)

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
sec.left_margin = sec.right_margin = Inches(1.0)
sec.top_margin = Inches(0.8)
sec.bottom_margin = Inches(0.8)
normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = Pt(10.5)
normal.font.color.rgb = TEXT
normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)


def para(text="", size=None, bold=False, color=None, after=10, align=None, line=1.25):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before, pf.space_after, pf.line_spacing = Pt(0), Pt(after), line
    if align is not None:
        p.alignment = align
    if text:
        r = p.add_run(text)
        r.bold = bold
        if size:
            r.font.size = Pt(size)
        if color:
            r.font.color.rgb = color
    return p


def border(p, side, color="C9D6E3", sz="6", space="6"):
    pPr = p._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    el = OxmlElement(f"w:{side}")
    for k, v in {"w:val": "single", "w:sz": sz, "w:space": space, "w:color": color}.items():
        el.set(qn(k), v)
    bdr.append(el)
    pPr.append(bdr)


# Header (same as v1: left-aligned name, grey contact lines)
para("HARI PRASAD GUNTUKU", size=18, bold=True, color=NAVY, after=2, line=1.0)
para("Hyderabad, India  |  +91 8555081508  |  connect.hpg@gmail.com",
     size=8.5, color=GREY, after=1, line=1.0)
para("LinkedIn: linkedin.com/in/dot-hpg  |  Portfolio: hariprasad-data-analyst.vercel.app  |  "
     "GitHub: github.com/dot-hpg", size=8.5, color=GREY, after=18, line=1.0)

para("Dear Hiring Manager,", after=10)

BODY = [
    "I am writing to express my interest in a Data Analyst role where I can apply my experience in "
    "SQL, Power BI and business reporting. I am a Data Analyst at Ivue Technologies, where I have "
    "worked since March 2024, and I focus on turning messy data into decisions people trust: I build "
    "the SQL and Python pipelines behind recurring business reports, the Power BI dashboards teams "
    "use to track their KPIs, and the validation checks that keep every number consistent with its "
    "source.",

    "In my current role, I automate data extraction, cleaning and transformation with SQL (joins, "
    "CTEs, window functions) and Python ETL pipelines, replacing manual spreadsheet pulls so "
    "recurring reports are consistent and on schedule. I design and maintain Power BI dashboards and "
    "KPI reports, and agree requirements, metric definitions and refresh schedules with stakeholders "
    "so every team works from the same numbers. I have also developed RFM segmentation and customer "
    "lifetime value (CLV) models that identify high-value customer groups and guide retention and "
    "marketing, and I run reconciliation checks so source systems, reports and dashboards match "
    "before results reach stakeholders.",

    "My portfolio shows the same focus on data quality at a larger scale. For a Global Freight "
    "Analytics Platform, I designed a SQL Server ETL pipeline that brings data from five systems into "
    "a dimensional model with six fact tables, using T-SQL stored procedures and 16 data-quality "
    "rules. On a 500,000-shipment synthetic dataset, the quality gate quarantined all 250 planted "
    "defects, and revenue reconciled between source and warehouse to within $0.16. In a separate "
    "analysis, I wrote 30 BigQuery SQL queries over 99,441 Target Brazil e-commerce orders and showed "
    "that very late deliveries cut review scores from 4.32 to 1.70, while same-state orders arrived "
    "twice as fast with 43% lower freight.",

    "My core toolkit is SQL (MySQL, PostgreSQL, SQL Server / T-SQL), Power BI (DAX, Power Query, data "
    "modeling) and Excel, supported by Python (Pandas, NumPy), Tableau and statistics such as "
    "hypothesis testing, A/B testing and regression. My background in architecture taught me to think "
    "in systems and to design for the person who will use the result, which is how I approach every "
    "dashboard and report. I am also pursuing an M.S. in Computer Science (AI & ML) through Woolf "
    "University.",

    "I would welcome the opportunity to discuss how my experience and skills could contribute to your "
    "team. Thank you for your time and consideration.",
]
for text in BODY:
    para(text, after=10)

para("Sincerely,", after=2)
para("Hari Prasad Guntuku", bold=True, after=0)

# Footer (same as v1: thin rule, right-aligned label)
fp = sec.footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
border(fp, "top", space="4")
r = fp.add_run("Hari Prasad Guntuku | Cover Letter")
r.font.size, r.font.color.rgb, r.font.name = Pt(7.5), GREY, FONT

doc.save(OUT)
print("wrote", OUT)
