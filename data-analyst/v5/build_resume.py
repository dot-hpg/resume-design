import sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_TAB_ALIGNMENT, WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
import re
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = sys.argv[1]
FONT = "Calibri"
BASE = 10
ACCENT = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x44, 0x44, 0x44)

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
sec.left_margin = sec.right_margin = Inches(0.55)
sec.top_margin = Inches(0.45)
sec.bottom_margin = Inches(0.4)
RIGHT = sec.page_width - sec.left_margin - sec.right_margin

st = doc.styles["Normal"]
st.font.name = FONT
st.font.size = Pt(BASE)
st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
st.paragraph_format.space_after = Pt(0)
st.paragraph_format.space_before = Pt(0)
st.paragraph_format.line_spacing = 1.0

cp = doc.core_properties
cp.title = "Hari Prasad Guntuku - Data Analyst Resume"
cp.author = "Hari Prasad Guntuku"


def run(p, text, bold=False, italic=False, size=None, color=None):
    # Text in [square brackets] is a placeholder for a real figure: highlight it yellow.
    pieces = [t for t in re.split(r"(\[[^\]]+\])", text) if t]
    if len(pieces) > 1 or (pieces and pieces[0].startswith("[")):
        for t in pieces:
            r = run_one(p, t, bold, italic, size, color)
            if t.startswith("["):
                r.font.highlight_color = WD_COLOR_INDEX.YELLOW
        return r
    return run_one(p, text, bold, italic, size, color)


def run_one(p, text, bold=False, italic=False, size=None, color=None):
    r = p.add_run(text)
    r.bold, r.italic = bold, italic
    r.font.name = FONT
    if size:
        r.font.size = Pt(size)
    if color:
        r.font.color.rgb = color
    return r


def para(space_before=0, space_after=0, align=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before, pf.space_after = Pt(space_before), Pt(space_after)
    if align is not None:
        p.alignment = align
    return p


def bottom_border(p):
    pPr = p._p.get_or_add_pPr()
    b = OxmlElement("w:pBdr")
    e = OxmlElement("w:bottom")
    for k, v in (("val", "single"), ("sz", "6"), ("space", "1"), ("color", "1F3A5F")):
        e.set(qn("w:" + k), v)
    b.append(e)
    pPr.append(b)


def heading(text):
    p = para(space_before=6, space_after=2.5)
    run(p, text.upper(), bold=True, size=10.5, color=ACCENT)
    bottom_border(p)
    p.paragraph_format.keep_with_next = True


def line_with_right(left_parts, right_text, space_before=0):
    p = para(space_before=space_before)
    p.paragraph_format.tab_stops.add_tab_stop(RIGHT, WD_TAB_ALIGNMENT.RIGHT)
    p.paragraph_format.keep_with_next = True
    for t, kw in left_parts:
        run(p, t, **kw)
    if right_text:
        run(p, "\t" + right_text, color=GREY, size=9.5)
    return p


def bullet(parts):
    p = para()
    pf = p.paragraph_format
    pf.left_indent = Inches(0.17)
    pf.first_line_indent = Inches(-0.12)
    pf.space_after = Pt(0.5)
    run(p, "•  ")
    if isinstance(parts, str):
        parts = [(parts, {})]
    for t, kw in parts:
        run(p, t, **kw)
    return p


B = {"bold": True}
G = {"italic": True, "color": GREY, "size": 9.5}

B = {"bold": True}
G = {"italic": True, "color": GREY, "size": 9.5}

# ---------- Header ----------
p = para(align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "HARI PRASAD GUNTUKU", bold=True, size=20, color=ACCENT)
p = para(space_before=1, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "Data Analyst  |  SQL  |  Power BI  |  Excel  |  Business Reporting  |  Python", bold=True, size=10.5)
p = para(space_before=2, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "Hyderabad, India  |  +91 8555081508  |  connect.hpg@gmail.com", size=9)
p = para(space_before=0.5, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "linkedin.com/in/dot-hpg  |  github.com/dot-hpg  |  Portfolio: hariprasad-data-analyst.vercel.app", size=9)

# ---------- Summary ----------
# Leads with the five things the review asked for: experience, SQL, Power BI, reporting, impact.
heading("Professional Summary")
p = para()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
run(p, "Data Analyst who turns messy data into decisions people trust. ", bold=True)
run(p, "At Ivue Technologies since March 2024: write SQL on MySQL and PostgreSQL (CTEs, window functions) for recurring "
       "business reports, build Python ETL pipelines, RFM and CLV customer segments, and the Power BI and Tableau "
       "dashboards teams use to track KPIs, with validation checks so every report matches its source. Trained as an "
       "architect, so I think in systems and design for the person using the result. Pursuing an M.S. in "
       "CS (AI & ML); recently shipped FitCheck, an open-source resume-to-job matcher that runs in the browser.")

# ---------- Skills ----------
# Split by priority, as the review asked. Primary = daily tools for the target roles.
heading("Skills")
skills = [
    ("Primary: ", "SQL (MySQL, PostgreSQL, SQL Server / T-SQL; CTEs, window functions, stored procedures)  |  "
                  "Power BI (DAX, Power Query, data modeling)  |  Excel (pivots, XLOOKUP)"),
    ("Secondary: ", "Python (Pandas, NumPy, Matplotlib, Seaborn, Jupyter)  |  ETL and data validation  |  KPI reporting"),
    ("Additional: ", "Tableau  |  Statistics (hypothesis and A/B testing, regression)  |  BigQuery, DuckDB  |  RFM / CLV  |  Git"),
]
for k, v in skills:
    p = para(space_after=0.5)
    run(p, k, bold=True)
    run(p, v)

# ---------- Experience ----------
# No figures here until real ones are available. Never estimate. ([Bracketed] text would be highlighted yellow.)
heading("Professional Experience")
line_with_right([("Data Analyst", B), ("  |  Ivue Technologies Pvt. Ltd., Hyderabad", {})], "Mar 2024 – Present")
for b in [
    "Write and automate SQL (joins, CTEs, window functions) and Python pipelines that extract, clean and transform data "
    "for recurring business reports, replacing manual spreadsheet pulls so reports go out consistent and on schedule.",
    "Build and maintain Power BI dashboards and KPI reports for business stakeholders; agree requirements, metric "
    "definitions and refresh schedules with them so every team reads the same numbers.",
    "Analyze operational and customer data in SQL, Python and Excel to find trends and opportunities, and present "
    "findings and recommendations to business leads.",
    "Built RFM segmentation and customer lifetime value (CLV) models to identify high-value customer groups, informing "
    "targeted retention and marketing strategies.",
    "Added validation and reconciliation checks across pipelines so source data, reports and dashboards match before "
    "anything reaches stakeholders.",
]:
    bullet(b)

# ---------- Projects ----------
# Top 3 only, each as problem, approach, result. The rest are named in one line and live on GitHub.
heading("Selected Projects")

def proj(title, stack, link, problem, approach, result, first=False):
    line_with_right([(title, B), ("  |  " + stack, G)], link, space_before=0 if first else 3)
    for label, text in (("Problem: ", problem), ("Approach: ", approach), ("Result: ", result)):
        bullet([(label, B), (text, {})])

proj("Global Freight Analytics Platform", "SQL Server, T-SQL, Python, Pandas",
     "github.com/dot-hpg",
     "Freight data sat in 5 systems (bookings, billing, screening, claims, capacity) with no single trusted source.",
     "Built a SQL Server lake-to-warehouse pipeline: T-SQL stored procedures load conformed dimensions and 6 fact "
     "tables, convert charges to USD, quarantine bad rows, then run 16 data-quality rules; pandas re-checks the totals.",
     "On a 500K-shipment synthetic dataset (4.6M rows, 14 source files), the quality gate caught all 250 planted "
     "defects, and row counts and USD revenue reconciled between files and warehouse to within $0.16.",
     first=True)

proj("Target Brazil: E-Commerce Operations Analysis", "SQL, BigQuery",
     "github.com/dot-hpg/target-brazil-sql-case-study",
     "Find what drove order growth, delivery delays and poor reviews for Target's Brazil e-commerce business.",
     "Wrote 30 BigQuery SQL queries (joins, CTEs, window functions) over 99,441 orders in six deep-dives.",
     "Order value grew 137% year over year; very late deliveries cut review scores from 4.32 to 1.70; same-state "
     "orders arrived 2x faster with 43% lower freight.")

proj("BI Dashboards", "Power BI, DAX, Power Query, Tableau",
     "github.com/dot-hpg/power-BI-projects-data-analysis",
     "Turn raw operational data into dashboards that managers can read at a glance.",
     "Built 7 Power BI and Tableau dashboards with DAX measures, Power Query cleaning and data modeling.",
     "Supplier Performance & SLA dashboard tracks 99.3% SLA compliance for consumables vs. 89.5% for uniforms; "
     "others cover audit efficiency and education data.")

p = para(space_before=3)
run(p, "More case studies on GitHub: ", bold=True)
run(p, "Customer Analytics (RFM, cohorts, CLV)  |  Walmart Black Friday (CLT, bootstrap)  |  "
       "Yulu demand (hypothesis testing, regression)  |  Netflix content strategy (EDA)")

# ---------- Education ----------
heading("Education")
for deg, school in [
    ("M.S. in Computer Science (AI & ML)", "Woolf University, via Scaler Neovarsity"),
    ("Advanced Data Science & Machine Learning Program", "Scaler Academy"),
    ("Bachelor of Architecture (B.Arch), First Class", "School of Planning and Architecture, New Delhi"),
]:
    right = "In Progress" if "Bachelor" not in deg else ""
    line_with_right([(deg, B), ("  |  " + school, {})], right)
p = para(space_before=1.5)
run(p, "Certifications: ", bold=True)
run(p, "HackerRank SQL (Intermediate, Basics)  |  NSDC: Python Libraries, SQL, EDA Fundamentals")

doc.save(OUT)
print("saved", OUT)
