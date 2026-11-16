# Data Analyst resume — changelog

Each entry is one version. Newest first. Files for each version live in `vN/`.

## v4 — 2026-11-16

Tag: `data-analyst-v4` · Folder: [`v4/`](v4/)

Applies the recruiter-style review of v3. **Not ready to send yet:** the yellow `[placeholders]`
need the real figures first (see "Open items" below). No numbers were estimated.

- Summary rewritten to lead with experience, SQL, Power BI and reporting. Uses the exact start
  date ("since March 2024") instead of a year count. Dropped the "8 case studies" claim.
- Skills split into Primary (SQL, Power BI, Excel), Secondary (Python, ETL / validation, KPI
  reporting) and Additional (Tableau, statistics, BigQuery, DuckDB, RFM / CLV, Git).
  Removed SciPy, Statsmodels, Scikit-learn and Docker from this track.
- Experience bullets rewritten around measurable outcomes, with highlighted placeholders for
  volumes, dashboard and user counts, hours saved and decisions influenced.
- Projects cut from 6 to the top 3, each as Problem / Approach / Result:
  - **New:** Global Freight Analytics Platform (SQL Server, T-SQL, pandas). Figures are the scale of
    its synthetic dataset, labelled as such: 500K shipments, 4.6M rows over 14 source files,
    6 fact tables, 16 data-quality rules, 250 planted defects caught, reconciliation within $0.16.
  - Target Brazil (SQL, BigQuery) and BI Dashboards (Power BI, Tableau) kept.
  - Customer Analytics, Walmart, Yulu and Netflix moved to a one-line "More case studies on GitHub".
- Education: added a one-line career-move note (architecture to analytics).
- Still one page.

**Open items (yellow placeholders):** Ivue figures (records per day/month, source systems,
number of teams, hours saved, dashboard count and users, report cadence and audience, one real
decision, RFM/CLV scope, data issues caught), the freight project's GitHub repo link, and the
reason for moving from architecture to analytics.

## v3 — 2026-11-11

Tag: `data-analyst-v3` · Folder: [`v3/`](v3/)

- Ivue Technologies dates are now "Mar 2024 – Present" (still employed); summary says 2+ years.
- Portfolio link is now hariprasad-data-analyst.vercel.app; contact info split over two lines.
- Every project now links to its own GitHub repo instead of a portfolio page.
- Added Customer Analytics (RFM, cohorts, CLV: 1,306 loyal customers, 75%+ of revenue) and
  BI Dashboards (7 Power BI and Tableau dashboards; supplier SLA 99.3% vs. 89.5%).
- Merged the Target Brazil bullets; Yulu now uses the case-study page's figures (4 hypotheses,
  R² 0.93, season swing up to 50%, +65% YoY). Retail Sales Forecasting moved to the AI Engineer resume only.
- Skills: added DuckDB, DAX, Power Query, Tableau LOD and parameters.

## v2 — 2026-11-11

Tag: `data-analyst-v2` · Folder: [`v2/`](v2/)

Job-ready version with no placeholders. Every number comes from the portfolio site.

- Removed all bracketed placeholders. LinkedIn is now `linkedin.com/in/dot-hpg`, and the
  portfolio `guntuku.vercel.app` was added to the header.
- Rewrote the Ivue Technologies bullets so they read complete without invented counts
  (merged the two reporting-automation bullets; 5 bullets).
- Rebuilt Projects around verified case-study results: Target Brazil (30 BigQuery queries,
  99,441 orders, +137% YoY, reviews 4.32 to 1.70), Walmart (550,068 transactions), Yulu
  (R² 0.93, -42% in rain), Netflix (8,807 titles), Retail Sales Forecasting (365 stores,
  16.8% WAPE). Added a one-line pointer to the other case studies.
- Removed the LLM Quality Analytics Dashboard and the RAG / multi-agent line, which are
  not on the portfolio site and could not be verified.
- Tightened the summary and skills (added BigQuery, Statsmodels, Bootstrap, Regression).
- Added `build_resume.py` (python-docx), matching the AI Engineer layout.
- Still one page.

## v1 — 2026-10-30

Tag: `data-analyst-v1` · Folder: [`v1/`](v1/)

- First version. One page, targeting Data Analyst / BI roles.
- Sections: Professional Summary, Technical Skills (SQL, Python, BI & Reporting,
  Statistics), Experience (Data Analyst, Ivue Technologies, Hyderabad, Mar 2024 to
  Apr 2026), Projects, Education.

**Open items carried into v1 (bracketed placeholders still to fill in):**

- LinkedIn URL is `linkedin.com/in/[your-linkedin]` (the real profile is `linkedin.com/in/dot-hpg`).
- Experience bullets have `[X]` placeholders: number of business units, number of
  dashboards, hours saved per week/month, and record volume (millions).
- Choice placeholders: `[sales / operations / finance]` stakeholders,
  `[weekly / monthly]` reporting, `[managers / business leads]`, `[retention / marketing]`.

Filling these in is the natural change for **v2**.
