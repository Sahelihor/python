df["Performance_Level"] = np.select(
    [
        df["Exam_Score"] >= 75,
        (df["Exam_Score"] >= 50) & (df["Exam_Score"] < 75)
    ],
    ["High", "Moderate"],
    default="Needs Support"
)

df.loc[df["Exam_Score"].isna(), "Performance_Level"] = "Unknown"