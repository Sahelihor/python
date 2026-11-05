import pandas as pd

df = pd.read_csv("train.csv")

result = df.groupby("Pclass").agg(
    Total_Passengers=("PassengerId", "count"),
    Survivors=("Survived", "sum")
)

print(result)