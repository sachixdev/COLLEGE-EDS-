"""You are given two arrays A and B. Your task is to complete the function array_operations, which will convert these lists into NumPy arrays and perform the following operations:
1. Arithmetic Operations:
Compute the element-wise sum, difference, and product of the two arrays. 
2. Statistical Operations:
Calculate the mean, median, and standard deviation of array A. 
3. Bitwise Operations:
Perform bitwise AND, bitwise OR, and bitwise XOR on the arrays (ex: Aᵢ OR Bᵢ).
"""
import numpy as np
def array_operations(A, B):
    # Convert lists to NumPy arrays
    array_A = np.array(A)
    array_B = np.array(B)
    
    # Arithmetic Operations
    elementwise_sum = array_A + array_B
    elementwise_difference = array_A - array_B
    elementwise_product = array_A * array_B
    
    # Statistical Operations for array A
    mean_A = np.mean(array_A)
    median_A = np.median(array_A)
    std_dev_A = np.std(array_A)
    
    # Bitwise Operations
    bitwise_and = np.bitwise_and(array_A, array_B)
    bitwise_or = np.bitwise_or(array_A, array_B)
    bitwise_xor = np.bitwise_xor(array_A, array_B)
    
    return {
        "elementwise_sum": elementwise_sum,
        "elementwise_difference": elementwise_difference,
        "elementwise_product": elementwise_product,
        "mean_A": mean_A,
        "median_A": median_A,
        "std_dev_A": std_dev_A,
        "bitwise_and": bitwise_and,
        "bitwise_or": bitwise_or,
        "bitwise_xor": bitwise_xor
    }