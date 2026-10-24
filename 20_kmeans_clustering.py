import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

np.random.seed(21)
cluster1 = np.column_stack((np.random.normal(25, 4, 60), np.random.normal(25, 8, 60)))
cluster2 = np.column_stack((np.random.normal(55, 7, 70), np.random.normal(70, 8, 70)))
cluster3 = np.column_stack((np.random.normal(80, 6, 70), np.random.normal(30, 7, 70)))
customers = np.vstack((cluster1, cluster2, cluster3))
customers = np.clip(customers, 1, 100)

scaled_customers = StandardScaler().fit_transform(customers)
model = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = model.fit_predict(scaled_customers)
centers = StandardScaler().fit(customers).inverse_transform(model.cluster_centers_)
print("First 10 customer records [Annual income, spending score]:\n", customers[:10].round(1))
print("\nCluster counts:", np.bincount(labels))
print("\nCluster centers [Annual income, spending score]:\n", centers.round(2))

plt.scatter(customers[:, 0], customers[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker="X", s=180, label="Cluster centers")
plt.xlabel("Annual Income (sample scale)")
plt.ylabel("Spending Score (sample scale)")
plt.title("K-Means Customer Clustering")
plt.legend()
plt.tight_layout()
plt.show()
