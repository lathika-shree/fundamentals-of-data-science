import matplotlib.pyplot as plt

names = ["SHREE", "DEV", "KEERTHI", "PRIYA", "SHAN", "KUMARAN"]
percentages = [96, 91, 94, 75, 45, 81]
plt.bar(names, percentages)
plt.xlabel("Names of Pupil")
plt.ylabel("Percentage")
plt.title("Comparison of HSC Percentage")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.show()
