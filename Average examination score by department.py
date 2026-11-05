dept_average = df.groupby("Department")["Exam_Score"].mean().sort_values(ascending=False)
print("\nAverage exam score by department:\n", dept_average)
print("Highest department average:", dept_average.index[0])

# ==========================================
# Q6: Create performance categories
# ==========================================
df["Performance_Level"] = np.select(
    [df["Exam_Score"] >= 75, df["Exam_Score"] >= 50],
    ["High", "Moderate"],
    default="Needs Support"
)
print("\nPerformance counts:\n", df["Performance_Level"].value_counts())