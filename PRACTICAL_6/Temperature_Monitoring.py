"""Temperatures recorded for a week:
30, 32, 31, 29, 35, 36, 33
Tasks:
Find the maximum temperature
Find the minimum temperature
Find the average temperature

"""
import numpy as np
# Create a NumPy array containing temperatures recorded for a week
temperatures = np.array([30, 32, 31, 29, 35, 36, 33])
# Print the array
print("Temperatures recorded for a week:", temperatures)
# Find the maximum temperature
max_temperature = np.max(temperatures)
print("Maximum temperature recorded for the week:", max_temperature)
# Find the minimum temperature
min_temperature = np.min(temperatures)
print("Minimum temperature recorded for the week:", min_temperature)
# Find the average temperature
average_temperature = np.mean(temperatures)
print("Average temperature recorded for the week:", average_temperature)
