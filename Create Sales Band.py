import numpy as np
import pandas as pd

df = pd.read_csv("case1_retail_sales.csv")

df["Sales_Band"] = pd.cut(
    df["Daily_Sales"],
    bins=[-np.inf, 6000, 10000, np.inf],
    labels=["Low", "Medium", "High"],
    right=False
)

print("Sales Band Counts:")
print(df["Sales_Band"].value_counts())