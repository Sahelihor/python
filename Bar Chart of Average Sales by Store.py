import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("case1_retail_sales.csv")

store_mean = df.groupby("Store")["Daily_Sales"].mean()

store_mean.plot(
    kind="bar",
    figsize=(7, 4),
    edgecolor="black"
)

plt.title("Average Sales by Store")
plt.xlabel("Store")
plt.ylabel("Mean Sales")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()

print("Highest Average Sales Store:")
print(store_mean.idxmax())

print("Highest Mean Sales:")
print(store_mean.max())