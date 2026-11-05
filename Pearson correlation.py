temp = df[["Study_Hours_Per_Day", "Exam_Score"]].dropna()

r, p_corr = stats.pearsonr(
    temp["Study_Hours_Per_Day"],
    temp["Exam_Score"]
)