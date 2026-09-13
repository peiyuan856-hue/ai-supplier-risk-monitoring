# Methodology adapted from:
# https://github.com/dytcoke23/procurement-spend-analysis-dashboard
#
# Original project copyright (c) 2026 Harsh.
# Distributed under the MIT License.
# See ../THIRD_PARTY_NOTICES.md for attribution and the complete license notice.

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


# 1. 定义输入和输出文件
project_root = Path(__file__).resolve().parents[1]
input_file = project_root / "data" / "supplier_scorecard.csv"
output_file = project_root / "data" / "supplier_risk_final.csv"


# 2. 读取供应商评分表
scorecard = pd.read_csv(input_file)


# 3. 选择提供给 AI 的风险指标
feature_columns = [
    "late_rate",
    "avg_delay_days",
    "reject_rate",
    "price_volatility",
    "off_contract_share",
]

features = scorecard[feature_columns].fillna(0)


# 4. 标准化指标
# 不同指标的单位不同，标准化后才能公平比较
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


# 5. 使用 Isolation Forest 识别异常供应商
# contamination=0.06 表示预计约 6% 的供应商需要重点审查
model = IsolationForest(
    n_estimators=300,
    contamination=0.06,
    random_state=42,
)

model_prediction = model.fit_predict(scaled_features)


# 6. 将异常程度转换成 0 到 100 分
# 分数越高，表示该供应商与其他供应商越不相似
raw_anomaly_score = -model.score_samples(scaled_features)

scorecard["anomaly_score"] = (
    pd.Series(
        raw_anomaly_score,
        index=scorecard.index,
    )
    .rank(pct=True)
    .mul(100)
    .round(1)
)

scorecard["ai_anomaly_flag"] = np.where(
    model_prediction == -1,
    "Review",
    "Normal",
)


# 7. 区分业务规则评分和 AI 异常评分
scorecard = scorecard.rename(
    columns={
        "risk_score": "business_risk_score",
        "risk_tier": "business_risk_tier",
    }
)


# 8. 组合最终风险分
# 业务规则占 70%，AI 异常检测占 30%
scorecard["final_risk_score"] = (
    scorecard["business_risk_score"] * 0.70
    + scorecard["anomaly_score"] * 0.30
).round(1)


# 9. 生成最终风险等级
scorecard["final_risk_tier"] = pd.cut(
    scorecard["final_risk_score"],
    bins=[-1, 45, 70, 101],
    labels=["Low", "Medium", "High"],
    right=False,
)


# 10. 按最终风险分从高到低排序
scorecard = scorecard.sort_values(
    "final_risk_score",
    ascending=False,
)


# 11. 保存最终结果
scorecard.to_csv(
    output_file,
    index=False,
    float_format="%.4f",
)


# 12. 显示分析结果
review_count = (
    scorecard["ai_anomaly_flag"] == "Review"
).sum()

print("AI 异常检测完成！")
print(f"供应商总数：{len(scorecard)}")
print(f"AI 建议重点审查：{review_count}")
print(f"最终文件：{output_file}")

print("\n最终风险最高的 10 家供应商：")
print(
    scorecard[
        [
            "supplier_name",
            "business_risk_score",
            "anomaly_score",
            "ai_anomaly_flag",
            "final_risk_score",
            "final_risk_tier",
        ]
    ]
    .head(10)
    .to_string(index=False)
)
