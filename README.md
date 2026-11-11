# Resume Design

Versioned resumes for **Hari Prasad Guntuku**, kept as two independent tracks:

| Track | Folder | Target roles | Latest | Tag |
|---|---|---|---|---|
| Data Analyst | [`data-analyst/`](data-analyst/) | Data Analyst, BI Analyst, Product/Business Analyst | [v3](data-analyst/v3/) | `data-analyst-v3` |
| AI Engineer | [`ai-engineer/`](ai-engineer/) | AI Engineer, ML Engineer, NLP / Applied ML | [v2](ai-engineer/v2/) | `ai-engineer-v2` |

## Layout

```
resume-design/
├── README.md                  ← this file (versioning rules + latest per track)
├── scripts/new_version.sh     ← cuts the next version of one track
├── data-analyst/
│   ├── CHANGELOG.md           ← what changed in each Data Analyst version
│   └── v1/
│       ├── Hari_Prasad_Guntuku_Data_Analyst_Resume_v1.docx
│       ├── Hari_Prasad_Guntuku_Data_Analyst_Resume_v1.pdf
│       └── resume.txt         ← plain-text snapshot, so versions can be diffed
└── ai-engineer/
    ├── CHANGELOG.md
    └── v1/
        ├── Hari_Prasad_Guntuku_AI_Engineer_Resume_v1.docx
        ├── Hari_Prasad_Guntuku_AI_Engineer_Resume_v1.pdf
        ├── build_resume.py    ← python-docx generator that produces the .docx
        └── resume.txt
```

## Versioning convention

1. **Each track has its own version number.** Data Analyst and AI Engineer count
   independently: `data-analyst` can be at v5 while `ai-engineer` is still at v2.
2. **Every change to a resume is a new version of that track only.** Editing the
   Data Analyst resume creates `data-analyst/v2/`, then `v3/`, and so on. The other
   track is not touched.
3. **Old versions are never edited or deleted.** Each `vN/` folder is a frozen
   snapshot of exactly what was sent out at that point, so any version can be
   re-downloaded later.
4. **Every version folder contains** the `.docx`, the `.pdf` (file names end in
   `_vN`), and a `resume.txt` text snapshot. From v2 (Data Analyst) and v1 (AI Engineer) each folder also keeps its
   `build_resume.py` generator.
5. **Every version gets a git tag** named `<track>-vN` (for example `data-analyst-v2`)
   and an entry in that track's `CHANGELOG.md`.
6. **One commit per version**, with the message `<track>: vN - <short summary>`.

### Cutting a new version

```bash
# copies the latest version of the track into the next vN folder and renames files
./scripts/new_version.sh data-analyst      # → data-analyst/v2/
# edit the .docx (or ai-engineer build_resume.py), re-export the PDF, then:
pdftotext -layout data-analyst/v2/*.pdf data-analyst/v2/resume.txt
# add a CHANGELOG entry and update the "Latest" column above, then:
git add data-analyst README.md
git commit -m "data-analyst: v2 - <what changed>"
git tag data-analyst-v2
git push origin main --tags
```

### Comparing versions

```bash
git diff data-analyst-v1 data-analyst-v2 -- data-analyst/   # what changed between tags
diff data-analyst/v1/resume.txt data-analyst/v2/resume.txt  # text-level diff
```
