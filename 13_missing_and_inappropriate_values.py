import numpy as np
import pandas as pd

# Example hotel dataset because Hotel_Dataset.csv was not included with the manual.
data = {
    "CustomerID": [1, 2, 3, 4, 4, -6, 7, 8],
    "Age_Group": ["20-25", "25-30", "30-35", "35+", "35+", "25-30", "20-25", "30-35"],
    "Rating(1-5)": [5, 4, None, 3, 3, 7, 4, None],
    "Hotel": ["Ibis", "Ibys", "LemonTree", "RedFox", "RedFox", "Ibis", "Ibis", "LemonTree"],
    "FoodPreference": ["Veg", "veg", "Vegetarian", "Non-Veg", "Non-Veg", "non-Veg", None, "Veg"],
    "EstimatedSalary": [30000, 42000, None, 50000, 50000, -1000, 36000, 45000],
    "NoOfPax": [2, 3, 0, 5, 5, 22, None, 4],
    "Bill": [1200, 1800, 2400, 3200, 3200, -500, None, 2100]
}
df = pd.DataFrame(data)
print("Original data:\n", df)
print("\nDuplicate rows:", int(df.duplicated().sum()))
df = df.drop_duplicates().copy()

df.loc[df["CustomerID"] < 0, "CustomerID"] = np.nan
df.loc[df["Bill"] < 0, "Bill"] = np.nan
df.loc[df["EstimatedSalary"] < 0, "EstimatedSalary"] = np.nan
df.loc[(df["NoOfPax"] < 1) | (df["NoOfPax"] > 20), "NoOfPax"] = np.nan
df.loc[~df["Rating(1-5)"].between(1, 5), "Rating(1-5)"] = np.nan

df["Hotel"] = df["Hotel"].replace({"Ibys": "Ibis"})
df["FoodPreference"] = df["FoodPreference"].replace({"Vegetarian": "Veg", "veg": "Veg", "non-Veg": "Non-Veg"})
df["EstimatedSalary"] = df["EstimatedSalary"].fillna(df["EstimatedSalary"].mean())
df["NoOfPax"] = df["NoOfPax"].fillna(df["NoOfPax"].median())
df["Rating(1-5)"] = df["Rating(1-5)"].fillna(df["Rating(1-5)"].median())
df["Bill"] = df["Bill"].fillna(df["Bill"].mean())
df["CustomerID"] = df["CustomerID"].fillna(df["CustomerID"].median()).astype(int)
df["FoodPreference"] = df["FoodPreference"].fillna(df["FoodPreference"].mode()[0])
print("\nCleaned data:\n", df)
print("\nMissing values after cleaning:\n", df.isnull().sum())
