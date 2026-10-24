import matplotlib.pyplot as plt

roles = ["Data Analyst", "Data Engineer", "Data Scientist", "ML Engineer", "Business Analyst"]
counts = [300, 500, 450, 200, 150]
print(dict(zip(roles, counts)))
plt.bar(roles, counts)
plt.title("Distribution of Data Science Roles")
plt.xlabel("Role")
plt.ylabel("Count")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.show()
