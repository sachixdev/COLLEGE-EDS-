"""Calculate the total marks of each student in each subject across both exams. 
Determine the improvement or decline in marks from Midterm to Final. 
Analyze the consistency of performance in each subject. 
Perform overall performance analysis by combining both datasets. 
Convert the data to view it subject-wise instead of student-wise.
"""
import numpy as np
# Create 2D NumPy arrays for Midterm and Final marks
midterm_marks = np.array([[80, 85, 90],
                        [70, 75, 80],
                        [90, 88, 95]])
final_marks = np.array([[85, 90, 95],
                        [75, 80, 85],
                        [92, 90, 98]])
# Calculate total marks for each student in each subject across both exams
total_marks = midterm_marks + final_marks
print("Total marks for each student in each subject across both exams:\n", total_marks)
# Determine improvement or decline in marks from Midterm to Final
improvement_decline = final_marks - midterm_marks
print("Improvement or decline in marks from Midterm to Final:\n", improvement_decline)
# Analyze consistency of performance in each subject
consistency = np.std(total_marks, axis=0)
print("Consistency of performance in each subject (standard deviation):", consistency)
# Perform overall performance analysis by combining both datasets
overall_performance = np.mean(total_marks, axis=0)
print("Overall performance by subject (average marks):", overall_performance)
# Convert the data to view it subject-wise instead of student-wise
subject_wise_marks = total_marks.T
print("Subject-wise marks (transposed):\n", subject_wise_marks)
