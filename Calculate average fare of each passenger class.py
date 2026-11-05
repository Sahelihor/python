import pandas as pd

df = pd.read_csv("train.csv")

average = df.groupby("Pclass")["Fare"].mean()

print(average)