import pandas as pd

df = pd.read_csv("case1_retail_sales.csv", parse_dates=["Date"])

print("First Five Rows:")
print(df.head())