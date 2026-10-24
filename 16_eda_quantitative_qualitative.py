import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.DataFrame({
    "total_bill": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88, 15.04, 18.29, 30.14, 12.90],
    "tip": [1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00, 3.12, 1.96, 3.00, 4.00, 1.50],
    "sex": ["Female", "Male", "Male", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Male", "Female"],
    "smoker": ["No", "No", "No", "No", "No", "Yes", "No", "Yes", "No", "No", "Yes", "No"],
    "day": ["Sun", "Sat", "Sun", "Sun", "Sun", "Sat", "Sun", "Sat", "Fri", "Sun", "Sat", "Thur"],
    "time": ["Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Dinner", "Lunch"],
    "size": [2, 3, 3, 2, 4, 4, 2, 4, 2, 2, 4, 2]
})
print("First five rows:\n", tips.head())
print("\nQuantitative summary:\n", tips[["total_bill", "tip", "size"]].describe())
print("\nQualitative counts by day:\n", tips["day"].value_counts())
print("\nCounts by time:\n", tips["time"].value_counts())

sns.histplot(data=tips, x="total_bill", kde=True, color="steelblue")
plt.title("Distribution of Total Bill")
plt.tight_layout()
plt.show()

sns.scatterplot(data=tips, x="tip", y="total_bill", hue="sex")
plt.title("Tip vs Total Bill")
plt.tight_layout()
plt.show()

sns.boxplot(data=tips, x="day", y="total_bill", color="steelblue")
plt.title("Total Bill by Day")
plt.tight_layout()
plt.show()

sns.countplot(data=tips, x="day", color="steelblue")
plt.title("Number of Bills by Day")
plt.tight_layout()
plt.show()

sns.heatmap(tips[["total_bill", "tip", "size"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
