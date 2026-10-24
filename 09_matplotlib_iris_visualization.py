import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame.rename(columns={
    "sepal length (cm)": "SepalLengthCm",
    "sepal width (cm)": "SepalWidthCm",
    "petal length (cm)": "PetalLengthCm",
    "petal width (cm)": "PetalWidthCm",
    "target": "target"
})
df["variety"] = df["target"].map(dict(enumerate(iris.target_names)))
print(df.head())
print("\nDataset information:")
df.info()
print("\nSummary statistics:\n", df.describe())
print("\nVariety counts:\n", df["variety"].value_counts())

sns.countplot(data=df, x="variety", color="steelblue")
plt.title("Count of Iris Varieties")
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="SepalLengthCm", y="SepalWidthCm", hue="variety")
plt.title("Sepal Length vs Sepal Width")
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="PetalLengthCm", y="PetalWidthCm", hue="variety")
plt.title("Petal Length vs Petal Width")
plt.tight_layout()
plt.show()

sns.pairplot(df, vars=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"], hue="variety")
plt.show()
