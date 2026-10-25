# Experiment 6 - Time Series Analysis of Website Traffic
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load dataset
data = pd.read_csv('data/website_traffic.csv', parse_dates=['Date'], index_col='Date')

# Handle missing values by interpolation
data = data.interpolate()

# Plot the time series data
data[['Page_Views', 'Unique_Visitors']].plot(figsize=(12, 5))
plt.title('Page Views and Unique Visitors')
plt.show()
data['Bounce_Rate'].plot(figsize=(12, 4), color='orange')
plt.title('Bounce Rate')
plt.show()

# Time Series Decomposition
decomposition = seasonal_decompose(data['Page_Views'], model='additive')
decomposition.plot()
plt.show()

# Moving Average
data['Page_Views_MA'] = data['Page_Views'].rolling(window=30).mean()
data[['Page_Views', 'Page_Views_MA']].plot()
plt.title('Page Views with Moving Average')
plt.show()

# Anomaly Detection
data['Page_Views_Z'] = (data['Page_Views'] - data['Page_Views'].mean()) / data['Page_Views'].std()
anomalies = data[data['Page_Views_Z'].abs() > 3]
print("Anomalies detected:\n", anomalies[['Page_Views', 'Page_Views_Z']])
plt.plot(data.index, data['Page_Views'], label='Page Views')
plt.scatter(anomalies.index, anomalies['Page_Views'], color='red', label='Anomalies')
plt.legend()
plt.show()
