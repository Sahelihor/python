for col in ["Study_Hours_Per_Day", "Exam_Score"]:
    x = df[col].dropna().to_numpy()
    print(f"\n{col}")
    print("Mean:", np.mean(x))
    print("Median:", np.median(x))
    print("Standard deviation:", np.std(x, ddof=1))
    print("Minimum:", np.min(x))
    print("Maximum:", np.max(x))