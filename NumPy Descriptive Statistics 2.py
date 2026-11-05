import numpy as np
import pandas as pd

df = pd.read_csv("case1_retail_sales.csv")

for col in ["Footfall", "Daily_Sales"]:
    x = df[col].dropna().to_numpy()

    print("\n", col)
    print("Mean:", np.mean(x))
    print("Median:", np.median(x))
    print("Standard Deviation:", np.std(x, ddof=1))
    print("Minimum:", np.min(x))
    print("Maximum:", np.max(x))