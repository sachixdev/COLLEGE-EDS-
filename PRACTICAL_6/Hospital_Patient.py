"""Problem Statement
A hospital monitors 3 patients over 3 days:
Matrix A → Blood pressure readings (Morning) 
Matrix B → Blood pressure readings (Evening) 
Each:
Row → Patient 
Column → Day
Tasks
Write a NumPy program to:
Compute daily average BP (column-wise) 
Find difference between evening and morning readings 
Identify readings where BP increased by more than 10 units 
Perform element-wise multiplication to analyze combined effect 
Find maximum BP recorded overall

"""
import numpy as np
# Create NumPy arrays for blood pressure readings in the morning and evening
bp_morning = np.array([[120, 125, 130],
                       [110, 115, 120],
                       [130, 135, 140]])
bp_evening = np.array([[130, 135, 140],
                       [120, 125, 130],
                       [140, 145, 150]])
# Compute daily average BP (column-wise)
daily_average_bp = np.mean((bp_morning + bp_evening) / 2, axis=0)
print("Daily average BP (column-wise):", daily_average_bp)
# Find difference between evening and morning readings
bp_difference = bp_evening - bp_morning
print("Difference between evening and morning readings:\n", bp_difference)
# Identify readings where BP increased by more than 10 units
bp_increase = bp_difference > 10
print("Readings where BP increased by more than 10 units:\n", bp_increase)
# Perform element-wise multiplication to analyze combined effect
combined_effect = bp_morning * bp_evening
print("Element-wise multiplication of morning and evening readings:\n", combined_effect)
