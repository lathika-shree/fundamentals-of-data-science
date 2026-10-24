import pandas as pd

employees = [
    [1, "Smith", 50000],
    [2, "Jones", 60000],
    [3, "Priya", 70000],
    [4, "Arun", 50000],
    [5, "Meena", 80000]
]
df = pd.DataFrame(employees, columns=["EmpID", "Name", "Salary"])
print("Employee DataFrame:\n", df)
print("\nFirst rows:\n", df.head())
print("\nLast rows:\n", df.tail())
print("\nDataFrame information:")
df.info()
print("\nSalary column:\n", df["Salary"])
print("\nMean salary:", df["Salary"].mean())
print("Median salary:", df["Salary"].median())
print("Mode salary:\n", df["Salary"].mode().tolist())
print("Variance:", round(df["Salary"].var(), 2))
print("Standard deviation:", round(df["Salary"].std(), 2))
print("\nNumeric summary:\n", df.describe())
print("\nAll-column summary:\n", df.describe(include="all"))
print("\nColumn names:", df.columns.tolist())
print("\nNumPy array:\n", df.to_numpy())
