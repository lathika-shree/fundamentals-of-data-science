import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales data is created here because the manual does not include sales_data.csv.
data = {
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06",
             "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10", "2023-01-11", "2023-01-12"],
    "Product": ["Product A", "Product B", "Product A", "Product C", "Product B", "Product C",
                "Product A", "Product B", "Product C", "Product A", "Product B", "Product C"],
    "Sales": [200, 150, 220, 300, None, 280, 250, 180, 320, 230, 170, 340],
    "Quantity": [4, 3, 5, 6, 4, 7, 5, 4, 8, 6, 3, 8],
    "Region": ["North", "South", "North", "East", "West", "East", "North", "West", "East", "North", "South", "East"]
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
print("First five rows:\n", df.head())
print("\nMissing values before cleaning:\n", df.isnull().sum())
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
df = df.dropna(subset=["Product", "Quantity", "Region"])
print("\nSummary statistics:\n", df[["Sales", "Quantity"]].describe())

product_summary = df.groupby("Product", as_index=False).agg(Sales=("Sales", "sum"), Quantity=("Quantity", "sum"))
print("\nSales and quantity by product:\n", product_summary)
plt.figure(figsize=(8, 4))
plt.bar(product_summary["Product"], product_summary["Sales"])
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product")
plt.tight_layout()
plt.show()

sales_over_time = df.groupby("Date", as_index=False)["Sales"].sum()
plt.figure(figsize=(8, 4))
plt.plot(sales_over_time["Date"], sales_over_time["Sales"], marker="o")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Sales Over Time")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

pivot = df.pivot_table(values="Sales", index="Region", columns="Product", aggfunc="sum", fill_value=0)
print("\nSales by region and product:\n", pivot)
correlation = df[["Sales", "Quantity"]].corr()
print("\nCorrelation matrix:\n", correlation)
sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
