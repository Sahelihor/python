print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.dtypes)
print("Missing values:\n", df.isna().sum())