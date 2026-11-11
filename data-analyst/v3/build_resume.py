import sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_TAB_ALIGNMENT, WD_ALIGN_PARAGRAPH
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

# ---------- Header ----------
p = para(align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "HARI PRASAD GUNTUKU", bold=True, size=20, color=ACCENT)
p = para(space_before=1, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "Data Analyst  |  SQL  |  Python  |  Power BI  |  Tableau  |  Excel  |  Statistics", bold=True, size=10.5)
p = para(space_before=2, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "Hyderabad, India  |  +91 8555081508  |  connect.hpg@gmail.com", size=9)
p = para(space_before=0.5, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "linkedin.com/in/dot-hpg  |  github.com/dot-hpg  |  Portfolio: hariprasad-data-analyst.vercel.app", size=9)

# ---------- Summary ----------
heading("Professional Summary")
p = para()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
run(p, "Data Analyst with 2+ years of industry experience building the SQL and Python pipelines, Power BI dashboards and "
       "validation checks business teams use to track KPIs. Strong in advanced SQL (CTEs, window functions, BigQuery), "
       "statistics (hypothesis and A/B testing, confidence intervals, regression) and customer analytics (RFM, CLV), ending "
       "every analysis in a clear recommendation. Completed 8 analytics case studies on up to 550K records; pursuing an M.S. in Computer Science (AI & ML).")

# ---------- Skills ----------
heading("Technical Skills")
skills = [
    ("SQL: ", "PostgreSQL, MySQL, BigQuery, DuckDB, Joins, CTEs, Window Functions, Subqueries, Aggregations, Data Modeling"),
    ("Python: ", "Pandas, NumPy, SciPy, Statsmodels, Scikit-learn, Matplotlib, Seaborn, Jupyter"),
    ("BI & Reporting: ", "Power BI (DAX, Power Query, Data Modeling), Tableau (LOD, Parameters), Excel (Pivot Tables, XLOOKUP)"),
    ("Statistics: ", "EDA, Hypothesis Testing (t-test, ANOVA, Chi-Square), A/B Testing, Confidence Intervals, Bootstrap, Regression"),
    ("Analytics & Tools: ", "Customer Segmentation, RFM / CLV, Cohort Analysis, Forecasting, ETL, Data Validation, Git, Docker"),
]
for k, v in skills:
    p = para(space_after=0.5)
    run(p, k, bold=True)
    run(p, v)

# ---------- Experience ----------
heading("Professional Experience")
line_with_right([("Data Analyst", B), ("  |  Ivue Technologies Pvt. Ltd., Hyderabad", {})], "Mar 2024 – Present")
for b in [
    "Built and automated SQL and Python data pipelines (joins, CTEs, window functions) to extract, transform and report data "
    "for multiple business units, replacing manual spreadsheet pulls and making recurring reports consistent and on time.",
    "Designed and maintained Power BI dashboards and KPI reports, working with business stakeholders to define requirements, "
    "metric definitions and refresh schedules so every team read the same numbers.",
    "Analyzed large operational and customer datasets in Python and Excel to surface behavior patterns and business "
    "opportunities, and presented findings and recommendations to business leads.",
    "Built RFM segmentation and customer lifetime value (CLV) models to identify high-value customer groups, informing "
    "targeted retention and marketing strategies.",
    "Added validation and reconciliation checks across pipelines so source data, reports and dashboards always matched.",
]:
    bullet(b)

# ---------- Projects ----------
heading("Data Analytics Projects")

def proj(title, stack, link, bullets, first=False):
    line_with_right([(title, B), ("  |  " + stack, G)], link, space_before=0 if first else 2.5)
    for b in bullets:
        bullet(b)

proj("Target Brazil: E-Commerce Operations Analysis", "SQL, BigQuery, Python",
     "github.com/dot-hpg/target-brazil-sql-case-study", [
         "Wrote 30 BigQuery SQL queries over 99,441 orders across six deep-dives: order value grew 137% year over year, very late "
         "deliveries cut review scores from 4.32 to 1.70, and same-state orders arrived 2x faster with 43% lower freight.",
     ], first=True)

proj("Customer Analytics: RFM, Cohorts & CLV", "Python, Pandas, Segmentation",
     "github.com/dot-hpg/crm-analytics-python", [
         "Segmented customers with RFM scoring, cohort retention and CLV; identified 1,306 loyal customers driving 75%+ of "
         "revenue and pinpointed Month 2 as the point where retention drops sharply.",
     ])

proj("Walmart: Black Friday Spending Analysis", "Python, CLT, Bootstrap, Tableau",
     "github.com/dot-hpg/walmart-black-friday-clt-analysis", [
         "Analyzed 550,068 transactions with the Central Limit Theorem, confidence intervals and bootstrapping; men spent ~8% "
         "more per transaction, but product mix explained 100% of the gap, shifting targeting from gender to category.",
     ])

proj("Yulu: What Drives E-Cycle Demand", "t-test, ANOVA, Chi-Square, Regression",
     "github.com/dot-hpg/yulu-hypothesis-testing", [
         "Tested 4 hypotheses on 10,886 hourly rental records; regression explained demand with R² 0.93, season swung demand "
         "by up to 50%, demand grew 65% year over year, and ~81% of rides came from registered users.",
     ])

proj("Netflix: Content Strategy Analysis", "Python, Pandas, Seaborn",
     "github.com/dot-hpg/netflix-content-insights", [
         "Explored 8,807 titles across 23 charts: TV's share of new additions rose from 25% to 34% (2018–2021) and 67% of "
         "shows ran a single season; delivered ten content-strategy recommendations.",
     ])

proj("BI Dashboards", "Power BI, DAX, Power Query, Tableau",
     "github.com/dot-hpg/power-BI-projects-data-analysis", [
         "Built 7 Power BI and Tableau dashboards, including Supplier Performance & SLA (tracking 99.3% SLA compliance for "
         "consumables vs. 89.5% for uniforms), Audit Efficiency & Effectiveness, and Education Data Insights.",
     ])

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
