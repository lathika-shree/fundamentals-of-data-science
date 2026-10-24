import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

values = np.array([27, 50, 44, 6, 58, 61, 23, 86, 67, 20, 75, 7, 79, 61, 90, 54, 150])
q1, q3 = np.percentile(values, [25, 75])
iqr = q3 - q1
lower_range = q1 - 1.5 * iqr
upper_range = q3 + 1.5 * iqr
outliers = values[(values < lower_range) | (values > upper_range)]
clean_values = values[(values >= lower_range) & (values <= upper_range)]

print("Values:", values)
print("Q1:", q1, "Q3:", q3, "IQR:", iqr)
print("Lower range:", lower_range)
print("Upper range:", upper_range)
print("Outliers:", outliers)
print("Values after removing outliers:", clean_values)

plt.figure(figsize=(8, 3))
sns.boxplot(x=values)
plt.title("Box Plot Before Removing Outliers")
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 3))
sns.histplot(clean_values, kde=True, color="steelblue")
plt.title("Distribution After Removing Outliers")
plt.tight_layout()
plt.show()
