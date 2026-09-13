# Data Provenance

| File | Provenance |
|---|---|
| `supplier_orders.csv` | Renamed, unmodified copy of `data/purchase_orders.csv` from [dytcoke23/procurement-spend-analysis-dashboard](https://github.com/dytcoke23/procurement-spend-analysis-dashboard) |
| `supplier_scorecard.csv` | Derived from `supplier_orders.csv` by `src/analyze_suppliers.py` |
| `supplier_risk_final.csv` | Derived from `supplier_scorecard.csv` by `src/ai_anomaly.py` |

The source order dataset is seeded synthetic data, not real company data.
The upstream project is distributed under the MIT License. See
[`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) for the complete notice.
