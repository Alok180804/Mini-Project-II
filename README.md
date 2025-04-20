# Mini-Project-II
# Effective Discharge Estimation in River Systems

This repository presents a series of Python scripts developed for the analysis and estimation of **effective discharge** in riverine systems, with a specific application to the **Netravathi River Basin (1970–1980)**. The effective discharge represents the flow that transports the greatest volume of sediment over time, playing a critical role in fluvial geomorphology and river engineering.

## Overview

The workflow involves:
- Cleaning and merging raw hydrological and sediment data
- Computing sediment loads based on observed discharge and concentration
- Grouping sediment loads by discharge bins to determine the effective discharge
- Fitting sediment-discharge relationships using a power-law model
- Analyzing interannual trends in sediment transport dynamics

This study aids in understanding sediment-water interactions and contributes to improved modeling of channel-forming discharges.

---

## Repository Contents

| File | Description |
|------|-------------|
| `Data Cleaning.py` | Preprocesses and merges raw sediment and discharge datasets. Computes sediment load in tonnes/day. |
| `Effective Discharge Estimation.py` | Bins sediment load by discharge intervals and identifies the discharge class responsible for the highest sediment transport (effective discharge). |
| `qs_q_plot.py` | Visualizes the sediment-discharge relationship for the first year of data and fits a power-law curve. |
| `a_b_value.py` | Performs annual curve fitting of sediment vs discharge and extracts year-wise and average `a` and `b` parameters for power-law modeling. |

---

## Methodology

1. **Data Integration and Cleaning**
   - Excel files containing discharge and sediment concentration measurements are merged based on timestamp.
   - Sediment load is calculated using:
     \[
     \text{Sediment Load (tonne/day)} = \text{Concentration (g/L)} \times \text{Discharge (m³/s)} \times 86.4
     \]

2. **Effective Discharge Estimation**
   - Data is grouped into discharge bins (default width: 250 m³/s).
   - Total sediment transported in each bin is calculated.
   - The bin with the maximum sediment load is identified as the **effective discharge** class.

3. **Power-Law Curve Fitting**
   - A log-log regression of the form:
     \[
     Q_s = a \cdot Q^b
     \]
     is applied to estimate sediment transport dynamics.

4. **Year-wise Analysis**
   - Interannual variations in sediment-discharge relationships are captured through parameter fitting for each year.
   - Results are exported for further statistical or modeling use.

---

## Requirements

This project uses the following Python libraries:

```bash
pandas
matplotlib
numpy
scipy
openpyxl
