for col in ["Attendance_Percent", "Assignment_Score"]:
    df[col] = df[col].fillna(df[col].median())
print("Missing values after cleaning:\n", df.isna().sum())

# ==========================================
# Q5: Average examination score by department
# ==========================================
dept_average = df.groupby("Department")["Exam_Score"].mean().sort_values(ascending=False)
print("\nAverage exam score by department:\n", dept_average)
print("Highest department average:", dept_average.index[0])