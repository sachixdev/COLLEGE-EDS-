"""A weather station records temperature for 30 days.
Tasks:
Generate 30 random temperatures between 25 and 45
Find the average temperature
Identify heatwave days (temperature > 40)
Count how many heatwave days occurred
"""
import numpy as np
# Generate 30 random temperatures between 25 and 45
temperatures = np.random.uniform(25, 45, 30)
# Print the array of temperatures
print("Temperatures recorded for 30 days:", temperatures)
# Find the average temperature
average_temperature = np.mean(temperatures)
print("Average temperature for 30 days:", average_temperature)
# Identify heatwave days (temperature > 40)
heatwave_days = temperatures > 40
print("Heatwave days (temperature > 40):", heatwave_days)
# Count how many heatwave days occurred
heatwave_count = np.sum(heatwave_days)
print("Number of heatwave days:", heatwave_count)
