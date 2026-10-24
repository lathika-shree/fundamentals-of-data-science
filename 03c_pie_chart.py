import matplotlib.pyplot as plt

labels = ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4"]
votes = [315, 130, 245, 210]
explode = (0.12, 0, 0, 0)
plt.pie(votes, labels=labels, explode=explode, autopct="%.2f%%", startangle=90)
plt.title("Election Results")
plt.axis("equal")
plt.tight_layout()
plt.show()
