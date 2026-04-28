"""Create a NumPy array of even numbers from 2 to 20.
Tasks:
Print the array
Find the sum of all numbers
Find the mean

"""
import numpy as np
# Create a NumPy array of even numbers from 2 to 20
even_numbers = np.arange(2, 21, 2)
# Print the array
print("Even numbers from 2 to 20:", even_numbers)
# Find the sum of all numbers
sum_even_numbers = np.sum(even_numbers)
print("Sum of all even numbers from 2 to 20:", sum_even_numbers)
# Find the mean
print("Mean of even numbers from 2 to 20:", np.mean(even_numbers))