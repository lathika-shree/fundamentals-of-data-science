import numpy as np
from scipy.stats import norm

sample_data = np.array([152, 148, 151, 149, 147, 153, 150, 148, 152, 149,
                        151, 150, 149, 152, 151, 148, 150, 152, 149, 150,
                        148, 153, 151, 150, 149, 152, 148, 151, 150, 153])
population_mean = 150
alpha = 0.05
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1)
n = len(sample_data)
z_statistic = (sample_mean - population_mean) / (sample_std / np.sqrt(n))
p_value = 2 * (1 - norm.cdf(abs(z_statistic)))

print(f"Sample Mean: {sample_mean:.2f}")
print(f"Z-Statistic: {z_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")
if p_value < alpha:
    print("Reject the null hypothesis: average weight is significantly different from 150 grams.")
else:
    print("Fail to reject the null hypothesis: insufficient evidence of a difference from 150 grams.")
print("Note: this follows the manual's example, using sample standard deviation in the statistic.")
