# AI-Assisted Supplier Performance & Risk Monitoring

**English** | [简体中文](./README.zh-CN.md)

An end-to-end procurement analytics portfolio project that combines transparent supplier KPI scoring, machine-learning-assisted anomaly detection, and an interactive Power BI dashboard.

The project demonstrates how procurement data can be transformed into an explainable supplier risk-monitoring workflow that helps teams identify high-priority suppliers, understand major risk drivers, and support follow-up actions.

> **Portfolio note:** The purchase-order data in this project is simulated. The model is designed to prioritize supplier reviews, not to make autonomous sourcing decisions or predict supplier failure.

## Business Problem

Procurement teams often review late delivery, quality, pricing, and contract-compliance data separately.

This project brings those signals together into one supplier risk-monitoring framework to answer four practical questions:

1. Which suppliers have the highest operational risk?
2. What factors are driving each supplier's risk?
3. Which suppliers should procurement review first?
4. What actions can reduce delivery and quality risk?

## Project Workflow

1. Read and validate the synthetic purchase-order dataset.
2. Aggregate order-level records into a supplier scorecard.
3. Calculate delivery, quality, price, and contract-compliance KPIs.
4. Produce a transparent and explainable business risk score.
5. Apply Isolation Forest to flag unusual supplier performance patterns.
6. Combine the business score and anomaly signal into a final review priority.
7. Present the results in Power BI for procurement decision support.

## KPI Framework

| KPI | Business Meaning |
|---|---|
| On-time rate | Share of orders delivered on or before the promised date |
| Late rate | Share of orders delivered after the promised date |
| Average delay days | Average number of late days across a supplier's orders |
| Reject rate | Share of orders with a quality rejection |
| Price volatility | Variation in unit price over time |
| Off-contract share | Share of purchase orders placed outside contract |
| Business risk score | Weighted and explainable score based on procurement KPIs |
| Anomaly score | Isolation Forest indication of unusual KPI patterns |
| Final risk score | Combined prioritization score for supplier review |

## Key Results

- Evaluated **106 suppliers** across multiple countries and procurement categories.
- Identified **6 High Risk suppliers** using the final risk framework.
- Flagged **7 suppliers for AI-assisted review** using Isolation Forest.
- Analyzed **411.18 million** in simulated purchase spend.
- Highest-priority suppliers included **Great Wall Packaging**, **Fujikawa Resources**, and **Thames Industrial Supply**.
- The main risk drivers among the highest-risk suppliers were **late delivery and quality rejection**.

## Power BI Dashboard

![Power BI dashboard overview](images/dashboard_overview.png)

The Power BI dashboard contains:

- Risk-tier slicer
- Four KPI cards
- Top 10 suppliers by final risk score
- Supplier risk-tier distribution
- Supplier-level detail table
- Key findings and recommended procurement actions

The dashboard allows users to move from a portfolio-level view of supplier risk to more detailed supplier-level investigation.

## Recommended Procurement Actions

- Launch supplier recovery plans for the highest-risk suppliers.
- Review delivery and quality KPIs weekly until performance stabilizes.
- Validate root-cause analysis and corrective-action evidence.
- Prepare alternative sourcing options for critical items where risk concentration is high.
- Use anomaly flags as prompts for investigation rather than proof of supplier failure.

## Technology

- Python 3
- pandas
- scikit-learn
- Isolation Forest
- Power BI Desktop
- DAX
- CSV-based analytical outputs

## Project Structure

```text
ai-supplier-risk-monitoring/
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
├─ README.md
└─ README.zh-CN.md
```

## Run Locally

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

Open:

```text
dashboard/Supplier_Risk_Dashboard.pbix
```

in Power BI Desktop to explore the interactive dashboard.

## Data Source, Attribution, and Method Adaptation

The raw order-level dataset, `data/supplier_orders.csv`, is a renamed,
unmodified copy of `data/purchase_orders.csv` from
[Procurement Spend Analysis Dashboard](https://github.com/dytcoke23/procurement-spend-analysis-dashboard),
created by Harsh (`dytcoke23`) and distributed under the MIT License.

The source dataset is seeded synthetic data and does not contain real company,
supplier, or confidential procurement information.

This project uses the source dataset as its analytical input and generates two
derived datasets:

- `data/supplier_scorecard.csv`: supplier-level KPI aggregation and business
  risk scores
- `data/supplier_risk_final.csv`: final results combining business risk scores
  with Isolation Forest anomaly signals

The supplier KPI framework, risk caps and weights, and the
`StandardScaler + IsolationForest` approach were adapted from the same
open-source project. This implementation modifies the analytical workflow,
uses a 70% business-score and 30% anomaly-score blend, applies a 6% anomaly
contamination setting, and presents the results in a newly built Power BI
dashboard.

The original copyright and MIT permission notice are preserved in
[THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).

## Risk Governance and Limitations

- The dataset is simulated and does not contain confidential supplier information.
- KPI weights and risk thresholds are business rules and should be calibrated with procurement stakeholders before real-world use.
- Isolation Forest detects unusual performance patterns; it does not explain root causes or confirm supplier failure.
- Suppliers with few purchase orders may have unstable rates and should be reviewed with sample size in mind.
- Currency is intentionally unspecified, so spend values should not be interpreted as the financial data of a real company.
- Final sourcing and supplier-management decisions require human review and supporting operational evidence.

## Portfolio Deliverables

- Interactive Power BI dashboard: `dashboard/Supplier_Risk_Dashboard.pbix`
- Exported dashboard PDF: `report/Supplier_Risk_Dashboard.pdf`
- Full project report: `report/AI_Supplier_Risk_Project_Report.docx`
- Markdown project report: `report/AI_Supplier_Risk_Project_Report.md`
- Resume and interview notes: `report/resume_and_interview_notes.md`

## Contact

If you have any questions, suggestions, or ideas for collaboration, feel free to contact me.

- Email: [peiyuan856@gmail.com](mailto:peiyuan856@gmail.com)
- GitHub: [@peiyuan856-hue](https://github.com/peiyuan856-hue)
