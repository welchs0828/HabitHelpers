import pandas as pd

def weekly_summary(df_compl: pd.DataFrame, df_mood: pd.DataFrame):
    # compl: [date, habit_id], mood: [date, rating]
    compl = df_compl.assign(val=1).pivot_table(index="date", columns="habit_id", values="val", fill_value=0)
    mood = df_mood.set_index("date")["rating"]
    week = compl.resample("W").sum().join(mood.resample("W").mean().rename("mood"))
    corr = week.corr(numeric_only=True)["mood"].sort_values(ascending=False)
    return corr