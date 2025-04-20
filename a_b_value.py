import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

# Load the merged CSV
df = pd.read_csv("Merged_Sediment_Discharge_Data.csv")

# Convert timestamp to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Define power-law function
def power_law(x, a, b):
    return a * x**b

# Add year column
df['Year'] = df['Timestamp'].dt.year

# Store results
yearly_results = []

# Fit model year by year
for year in df['Year'].unique():
    subset = df[df['Year'] == year]
    x = subset['Discharge_m3_s'].values
    y = subset['Sediment_tonne_day'].values

    # Filter out non-positive values
    mask = (x > 0) & (y > 0)
    x, y = x[mask], y[mask]

    if len(x) > 10:  # Sufficient data points
        try:
            popt, _ = curve_fit(power_law, x, y)
            a, b = popt
            yearly_results.append((year, a, b))
        except Exception as e:
            print(f"Could not fit year {year}: {e}")

# Convert to DataFrame
results_df = pd.DataFrame(yearly_results, columns=['Year', 'a', 'b'])

# Calculate averages
avg_a = results_df['a'].mean()
avg_b = results_df['b'].mean()

print("Yearly Fit Parameters:\n", results_df)
print(f"\nAverage a: {avg_a:.4f}")
print(f"Average b: {avg_b:.4f}")

# Save results to CSV
results_df.to_csv("Yearly_Sediment_Discharge_Fit.csv", index=False)

# Also save the averages as a separate CSV
avg_df = pd.DataFrame([{'Average_a': avg_a, 'Average_b': avg_b}])
avg_df.to_csv("Average_Sediment_Discharge_Fit.csv", index=False)

print("Saved 'Yearly_Sediment_Discharge_Fit.csv' and 'Average_Sediment_Discharge_Fit.csv'")
