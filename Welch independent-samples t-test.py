if len(high_attendance) >= 2 and len(low_attendance) >= 2:
    t_stat, p_ttest = stats.ttest_ind(
        high_attendance,
        low_attendance,
        equal_var=False
    )
    print("Welch t =", t_stat)
    print("P-value =", p_ttest)
else:
    print("Not enough data for t-test")