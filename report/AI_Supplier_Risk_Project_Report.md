# AI-Assisted Supplier Performance & Risk Monitoring

## Executive summary

This project demonstrates how a procurement team can combine supplier-performance KPIs with machine-learning-assisted anomaly detection to prioritize supplier reviews. Using simulated purchase-order data, the analysis evaluates 106 suppliers across delivery, quality, pricing, and contract-compliance dimensions. A transparent business risk score is combined with an Isolation Forest anomaly signal and presented in an interactive Power BI dashboard.

The final output identifies 6 High Risk suppliers and flags 7 suppliers for AI-assisted review. The analysis covers 411.18 million in simulated spend. Great Wall Packaging, Fujikawa Resources, and Thames Industrial Supply are the three highest-priority suppliers by final risk score.

## 1. Business context

Procurement teams need to monitor supplier performance before delivery and quality problems create material shortages, production disruption, or unplanned cost. Order-level data is often too detailed for quick decision-making, while a single KPI can hide important trade-offs.

This project creates a supplier-review workflow that answers:

1. Which suppliers have the highest operational risk?
2. What factors are driving each supplier's risk?
3. Which suppliers should procurement review first?
4. What corrective actions should the procurement team consider?

## 2. Data and KPI framework

The simulated source table contains purchase-order dates, promised and actual delivery dates, supplier identifiers, country and category, spend, contract status, and quality-rejection indicators. The order-level data is aggregated into one supplier-level scorecard.

The core KPIs are:

- On-time delivery rate
- Late-delivery rate
- Average delay days
- Quality-rejection rate
- Price volatility
- Off-contract purchasing share
- Purchase-order count and total spend

These measures were selected because they connect directly to procurement concerns: service reliability, supply continuity, quality exposure, commercial stability, and contract compliance.

## 3. Methodology

### 3.1 Transparent business risk score

The first layer uses explainable procurement KPIs. Higher late-delivery rates, longer average delays, higher reject rates, greater price volatility, and more off-contract purchases increase the business risk score. The score supports discussion with suppliers because its drivers can be traced to operational metrics.

### 3.2 AI-assisted anomaly detection

Isolation Forest is applied to supplier-level KPI patterns. It highlights suppliers whose combined behavior differs from the broader supplier population. This helps surface suppliers that may not cross every fixed threshold but still deserve investigation.

The anomaly flag is not a prediction of failure and is not an autonomous decision. It is a review signal for a procurement analyst.

### 3.3 Combined review priority

The final risk score brings together the transparent business score and the anomaly signal. Suppliers are then grouped into Low, Medium, and High risk tiers. This creates a practical queue for procurement review while preserving human oversight.

## 4. Results

- Total suppliers evaluated: 106
- High Risk suppliers: 6
- Suppliers flagged for AI review: 7
- Simulated spend analyzed: 411.18 million
- Risk-tier distribution: 78 Low, 22 Medium, and 6 High

Top final-risk suppliers:

| Rank | Supplier | Final risk score |
|---:|---|---:|
| 1 | Great Wall Packaging | 95.4 |
| 2 | Fujikawa Resources | 93.8 |
| 3 | Thames Industrial Supply | 93.0 |
| 4 | Cascade Technologies | 92.6 |
| 5 | Great Wall Components | 92.6 |
| 6 | Baltic Workplace | 91.7 |

The highest-risk group is mainly characterized by severe late-delivery performance and elevated quality-rejection rates. The visible separation between the six highest-risk suppliers and the next group gives procurement a clear first review cohort.

## 5. Dashboard output

![Dashboard overview](../images/dashboard_overview.png)

The Power BI dashboard provides an executive summary and supplier-level detail on one page. Users can filter by risk tier, compare the Top 10 suppliers by final risk score, review the risk-tier distribution, and inspect detailed performance measures.

## 6. Procurement recommendations

1. Start supplier recovery plans with the six High Risk suppliers, beginning with the top three.
2. Review delivery and quality KPIs weekly until performance remains within agreed thresholds.
3. Require root-cause analysis and corrective-action evidence for repeated late delivery or rejection.
4. Check whether high-risk suppliers support critical or single-source items and prepare alternative sourcing where needed.
5. Review AI anomaly flags with purchase-order volume and operational context before escalating.
6. Recalibrate risk weights and thresholds with category managers after collecting real feedback.

## 7. Governance and limitations

- The dataset is simulated and is suitable for portfolio demonstration, not real supplier decisions.
- Risk weights and tier thresholds are business assumptions that require stakeholder validation.
- An anomaly is an unusual pattern, not evidence of wrongdoing or inevitable failure.
- Suppliers with small order counts may show unstable percentages.
- The dashboard supports prioritization; it does not replace buyer judgment or supplier communication.
- Spend currency is not specified and values must not be represented as real company financials.

## 8. Technical stack and deliverables

- Python and pandas for data preparation and aggregation
- scikit-learn Isolation Forest for anomaly detection
- Power BI and DAX for interactive reporting
- CSV outputs for transparent handoff between analytics and visualization

Deliverables include the Python scripts, raw and derived datasets, interactive Power BI file, exported dashboard PDF, project report, README, and interview notes.

## Appendix: project logic

The project deliberately uses a two-layer approach:

1. A business score that is explainable to buyers and suppliers.
2. An anomaly model that widens the review net and highlights unusual combinations of KPIs.

This design makes the AI component useful without overstating automation. The final decision remains with the procurement team.

