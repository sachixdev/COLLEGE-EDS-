"""Normalize Sales Data Using Z-Score Standardization
A company tracks the monthly sales performance of its employees across different product categories. However, each category has different sales ranges, making it hard to compare employee performance fairly.
To standardize the data, the company wants to normalize each category using Z-score normalization.

"""
import numpy as np
# Sample sales data for 5 employees across 3 product categories
sales_data = np.array([[200, 500, 300],
                        [150, 450, 250],
                        [300, 600, 400],
                        [250, 550, 350],
                        [180, 480, 280]])
# Print original sales data
print("Original Sales Data:\n", sales_data)
# Function to perform Z-score normalization
def z_score_normalization(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    normalized_data = (data - mean) / std
    return normalized_data
# Normalize the sales data using Z-score normalization
normalized_sales_data = z_score_normalization(sales_data)
# Print normalized sales data
print("Normalized Sales Data (Z-score):\n", normalized_sales_data)
