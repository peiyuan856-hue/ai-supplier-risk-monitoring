# Resume and Interview Notes

## Suggested project title

**AI-Assisted Supplier Performance & Risk Monitoring**  
AI 辅助供应商绩效与风险监控项目

## English resume bullets

- Built an AI-assisted supplier risk monitoring workflow for **106 simulated suppliers** using Python, pandas, scikit-learn, and Power BI, consolidating delivery, delay, quality, price-volatility, and contract-compliance metrics into a supplier scorecard.
- Applied **Isolation Forest** to flag **7 anomalous supplier profiles** and combined the results with transparent KPI scoring to identify **6 High Risk suppliers** for procurement review.
- Designed an interactive Power BI dashboard with DAX measures, risk-tier filtering, Top 10 supplier ranking, risk distribution, supplier-level drill-down, and procurement action recommendations.

## 中文简历表述

- 使用 Python、Pandas、Scikit-learn 与 Power BI 搭建 AI 辅助供应商风险监控流程，基于交付延误、质量拒收、价格波动及非合同采购等指标，对 106 家模拟供应商建立绩效评分卡。
- 运用 Isolation Forest 识别 7 家异常表现供应商，并结合可解释的业务风险评分，筛选出 6 家高风险供应商，为采购团队提供分层复核优先级。
- 使用 DAX 设计交互式 Power BI 仪表盘，呈现风险等级筛选、Top 10 供应商、风险分布、供应商明细与采购改进建议。

## 90-second English interview pitch

I built this project to simulate a real procurement analyst problem: how to identify supplier risk before buyers spend hours checking purchase orders one by one. I started with order-level data and used Python and pandas to create supplier-level KPIs, including late-delivery rate, average delay days, quality-rejection rate, price volatility, and off-contract purchasing share.

I first created a transparent business risk score because procurement teams need to understand why a supplier is ranked as risky. I then added Isolation Forest as an AI-assisted second layer to flag unusual combinations of performance metrics. The model does not make sourcing decisions; it creates a review signal for a human analyst.

The analysis covered 106 simulated suppliers and identified 6 High Risk suppliers, while the anomaly model flagged 7 suppliers for review. I presented the results in Power BI with KPI cards, a Top 10 risk ranking, risk-tier distribution, supplier details, and recommended actions. The main business conclusion was to prioritize recovery plans for Great Wall Packaging, Fujikawa Resources, and Thames Industrial Supply, then monitor delivery and quality KPIs weekly.

## 90 秒中文面试话术

我做这个项目，是为了模拟采购分析师的真实问题：当订单很多时，如何快速判断哪些供应商最值得优先复核，而不是靠人工逐单检查。

我先用 Python 和 Pandas 把订单级数据汇总成供应商级评分卡，计算了延期率、平均延误天数、质量拒收率、价格波动和非合同采购占比等 KPI。第一层是可解释的业务风险评分，确保采购人员能说清楚供应商为什么被判定为高风险；第二层使用 Isolation Forest 识别多指标组合异常的供应商。这里的 AI 只是辅助复核，不直接代替采购决策。

最终项目分析了 106 家模拟供应商，识别出 6 家高风险供应商，AI 异常模型标记了 7 家需要复核的供应商。我再用 Power BI 做了风险等级筛选、Top 10 排名、风险分布、供应商明细和行动建议。业务结论是优先推动 Great Wall Packaging、Fujikawa Resources 和 Thames Industrial Supply 制定改善计划，并按周跟踪交付和质量 KPI。

## Likely interview questions

### Why did you use Isolation Forest?

Because there was no reliable labeled outcome such as confirmed supplier failure. Isolation Forest is suitable for unsupervised anomaly detection and can identify unusual combinations of supplier KPIs. I used it only as a review flag, not as a prediction label.

### Why not rely only on machine learning?

Procurement teams need explainability. A KPI-based score makes the risk drivers visible, while the anomaly model can surface patterns missed by fixed thresholds. Using both gives a clearer and more practical review process.

### What would you improve with real company data?

I would validate KPI definitions with procurement stakeholders, add material criticality and spend concentration, use time-based validation, set minimum order-count rules, monitor model drift, and test whether alerts lead to measurable supplier improvement.

### What is the biggest limitation?

The data is simulated, so the project proves the workflow and analytical logic rather than real-world predictive accuracy. Risk thresholds and weights must be calibrated before business use.

## Honest wording to use

- Say **AI-assisted anomaly detection**, not autonomous supplier selection.
- Say **review prioritization**, not supplier-failure prediction.
- State clearly that the data is simulated.
- Explain that final decisions require buyer review and supplier context.

