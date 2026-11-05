import pandas as pd

df = pd.read_csv("train.csv")

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

alone = (df["FamilySize"] == 1).sum()
family = (df["FamilySize"] > 1).sum()

print("Travelling alone:", alone)
print("Travelling with family:", family)