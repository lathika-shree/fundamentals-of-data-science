import pandas as pd

df = pd.DataFrame({
    "Country": ["France", "Spain", "Germany", "Spain", "Germany", "France", "Spain", "France", None, "France"],
    "Age": [44, 27, 30, 38, 40, 35, None, 48, 50, 37],
    "Salary": [72000, 48000, 54000, 61000, None, 58000, 52000, 79000, 83000, 67000],
    "Purchased": ["No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "No", "Yes"]
})
print("Original data:\n", df)
df["Country"] = df["Country"].fillna(df["Country"].mode()[0])
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(round(df["Salary"].mean()))
country_columns = pd.get_dummies(df["Country"], dtype=int)
processed = pd.concat([country_columns, df[["Age", "Salary", "Purchased"]]], axis=1)
processed["Purchased"] = processed["Purchased"].map({"No": 0, "Yes": 1})
print("\nProcessed dataset:\n", processed)
print("\nRemaining missing values:\n", processed.isnull().sum())
