"""A shop records daily sales for 6 days:
120, 150, 180, 200, 170, 160
Tasks:
Create a NumPy array
Find the total sales
Find the average sales
"""
import numpy as np
# Create a NumPy array containing daily sales for 6 days
daily_sales = np.array([120, 150, 180, 200, 170, 160])
# Print the array
print("Daily sales for 6 days:", daily_sales)
# Find the total sales
total_sales = np.sum(daily_sales)
print("Total sales for 6 days:", total_sales)
# Find the average sales
average_sales = np.mean(daily_sales)
print("Average sales for 6 days:", average_sales)