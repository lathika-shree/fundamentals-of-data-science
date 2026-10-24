import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Synthetic example with the same idea as Social_Network_Ads.csv: age and salary predict purchase.
np.random.seed(12)
count = 400
age = np.random.randint(18, 61, count)
salary = np.random.randint(15000, 150001, count)
score = (age - 35) / 8 + (salary - 75000) / 45000 + np.random.normal(0, 0.8, count)
purchased = (score > 0.2).astype(int)
features = np.column_stack((age, salary))
X_train, X_test, y_train, y_test = train_test_split(
    features, purchased, test_size=0.2, random_state=42, stratify=purchased
)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Training accuracy:", round(model.score(X_train, y_train), 3))
print("Testing accuracy:", round(accuracy_score(y_test, predictions), 3))
print("\nConfusion matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification report:\n", classification_report(y_test, predictions, zero_division=0))
print("Purchase prediction for age 30, salary 60000:", int(model.predict([[30, 60000]])[0]))
