from pathlib import Path

import pandas as pd


data_file = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "supplier_orders.csv"
)

orders = pd.read_csv(data_file)

print("数据读取成功！")
print(f"订单行数：{len(orders):,}")
print(f"字段数量：{len(orders.columns)}")

print("\n字段名称：")
for column in orders.columns:
    print(f"- {column}")

print("\n前 5 行数据：")
print(orders.head())