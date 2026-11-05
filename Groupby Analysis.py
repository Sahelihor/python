import pandas as pd

df = pd.read_csv("case1_retail_sales.csv")

print("Sales Analysis by Store:")

print(
    df.groupby("Store")["Daily_Sales"].agg(
        ["mean", "median", "count"]
    )
)

print("\nMean Sales by Promotion:")

print(
    df.groupby("Promotion")["Daily_Sales"].mean()
)