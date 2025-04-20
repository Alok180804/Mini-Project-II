import pandas as pd
import matplotlib.pyplot as plt

# Load the merged data
merged_df = pd.read_csv("Netravathi River 1970-80/Merged_Sediment_Discharge_Data.csv")

# Sort by discharge
sorted_df = merged_df.sort_values(by='Discharge_m3_s').reset_index(drop=True)

# Create discharge bins (0–250, 250–500, ...)
max_discharge = int((sorted_df['Discharge_m3_s'].max() // 250 + 1) * 250)
bins = list(range(0, max_discharge + 250, 250))

# Assign bins
sorted_df['Discharge_Bin'] = pd.cut(sorted_df['Discharge_m3_s'], bins=bins)

# Group and sum sediment load
# binned_sediment = sorted_df.groupby('Discharge_Bin')['Sediment_tonne_day'].sum().reset_index()
binned_sediment = sorted_df.groupby('Discharge_Bin', observed=True)['Sediment_tonne_day'].sum().reset_index()
binned_sediment.columns = ['Discharge_Bin', 'Total_Sediment_tonne_day']

# Save to CSV
binned_sediment.to_csv("Binned_Sediment_Load.csv", index=False)

# Plot
plt.figure(figsize=(12, 6))
plt.bar(binned_sediment['Discharge_Bin'].astype(str), binned_sediment['Total_Sediment_tonne_day'], color='teal')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Discharge Bins (m³/s)")
plt.ylabel("Total Sediment Load (tonne/day)")
plt.title("Total Sediment Load per River Discharge Bin")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Report max sediment load
max_sediment = binned_sediment.loc[binned_sediment['Total_Sediment_tonne_day'].idxmax()]
print("Highest Sediment Load Bin:")
print(max_sediment)
