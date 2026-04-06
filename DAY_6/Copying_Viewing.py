"""The given code takes a list of integers as input and converts it into a NumPy array. Your task is to complete the code by:
Creating a view of the original_array and assigning it to view_array.
Creating a copy of the original_array and assigning it to copy_array.
After completing these steps, observe how modifying the view affects the original_array, while modifying the copy does not.
"""
import numpy as np
# Take input for the original array
original_array = np.array(list(map(int, input("Enter space-separated integers for the original array: ").split())))
# Create a view of the original array
view_array = original_array.view()
# Create a copy of the original array
copy_array = original_array.copy()
# Modify the view array
view_array[0] = -1  # Modifying the first element of the view array
# Modify the copy array
copy_array[0] = -2  # Modifying the first element of the copy array
# Print the original array, view array, and copy array to observe the effects
print("Original array after modifying view:", original_array)
print("View array:", view_array)
print("Copy array:", copy_array)
