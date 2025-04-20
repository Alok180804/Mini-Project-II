import pandas as pd

# Load Excel files (assuming they're in the current directory)
suspended_data = pd.read_excel("Suspended Sediment_Bantwal.xlsx", sheet_name=1, skiprows=10)
discharge_data = pd.read_excel("River Water Discharge_Bantwal.xlsx", sheet_name=1, skiprows=10)

# Clean and rename columns
suspended_clean = suspended_data.iloc[:, [2, 3]]
suspended_clean.columns = ['Timestamp', 'Sediment_g_L']
suspended_clean['Timestamp'] = pd.to_datetime(suspended_clean['Timestamp'])

discharge_clean = discharge_data.iloc[:, [2, 3]]
discharge_clean.columns = ['Timestamp', 'Discharge_m3_s']
discharge_clean['Timestamp'] = pd.to_datetime(discharge_clean['Timestamp'])

# Merge on exact timestamp match
merged_df = pd.merge(discharge_clean, suspended_clean, on='Timestamp', how='inner')

# Convert units: Sediment Load (tonne/day) = g/L * m3/s * 86.4
merged_df['Sediment_tonne_day'] = merged_df['Sediment_g_L'] * merged_df['Discharge_m3_s'] * 86.4

# Save the merged file
merged_df.to_csv("Merged_Sediment_Discharge_Data.csv", index=False)

# Show first few rows to confirm
print(merged_df.head())
