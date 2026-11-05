import pandas as pd

df = pd.read_csv("case1_retail_sales.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isna().sum())