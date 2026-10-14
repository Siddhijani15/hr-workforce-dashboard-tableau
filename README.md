# HR Workforce Dashboard — Tableau

An interactive Tableau Public dashboard that answers 12 workforce questions for **XYZ Corporation** (22,211 employees, 2000–2020): hiring, attrition, location, tenure, organisation structure and diversity.

🔗 **Live dashboard:** https://public.tableau.com/app/profile/siddhi.jani6174/viz/HRworkspacedashboard/HRDashboard


---

## Questions answered

| # | Question | Answer |
|---|---|---|
| 1 | Total employees hired to date | 22,211 |
| 2 | Active vs non-active | 90.5% active (20,091) · 9.5% terminated (2,120) |
| 3 | Remote vs HQ | 75.3% HQ · 24.7% Remote |
| 4 | Average / median age | 38.2 / 38 |
| 5 | Average tenure | 10.9 years |
| 6 | Number of departments | 13 |
| 7 | Employees by department and job title | Engineering largest (6,686, 87 titles) |
| 8 | Employees by state | Ohio 18,024; all other states remote-only |
| 9 | Hiring trend by month and gender | ~1,050–1,150 hires a year, steady |
| 10 | Age diversity | Even spread across 20–54 |
| 11 | Gender diversity | Male 50.8% · Female 46.5% · Non-Conforming 2.7% |
| 12 | Race and gender diversity | White largest (28.5%); ~52/48 M/F split in every group |

## Tools

- **Tableau Desktop / Tableau Public**: calculated fields, dual-axis charts, containers, filter actions
- **Python (pandas)**: data audit before building ([`data_audit.py`](data_audit.py))

## Data cleaning

| Issue | What I did |
|---|---|
| Two status fields disagreed: 1,809 "Active" employees had a future termination date | Used `Employment Status` as the source of truth; added a **Scheduled to Leave** KPI |
| 16 leftover columns from an earlier workbook | Hidden in the data source |
| Dates stored as text (`dd-mm-yyyy hh:mm:ss`) | Converted to Date & Time |
| Typos in column names | Renamed `Employement Status`, `Jobtitle`, `Age (bin)` |
| Personal fields (names, birthdates) | Removed from the published workbook with *Hide All Unused Fields* |

## Key calculated fields

```
Total Employees     = COUNTD([Id])
Active Employees    = COUNTD(IF [Employment Status] = "Active" THEN [Id] END)
% Active            = [Active Employees] / [Total Employees]
% Remote            = COUNTD(IF [Location] = "Remote" THEN [Id] END) / [Total Employees]
Scheduled to Leave  = COUNTD(IF [Employment Status] = "Active" AND NOT ISNULL([Termdate]) THEN [Id] END)
```

## Dashboard features

- 8 KPI cards
- Hiring trend line by gender
- Donut charts (dual-axis `MIN(0)` technique) for gender and HQ vs Remote
- Department → job title drill-down
- 7 dropdown filters applied to all worksheets
- Click-to-filter actions: click any department, state, gender or race to filter the whole dashboard

## Key insights

- **90.5% retention**, but 1,809 departures are already scheduled; counting them almost doubles attrition.
- **75% of staff work at HQ** in Ohio; everyone outside Ohio is remote.
- **Engineering is 30%** of the workforce.
- Leavers stayed **7.1 years** on average vs **11.3** for current staff.

## Repository contents

```
├── README.md
├── data_audit.py            # Python checks used to validate the data
├── HR_Dashboard.twbx        # Tableau packaged workbook
└── images/
    └── dashboard.png        # Dashboard screenshot
```

## Author

**Siddhi Jani**, Data Analyst · Melbourne
[LinkedIn](PASTE_YOUR_LINKEDIN_URL_HERE)
