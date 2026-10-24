import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
population_mean = 50
population_std = 10
population = np.random.normal(population_mean, population_std, 100000)
sample_sizes = [30, 50, 100]
num_samples = 500
sample_means = {}

for size in sample_sizes:
    means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, size=size, replace=False)
        means.append(np.mean(sample))
    sample_means[size] = means
    print("Sample size:", size, "Mean of sample means:", round(float(np.mean(means)), 2),
          "Standard error:", round(float(np.std(means, ddof=1)), 2))

plt.figure(figsize=(9, 8))
for position, size in enumerate(sample_sizes, start=1):
    plt.subplot(len(sample_sizes), 1, position)
    plt.hist(sample_means[size], bins=30, alpha=0.75, label=f"Sample size {size}")
    plt.axvline(population_mean, linestyle="dashed", label="Population mean")
    plt.title(f"Sampling Distribution (n={size})")
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")
    plt.legend()
plt.tight_layout()
plt.show()
