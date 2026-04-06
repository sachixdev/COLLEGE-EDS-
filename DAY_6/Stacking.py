""" Problem Statement
A company has collected employee performance scores from two departments:
Array A → Sales Department scores 
Array B → Marketing Department scores 
Each array is a 3×3matrix where:
Rows represent employees 
Columns represent performance metrics
Write a Python program using NumPy to:
Perform Horizontal Stacking 
Combine both arrays side by side (same rows, more columns) 
Perform Vertical Stacking 
Combine both arrays one below the other (more rows, same columns) 
Find the average performance after vertical stacking (column-wise)

"""
import numpy as np
# Create NumPy arrays for Sales Department scores and Marketing Department scores
sales_scores = np.array([[85, 90, 80],
                         [78, 88, 92],
                         [90, 85, 87]])
marketing_scores = np.array([[80, 85, 88],
                             [82, 90, 91],
                             [88, 87, 89]])
# Perform Horizontal Stacking
horizontal_stacked = np.hstack((sales_scores, marketing_scores))
print("Horizontal Stacking (side by side):\n", horizontal_stacked)
# Perform Vertical Stacking
vertical_stacked = np.vstack((sales_scores, marketing_scores))
print("Vertical Stacking (one below the other):\n", vertical_stacked)
# Find the average performance after vertical stacking (column-wise)
average_performance = np.mean(vertical_stacked, axis=0)
print("Average performance after vertical stacking (column-wise):", average_performance)
