import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Load merged data
df = pd.read_csv("Merged_Sediment_Discharge_Data.csv")

# Convert 'Timestamp' to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Sort by timestamp
df = df.sort_values('Timestamp')

# Filter first one year of data
start_date = df['Timestamp'].min()
end_date = start_date + pd.DateOffset(years=1)
df_one_year = df[(df['Timestamp'] >= start_date) & (df['Timestamp'] < end_date)]

# Drop rows with zero or negative values (for log-log fitting)
df_one_year = df_one_year[(df_one_year['Discharge_m3_s'] > 0) & (df_one_year['Sediment_tonne_day'] > 0)]

# Define power-law function: Sediment = a * Discharge^b
def power_law(x, a, b):
    return a * x**b

# Fit the curve
x_data = df_one_year['Discharge_m3_s'].values
y_data = df_one_year['Sediment_tonne_day'].values
params, _ = curve_fit(power_law, x_data, y_data)
a, b = params

# Generate fitted curve
x_fit = np.linspace(min(x_data), max(x_data), 500)
y_fit = power_law(x_fit, a, b)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, alpha=0.6, color='darkorange', label='Observed Data')
plt.plot(x_fit, y_fit, color='blue', linewidth=2, label=f'Best Fit: Sediment = {a:.3f} × Discharge^{b:.3f}')
plt.xlabel('River Water Discharge (m³/s)')
plt.ylabel('Suspended Sediment Load (tonne/day)')
plt.title('Sediment Load vs River Discharge (First 1 Year)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
