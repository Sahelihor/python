import pandas as pd

df = pd.read_csv("train.csv")

average = df.groupby("Pclass")["Fare"].mean()

highest = average.idxmax()

print("Highest average fare class:", highest)
print("Average fare:", average.max())