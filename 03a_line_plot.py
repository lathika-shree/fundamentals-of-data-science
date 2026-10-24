import matplotlib.pyplot as plt

overs = list(range(5, 51, 5))
india_score = [30, 55, 90, 129, 165, 200, 239, 270, 310, 350]
sri_lanka_score = [25, 70, 90, 120, 140, 170, 195, 220, 255, 279]

plt.plot(overs, india_score, marker="o", label="India")
plt.plot(overs, sri_lanka_score, marker="o", label="Sri Lanka")
plt.title("India vs Sri Lanka")
plt.xlabel("Overs")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
