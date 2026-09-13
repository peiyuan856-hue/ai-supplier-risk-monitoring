# Methodology adapted from:
# https://github.com/dytcoke23/procurement-spend-analysis-dashboard
#
# Original project copyright (c) 2026 Harsh.
# Distributed under the MIT License.
# See ../THIRD_PARTY_NOTICES.md for attribution and the complete license notice.

from pathlib import Path

import pandas as pd


# 1. 定义输入和输出文件的位置
project_root = Path(__file__).resolve().parents[1]
input_file = project_root / "data" / "supplier_orders.csv"
output_file = project_root / "data" / "supplier_scorecard.csv"


# 2. 读取采购订单数据
orders = pd.read_csv(
    input_file,
    parse_dates=[
        "order_date",
        "promised_delivery_date",
        "actual_delivery_date",
    ],
)


# 3. 统一真假字段的格式
orders["on_contract"] = (
    orders["on_contract"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("true")
)

orders["quality_rejected"] = (
    orders["quality_rejected"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("true")
)


# 4. 计算每一笔订单是否准时，以及延期天数
orders["on_time"] = (
    orders["actual_delivery_date"]
    <= orders["promised_delivery_date"]
)

orders["delay_days"] = (
    orders["actual_delivery_date"]
    - orders["promised_delivery_date"]
).dt.days.clip(lower=0)


# 5. 按供应商汇总 KPI
scorecard = (
    orders.groupby(
        ["supplier_id", "supplier_name", "supplier_country"],
        as_index=False,
    )
    .agg(
        category=("category", "first"),
        total_spend=("line_total", "sum"),
        po_count=("po_id", "nunique"),
        on_time_rate=("on_time", "mean"),
        avg_delay_days=("delay_days", "mean"),
        reject_rate=("quality_rejected", "mean"),
        contract_rate=("on_contract", "mean"),
        avg_unit_price=("unit_price", "mean"),
        unit_price_std=("unit_price", "std"),
    )
)


# 6. 计算额外风险指标
scorecard["late_rate"] = 1 - scorecard["on_time_rate"]

scorecard["off_contract_share"] = (
    1 - scorecard["contract_rate"]
)

scorecard["price_volatility"] = (
    scorecard["unit_price_std"]
    / scorecard["avg_unit_price"]
).fillna(0)


# 7. 把不同指标转换成 0 到 100 的风险分
def capped_risk(series, risk_cap):
    return (series / risk_cap).clip(lower=0, upper=1)


scorecard["risk_score"] = (
    capped_risk(scorecard["late_rate"], 0.60) * 30
    + capped_risk(scorecard["avg_delay_days"], 10) * 15
    + capped_risk(scorecard["reject_rate"], 0.12) * 25
    + capped_risk(scorecard["price_volatility"], 0.15) * 20
    + capped_risk(scorecard["off_contract_share"], 0.40) * 10
).round(1)


# 8. 将供应商划分为低、中、高风险
scorecard["risk_tier"] = pd.cut(
    scorecard["risk_score"],
    bins=[-1, 45, 70, 101],
    labels=["Low", "Medium", "High"],
    right=False,
)


# 9. 整理最终输出字段
scorecard = scorecard[
    [
        "supplier_id",
        "supplier_name",
        "supplier_country",
        "category",
        "total_spend",
        "po_count",
        "on_time_rate",
        "late_rate",
        "avg_delay_days",
        "reject_rate",
        "price_volatility",
        "off_contract_share",
        "risk_score",
        "risk_tier",
    ]
]

scorecard = scorecard.sort_values(
    "risk_score",
    ascending=False,
)

scorecard.to_csv(output_file, index=False)


# 10. 在 Terminal 中显示结果
print("供应商评分表创建成功！")
print(f"供应商数量：{len(scorecard)}")
print(f"输出文件：{output_file}")

print("\n各风险等级的供应商数量：")
print(scorecard["risk_tier"].value_counts())

print("\n风险最高的 10 家供应商：")
print(
    scorecard[
        [
            "supplier_name",
            "late_rate",
            "reject_rate",
            "risk_score",
            "risk_tier",
        ]
    ].head(10)
)
