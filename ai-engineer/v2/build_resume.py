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
cp.title = "Hari Prasad Guntuku - AI / ML Engineer Resume"
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

# ---------- Header ----------
p = para(align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "HARI PRASAD GUNTUKU", bold=True, size=20, color=ACCENT)
p = para(space_before=1, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "AI / ML Engineer  |  NLP  |  Embeddings  |  Time-Series Forecasting  |  Python", bold=True, size=10.5)
p = para(space_before=2, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "Hyderabad, India  |  +91 8555081508  |  connect.hpg@gmail.com", size=9)
p = para(space_before=0.5, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, "linkedin.com/in/dot-hpg  |  github.com/dot-hpg  |  Portfolio: hariprasad-ai-engineer.vercel.app", size=9)

# ---------- Summary ----------
heading("Professional Summary")
p = para()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
run(p, "AI/ML engineer with 2+ years of industry experience as a Data Analyst (SQL and Python pipelines, data validation, Power BI), "
       "now building end-to-end ML systems in NLP, embeddings and forecasting. Takes models from notebook to tested, deployed "
       "product: fine-tuned BERT for tweet NER (3.2x a BiLSTM baseline), a LightGBM forecaster for 365 stores (16.8% daily WAPE), "
       "and an on-device embedding app with ~97% test coverage. Pursuing an M.S. in Computer Science (AI & ML).")

# ---------- Skills ----------
heading("Technical Skills")
skills = [
    ("ML & NLP: ", "BERT fine-tuning, BiLSTM-CRF, Sentence Embeddings, TF-IDF, NLTK, Scikit-learn, TensorFlow, LightGBM, XGBoost, SHAP"),
    ("Modeling & Statistics: ", "Time-Series Forecasting, Rolling-Origin Validation, Regression, Hypothesis Testing, Bootstrap, ROC AUC"),
    ("Deployment & MLOps: ", "FastAPI, Flask, Streamlit, Docker, Kubernetes, ONNX Runtime Web, Transformers.js, GitHub Actions CI/CD"),
    ("Languages & Data: ", "Python, SQL (PostgreSQL, MySQL, BigQuery), TypeScript, React, Pandas, NumPy, Power BI, Tableau"),
]
for k, v in skills:
    p = para(space_after=0.5)
    run(p, k, bold=True)
    run(p, v)

# ---------- Experience ----------
heading("Professional Experience")
line_with_right([("Data Analyst", B), ("  |  Ivue Technologies Pvt. Ltd., Hyderabad", {})], "Mar 2024 – Present")
for b in [
    "Built and automated SQL and Python data pipelines (joins, CTEs, window functions) for extraction, transformation and "
    "reporting across multiple business units, with validation checks keeping reports consistent with source data.",
    "Automated recurring reporting and developed Power BI dashboards and KPI reports, working with stakeholders to define "
    "requirements, metric logic and refresh cadence.",
    "Analyzed large operational and customer datasets with Python and Excel; built RFM segmentation and customer "
    "lifetime value (CLV) models to identify high-value customer groups.",
]:
    bullet(b)

# ---------- AI / ML Projects ----------
heading("AI / ML Projects")

def proj(title, stack, link, bullets, first=False):
    line_with_right([(title, B), ("  |  " + stack, {"italic": True, "color": GREY, "size": 9.5})], link,
                    space_before=0 if first else 2.5)
    for b in bullets:
        bullet(b)

proj("FitCheck: On-Device AI Resume Matcher", "Transformers.js, ONNX, React, TypeScript",
     "github.com/dot-hpg/fitcheck", [
         "Shipped a private resume-to-job matcher running the all-MiniLM-L6-v2 embedding model (~23 MB quantized ONNX) fully "
         "in the browser via a Web Worker, with an explainable 100-point score and skill-gap analysis over 350+ skill aliases.",
         "Reached ~97% unit-test coverage of the matching engine plus Playwright end-to-end tests (including offline real-model "
         "runs); GitHub Actions lints, type-checks, tests, builds and deploys on every push.",
     ], first=True)

proj("Twitter Named Entity Recognition", "BERT, TensorFlow, FastAPI, Docker, Kubernetes",
     "github.com/dot-hpg/twitter-ner", [
         "Ran 17 controlled experiments on WNUT-16 comparing BiLSTM-CRF with fine-tuned BERT for entity extraction from noisy "
         "tweets; fine-tuned BERT reached test F1 0.437, 3.2x the LSTM baseline.",
         "Served the best model as a containerized FastAPI service and published a technical write-up on Medium.",
     ])

proj("Retail Sales Forecasting", "LightGBM, XGBoost, SHAP, Flask, Streamlit",
     "github.com/dot-hpg/sales-forecasting", [
         "Forecast daily sales 61 days ahead for 365 stores; compared 10 models and tested 8 hypotheses using leakage-free "
         "features and rolling-origin validation.",
         "Global LightGBM hit 16.8% daily WAPE on a 61-day hold-out (~90% accurate at store-month level) and measured a +33% "
         "discount sales lift; explained with SHAP, served via Flask API and Streamlit.",
     ])

proj("FlipItNews: News Classification", "Scikit-learn, NLTK, TF-IDF, FastAPI",
     "github.com/dot-hpg/flipitnews-news-classification", [
         "Compared 12 model and vectorizer pairs with cross-validation and leakage checks; Logistic Regression reached 98.0% "
         "test accuracy, rising to 99.8% by routing low-confidence articles to an editor; served via FastAPI in Docker.",
     ])

# ---------- Analytics case studies ----------
heading("Data Science Case Studies")
cases = [
    ("Target Brazil (SQL, BigQuery): ", "99,441 orders; +137% YoY order value; very late deliveries cut reviews from 4.32 to 1.70."),
    ("LoanTap Credit Risk (Logistic Regression, SMOTE): ", "396,030 loans, 0.70 ROC AUC; 81% accuracy masked just 7% defaulter recall."),
    ("Walmart Black Friday (CLT, Bootstrap): ", "550,068 transactions; traced the ~8% gender spending gap to product mix."),
]
for k, v in cases:
    bullet([(k, B), (v, {})])
p = para(space_before=0.5)
p.paragraph_format.left_indent = Inches(0.05)
run(p, "8 more case studies (Yulu, Delhivery, Netflix, Aerofit, Jamboree and others) on github.com/dot-hpg",
    italic=True, color=GREY, size=9.5)

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
