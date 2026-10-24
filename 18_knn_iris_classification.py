import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

iris = load_iris()
features = iris.data
labels = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42, stratify=labels
)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Training accuracy:", round(model.score(X_train, y_train), 3))
print("Testing accuracy:", round(accuracy_score(y_test, predictions), 3))
print("\nConfusion matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification report:\n", classification_report(y_test, predictions, target_names=iris.target_names))
example = [[5.1, 3.5, 1.4, 0.2]]
print("\nPrediction for [5.1, 3.5, 1.4, 0.2]:", iris.target_names[model.predict(example)[0]])
