import pandas as pd
from scipy import stats

df = pd.read_csv("case1_retail_sales.csv")

temp = df[["Footfall", "Daily_Sales"]].dropna()

r, p = stats.pearsonr(
    temp["Footfall"],
    temp["Daily_Sales"]
)

print("Pearson Correlation:", round(r, 3))
print("P-value:", round(p, 5))

print("H0: No significant correlation.")

if p < 0.05:
    print("Reject H0")
else:
    print("Fail to reject H0")