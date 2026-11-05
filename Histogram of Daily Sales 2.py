import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("case1_retail_sales.csv")

plt.figure(figsize=(7, 4))

plt.hist(
    df["Daily_Sales"].dropna(),
    bins=12,
    edgecolor="black"
)

plt.title("Daily Sales Distribution")
plt.xlabel("Daily Sales")
plt.ylabel("Number of Days")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()