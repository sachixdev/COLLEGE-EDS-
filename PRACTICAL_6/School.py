"""A school maintains student records for different classes and subjects.
Matrix A contains marks of students in Math and Science 
Matrix B contains marks of the same students in English and History 
Each matrix has:
Rows → Students 
Columns → Subjects 
Additionally, the school has another class:
Matrix C contains marks of Class B students in Math and Science
Tasks
Write a Python program using NumPy to:
 Combine subjects → create a full subject record for each student
Combine students → create a dataset of all students
Write a Python program using NumPy to:
Perform Horizontal Stacking of Matrix A and Matrix B 
Combine subjects → create a full subject record for each student 
Perform Vertical Stacking of Matrix A and Matrix C 
Combine students → create a dataset of all students
"""
import numpy as np
# Create NumPy arrays for marks of students in Math and Science (Matrix A) and English
# and History (Matrix B)
print("Enter values for Matrix A (Math and Science marks):")
arr1 = []
for i in range(3):
    row = list(map(int, input(f"Enter marks for student {i + 1} (Math and Science): ").split()))
    arr1.append(row)
matrix_a = np.array(arr1)
print("\nEnter values for Matrix B (English and History marks):")
arr2 = []
for i in range(3):
    row = list(map(int, input(f"Enter marks for student {i + 1} (English and History): ").split()))
    arr2.append(row)
matrix_b = np.array(arr2)
# Create NumPy array for marks of Class B students in Math and Science (Matrix C)
print("\nEnter values for Matrix C (Math and Science marks for Class B students):")
arr3 = []
for i in range(3):
    row = list(map(int, input(f"Enter marks for Class B student {i + 1} (Math and Science): ").split()))
    arr3.append(row)
matrix_c = np.array(arr3)
# Perform Horizontal Stacking of Matrix A and Matrix B
horizontal_stacked = np.hstack((matrix_a, matrix_b))
print("\nHorizontal Stacking (full subject record for each student):\n", horizontal_stacked)
# Perform Vertical Stacking of Matrix A and Matrix C
vertical_stacked = np.vstack((matrix_a, matrix_c))
print("\nVertical Stacking (dataset of all students):\n", vertical_stacked)
