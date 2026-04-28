"""Sales for 3 stores over 4 days:
100 120 130 14090  110 115 120150 160 170 180

Tasks:
Find total sales per store
Find overall average sales
Real-world idea: Retail chain analysis
"""
import numpy as np
# Create a 2D NumPy array representing sales for 3 stores over 4 days
sales = np.array([[100, 120, 130, 140],
                    [90, 110, 115, 120],
                    [150, 160, 170, 180]])
# Print the array
print("Sales for 3 stores over 4 days:\n", sales)
# Find total sales per store
total_sales_per_store = np.sum(sales, axis=1)
print("Total sales per store:", total_sales_per_store)
# Find overall average sales
overall_average_sales = np.mean(sales)
print("Overall average sales:", overall_average_sales)
