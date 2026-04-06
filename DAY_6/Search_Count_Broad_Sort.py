"""The given code in the editor takes a single array, array1, as space-separated integers as input from the user. Additionally, it takes the following inputs:
search_value: The value to search for in the array.
count_value: The value to count its occurrences in the array.
broadcast_value: The value to add for broadcasting across the array.
You need to complete the code to perform the following operations:
"""
import numpy as np
# Take input for the array
array1 = np.array(list(map(int, input("Enter space-separated integers for the array: ").split())))
# Take input for search_value, count_value, and broadcast_value
search_value = int(input("Enter the value to search for in the array: "))
count_value = int(input("Enter the value to count its occurrences in the array: "))
broadcast_value = int(input("Enter the value to add for broadcasting across the array: "))
# Search for the search_value in the array
search_result = np.where(array1 == search_value)[0]
if search_result.size > 0:
    print(f"Value {search_value} found at indices: {search_result}")
else:
    print(f"Value {search_value} not found in the array.")
# Count the occurrences of count_value in the array
count_result = np.sum(array1 == count_value)
print(f"Value {count_value} occurs {count_result} times in the array.")
# Add broadcast_value to each element in the array
broadcast_result = array1 + broadcast_value
print(f"Array after broadcasting {broadcast_value} across it: {broadcast_result}")
