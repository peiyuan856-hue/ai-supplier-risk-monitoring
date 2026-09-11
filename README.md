# AI-Assisted Supplier Performance & Risk Monitoring

An end-to-end procurement analytics portfolio project that combines transparent supplier KPI scoring, machine-learning-assisted anomaly detection, and an interactive Power BI dashboard.

> Portfolio note: the purchase-order data in this project is simulated. The model is designed to prioritize supplier reviews, not to make autonomous sourcing decisions or predict supplier failure.

## Business problem

Procurement teams often review late delivery, quality, pricing, and contract-compliance data separately. This project brings those signals together to answer four practical questions:

1. Which suppliers have the highest operational risk?
2. What factors are driving each supplier's risk?
3. Which suppliers should procurement review first?
4. What actions can reduce delivery and quality risk?

## Project workflow

1. Read and validate historical purchase-order data.
2. Aggregate order-level records into a supplier scorecard.
3. Calculate delivery, quality, price, and contract-compliance KPIs.
4. Produce a transparent business risk score.
5. Apply Isolation Forest to flag unusual supplier performance patterns.
6. Combine the business score and anomaly signal into a final review priority.
7. Present the results in Power BI for procurement decision support.

## KPI framework

| KPI | Business meaning |
|---|---|
| On-time rate | Share of orders delivered on or before the promised date |
| Late rate | Share of orders delivered after the promised date |
| Average delay days | Average number of late days across a supplier's orders |
| Reject rate | Share of orders with a quality rejection |
| Price volatility | Variation in unit price over time |
| Off-contract share | Share of purchase orders placed outside contract |
| Business risk score | Weighted, explainable score based on procurement KPIs |
| Anomaly score | Isolation Forest indication of unusual KPI patterns |
| Final risk score | Combined prioritization score for supplier review |

## Key results

- Evaluated **106 suppliers** across multiple countries and procurement categories.
- Identified **6 High Risk suppliers** using the final risk framework.
- Flagged **7 suppliers for AI-assisted review** using Isolation Forest.
- Analyzed **411.18 million** in simulated purchase spend.
- Highest-priority suppliers: **Great Wall Packaging**, **Fujikawa Resources**, and **Thames Industrial Supply**.
- Main risk drivers in the highest-risk group were late delivery and quality rejection.

## Dashboard

![Power BI dashboard overview](images/dashboard_overview.png)

The Power BI page contains:

- Risk-tier slicer
- Four KPI cards
- Top 10 suppliers by final risk score
- Supplier risk-tier distribution
- Supplier-level detail table
- Key findings and recommended procurement actions

## Recommended actions

- Launch supplier recovery plans for the highest-risk suppliers.
- Review delivery and quality KPIs weekly until performance stabilizes.
- Validate root-cause analysis and corrective-action evidence.
- Prepare alternative sourcing for critical items where risk concentration is high.
- Use anomaly flags as a prompt for investigation, not as proof of supplier failure.

## Technology

- Python 3
- pandas
- scikit-learn (Isolation Forest)
- Power BI Desktop
- DAX
- CSV-based analytical outputs

## Project structure

```text
supplier-risk-project/
├─ dashboard/
│  └─ Supplier_Risk_Dashboard.pbix
├─ data/
│  ├─ supplier_orders.csv
│  ├─ supplier_scorecard.csv
│  └─ supplier_risk_final.csv
├─ images/
│  └─ dashboard_overview.png
├─ report/
│  ├─ Supplier_Risk_Dashboard.pdf
│  ├─ AI_Supplier_Risk_Project_Report.docx
│  ├─ AI_Supplier_Risk_Project_Report.md
│  └─ resume_and_interview_notes.md
├─ src/
│  ├─ read_data.py
│  ├─ analyze_suppliers.py
│  └─ ai_anomaly.py
├─ requirements.txt
└─ README.md
```

## Run locally

From the project root:

```powershell
python -m pip install -r requirements.txt
python src/read_data.py
python src/analyze_suppliers.py
python src/ai_anomaly.py
```

Expected outputs:

- `data/supplier_scorecard.csv`
- `data/supplier_risk_final.csv`

Open `dashboard/Supplier_Risk_Dashboard.pbix` in Power BI Desktop to explore the dashboard.

## Risk governance and limitations

- The dataset is simulated and does not contain confidential supplier information.
- KPI weights and risk thresholds are business rules and should be calibrated with procurement stakeholders.
- Isolation Forest detects unusual patterns; it does not explain root cause or confirm supplier failure.
- Suppliers with few purchase orders may have unstable rates and should be reviewed with sample size in mind.
- Currency is intentionally unspecified; spend values should not be interpreted as a real company's financial data.
- Final sourcing decisions require human review and supporting operational evidence.

## Portfolio deliverables

- Interactive Power BI file: `dashboard/Supplier_Risk_Dashboard.pbix`
- Exported dashboard PDF: `report/Supplier_Risk_Dashboard.pdf`
- Project report: `report/AI_Supplier_Risk_Project_Report.docx`
- Resume and interview notes: `report/resume_and_interview_notes.md`

