import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

np.random.seed(7)
dates = pd.date_range("2025-01-01", periods=120, freq="D")
trend = np.arange(120) * 3
weekly = 30 * np.sin(2 * np.pi * np.arange(120) / 7)
page_views = 500 + trend + weekly + np.random.normal(0, 15, 120)
page_views[85] += 180
traffic = pd.DataFrame({
    "Date": dates,
    "Page_Views": page_views,
    "Unique_Visitors": (page_views * 0.62 + np.random.normal(0, 8, 120)).round(),
    "Bounce_Rate": np.clip(48 + 4 * np.sin(2 * np.pi * np.arange(120) / 7) + np.random.normal(0, 2, 120), 20, 80)
}).set_index("Date")
traffic = traffic.interpolate()
print(traffic.head())

traffic[["Page_Views", "Unique_Visitors", "Bounce_Rate"]].plot(subplots=True, figsize=(10, 7), title="Website Traffic Over Time")
plt.tight_layout()
plt.show()

decomposition = seasonal_decompose(traffic["Page_Views"], model="additive", period=7)
decomposition.plot()
plt.suptitle("Website Traffic Decomposition", y=1.02)
plt.tight_layout()
plt.show()

traffic["Page_Views_MA"] = traffic["Page_Views"].rolling(window=7, min_periods=1).mean()
traffic[["Page_Views", "Page_Views_MA"]].plot(figsize=(10, 4), title="Page Views with 7-Day Moving Average")
plt.tight_layout()
plt.show()

traffic["Page_Views_Z"] = (traffic["Page_Views"] - traffic["Page_Views"].mean()) / traffic["Page_Views"].std()
anomalies = traffic[traffic["Page_Views_Z"].abs() > 3]
print("\nPotential anomalies:\n", anomalies[["Page_Views", "Page_Views_Z"]])
plt.plot(traffic.index, traffic["Page_Views"], label="Page Views")
plt.scatter(anomalies.index, anomalies["Page_Views"], label="Anomalies")
plt.title("Website Traffic Anomaly Detection")
plt.legend()
plt.tight_layout()
plt.show()
