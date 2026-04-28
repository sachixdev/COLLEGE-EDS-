"""Product prices:
100, 200, 300, 400
Tasks:
Increase all prices by 10%
Print new prices
Real-world idea: Inflation or tax increase
"""
import numpy as np
# Create a NumPy array containing product prices
prices = np.array([100, 200, 300, 400])
# Print the original prices
print("Original prices:", prices)
# Increase all prices by 10%
new_prices = prices * 1.10
# Print the new prices
print("New prices after 10% increase:", new_prices)
