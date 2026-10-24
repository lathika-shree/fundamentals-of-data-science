# Fundamentals of Data Science Lab - Programs

This repository contains the lab programs in the order of the Fundamentals of Data Science Lab manual.

## Experiment order

- **1(a)** `01a_job_postings_trend.py` - Data science job postings trend
- **1(b)** `01b_data_science_roles.py` - Distribution of data science roles
- **1(c)** `01c_data_types.py` - Structured, unstructured and semi-structured data
- **1(d)** `01d_encrypt_decrypt_fernet.py` - Encrypt and decrypt using Fernet
- **2** `02_sales_csv_preprocessing_visualization.py` - Sales data preprocessing, plots and heatmap
- **3(a)** `03a_line_plot.py` - Line plot
- **3(b)** `03b_bar_chart.py` - Bar chart
- **3(c)** `03c_pie_chart.py` - Pie chart
- **4** `04_word_frequency.py` - Word frequency in text
- **5** `05_diabetes_data_exploration.py` - Diabetes data collection and initial exploration
- **6** `06_website_traffic_time_series.py` - Website traffic time-series analysis
- **7** `07_random_sampling_distribution.py` - Random sampling and sampling distribution
- **8** `08_z_test_bird_weights.py` - Z-test example
- **9** `09_matplotlib_iris_visualization.py` - Visualization using the Iris dataset
- **10** `10_numpy_array_functions.py` - NumPy array functions
- **11** `11_pandas_dataframe.py` - Pandas DataFrame operations
- **12** `12_outlier_detection_iqr.py` - Outlier detection using IQR
- **13** `13_missing_and_inappropriate_values.py` - Handle missing/inappropriate values
- **14** `14_feature_scaling.py` - Standard scaling and min-max scaling
- **15** `15_data_preprocessing.py` - Data preprocessing and encoding
- **16** `16_eda_quantitative_qualitative.py` - Quantitative and qualitative EDA
- **17** `17_linear_regression.py` - Linear regression
- **18** `18_knn_iris_classification.py` - K-nearest neighbours classification
- **19** `19_logistic_regression.py` - Logistic regression
- **20** `20_kmeans_clustering.py` - K-means clustering

## How to run on Windows

1. Install Python 3 from https://www.python.org/downloads/ if it is not installed. On the installer, tick **Add Python to PATH**.
2. Download this repository as a ZIP from GitHub, extract it, and open the extracted folder.
3. Click the folder address bar in File Explorer, type `cmd`, and press Enter.
4. Install required libraries once:

   ```text
   py -m pip install -r requirements.txt
   ```

5. Run any program, for example:

   ```text
   py 01a_job_postings_trend.py
   ```

6. For plots, a graph window will appear. Close it to let the program continue. For ML experiments, read the printed accuracy/metrics in the terminal.

## Notes about datasets

The supplied manual refers to external CSV files such as `sales_data.csv`, `diabetes.csv`, `website_traffic.csv`, `Hotel_Dataset.csv`, `pre-process_datasample.csv`, `Salary_data.csv`, `Iris.csv`, `Social_Network_Ads.csv`, and `Mall_Customers.csv`, but these datasets are not embedded in the uploaded manual. To make every program runnable now, the related scripts use small illustrative data created in the code or a dataset included locally with scikit-learn. The experiment topics and methods follow the manual. If your instructor has supplied original CSV files, you can replace the sample data with those files.

## Important for correction

Run the programs on your laptop before correction. Keep the terminal/output and graph windows available, and open this GitHub repository in your browser. The sample datasets are for demonstrating the code and are not real medical, sales, employment or customer records.
