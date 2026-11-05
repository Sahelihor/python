import pandas as pd

df = pd.read_csv("train.csv")

print(df.head(10))
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("Column names:")
print(df.columns)