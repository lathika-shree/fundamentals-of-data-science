import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.DataFrame({
    "Country": ["France", "Spain", "Germany", "Spain", "Germany", "France", "Spain", "France", None, "France"],
    "Age": [44, 27, 30, 38, 40, 35, None, 48, 50, 37],
    "Salary": [72000, 48000, 54000, 61000, None, 58000, 52000, 79000, 83000, 67000],
    "Purchased": ["No", "Yes", "No", "No", "Yes", "Yes", "No", "Yes", "No", "Yes"]
})
print("Original data:\n", df)
df["Country"] = df["Country"].fillna(df["Country"].mode()[0])
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
country_encoded = pd.get_dummies(df["Country"], dtype=int)
features = pd.concat([country_encoded, df[["Age", "Salary"]]], axis=1)
print("\nEncoded and imputed features:\n", features)

standard_scaled = StandardScaler().fit_transform(features)
minmax_scaled = MinMaxScaler().fit_transform(features)
print("\nStandard-scaled values:\n", pd.DataFrame(standard_scaled, columns=features.columns).round(3))
print("\nMin-max scaled values:\n", pd.DataFrame(minmax_scaled, columns=features.columns).round(3))
