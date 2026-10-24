import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Example Salary_data because the CSV is not included in the manual.
years_experience = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]).reshape(-1, 1)
salary = np.array([30000, 34000, 38000, 42000, 45000, 49000, 53000, 57000, 60000, 64000, 68000, 72000])
X_train, X_test, y_train, y_test = train_test_split(years_experience, salary, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Coefficient:", round(float(model.coef_[0]), 2))
print("Intercept:", round(float(model.intercept_), 2))
print("Training R-squared:", round(model.score(X_train, y_train), 3))
print("Testing R-squared:", round(r2_score(y_test, predictions), 3))
print("Mean squared error:", round(mean_squared_error(y_test, predictions), 2))
print("Predicted salary for 7 years experience:", round(float(model.predict([[7]])[0]), 2))
plt.scatter(years_experience, salary, label="Actual salary")
plt.plot(years_experience, model.predict(years_experience), label="Regression line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression: Experience vs Salary")
plt.legend()
plt.tight_layout()
plt.show()
