import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Pregnancies": [1, 4, 0, 3, 2, 5, 1, 6, 2, 0],
    "Glucose": [89, 120, 95, 150, 110, 165, 105, 180, 130, 98],
    "BloodPressure": [66, 70, 60, 82, 72, 88, 68, 90, 74, 64],
    "BMI": [28.1, 32.0, 22.5, 35.7, 29.8, 38.2, 26.4, 41.0, 31.2, 24.0],
    "Age": [25, 38, 22, 44, 31, 52, 28, 55, 36, 23],
    "Outcome": [0, 1, 0, 1, 0, 1, 0, 1, 1, 0]
}
diabetes_df = pd.DataFrame(data)
print("First five rows:\n", diabetes_df.head())
print("\nDataset information:")
diabetes_df.info()
print("\nSummary statistics:\n", diabetes_df.describe())
print("\nOutcome counts:\n", diabetes_df["Outcome"].value_counts())
print("\nMissing values:\n", diabetes_df.isnull().sum())
diabetes_df["Outcome"].value_counts().sort_index().plot(kind="bar")
plt.title("Diabetes Outcome Counts (Sample Data)")
plt.xlabel("Outcome (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
