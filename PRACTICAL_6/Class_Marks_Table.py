"""Create a 2D array representing marks of 3 students in 3 subjects.
Math Science English80   85      9070   75      8090   88      95
Tasks:
Print the array
Find average marks of each student
Find highest marks in the class
"""
import numpy as np
# Create a 2D NumPy array representing marks of 3 students in 3 subjects
marks = np.array([[80, 85, 90],
                    [70, 75, 80],
                    [90, 88, 95]])
# Print the array
print("Marks of students in Math, Science, and English:\n", marks)
# Find average marks of each student
average_marks = np.mean(marks, axis=1)
print("Average marks of each student:", average_marks)
# Find highest marks in the class
highest_marks = np.max(marks)
print("Highest marks in the class:", highest_marks)
