import pandas as pd

df = pd.read_csv("train.csv")

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

def family_group(size):
    if size == 1:
        return "Alone"
    elif size <= 4:
        return "Small Family"
    else:
        return "Large Family"

df["Family_Group"] = df["FamilySize"].apply(family_group)

result = df.groupby("Family_Group")["Survived"].mean() * 100

print("Survival Rates:")
print(result)