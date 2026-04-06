"""Students scored:
55, 65, 75, 85, 95
Tasks:
Add 5 grace marks to all students
Find the new average
Find the highest score
Real-world idea: Teacher adding grace marks
"""
import numpy as np
# Create a NumPy array containing marks of students
marks = np.array([55, 65, 75, 85, 95])
# Print the original marks
print("Original marks of students:", marks)
# Add 5 grace marks to all students
new_marks = marks + 5
# Print the new marks
print("New marks of students after adding grace marks:", new_marks)
# Find the new average
new_average = np.mean(new_marks)
print("New average marks of students:", new_average)
# Find the highest score
highest_score = np.max(new_marks)
print("Highest score after adding grace marks:", highest_score)
