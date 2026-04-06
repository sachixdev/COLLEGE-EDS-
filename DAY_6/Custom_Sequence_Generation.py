"""Write a Python program that takes the following inputs from the user:
Start value: The starting point of the sequence.
Stop value: The sequence should end before this value.
Step value: The increment between each number in the sequence.
The program should then generate a sequence using numpy based on these inputs and print the generated sequence.
"""
import numpy as np
# Take inputs from the user
start_value = int(input("Enter the start value: "))
stop_value = int(input("Enter the stop value: "))
step_value = int(input("Enter the step value: "))
# Generate the sequence using numpy
sequence = np.arange(start_value, stop_value, step_value)
# Print the generated sequence
print("Generated sequence:", sequence)
