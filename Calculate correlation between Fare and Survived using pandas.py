import pandas as pd

df = pd.read_csv("train.csv")

correlation = df["Fare"].corr(df["Survived"])

print("Correlation:", correlation)