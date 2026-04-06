"""Write a Python program that creates different NumPy arrays and demonstrates how to use the attributes ndim, shape, and size. The program should display:
The number of dimensions of the array (ndim)
The shape of the array (shape)
The total number of elements in the array (size)
"""
import numpy as np
# Create a 1D NumPy array
array_1d = np.array([1, 2, 3, 4, 5])
# Create a 2D NumPy array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# Create a 3D NumPy array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# Display attributes for 1D array
print("1D Array:", array_1d)
print("Number of dimensions (ndim):", array_1d.ndim)
print("Shape of the array (shape):", array_1d.shape)
print("Total number of elements (size):", array_1d.size)
# Display attributes for 2D array
print("\n2D Array:\n", array_2d)
print("Number of dimensions (ndim):", array_2d.ndim)
print("Shape of the array (shape):", array_2d.shape)
print("Total number of elements (size):", array_2d.size)
# Display attributes for 3D array
print("\n3D Array:\n", array_3d)

print("Number of dimensions (ndim):", array_3d.ndim)
print("Shape of the array (shape):", array_3d.shape)
print("Total number of elements (size):", array_3d.size)
