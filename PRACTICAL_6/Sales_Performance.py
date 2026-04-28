"""Problem Statement
A company tracks sales of 3 products across 3 regions:
Matrix A → Sales in Quarter 1 
Matrix B → Sales in Quarter 2 
Each:
Row → Region 
Column → Product
Tasks
Write a NumPy program to:
Find total sales across both quarters 
Find growth in sales (Q2 − Q1) 
Compute average sales per product (column-wise) 
Find the region with highest total sales in Q2 
Transpose Matrix B to view product-wise regional sales

"""
import numpy as np
# Create NumPy arrays for sales in Quarter 1 and Quarter 2
sales_q1 = np.array([[100, 150, 200],
                    [80, 120, 160],
                    [90, 130, 170]])
sales_q2 = np.array([[110, 160, 210],
                    [85, 125, 165],
                    [95, 135, 175]])
# Find total sales across both quarters
total_sales = sales_q1 + sales_q2
print("Total sales across both quarters:\n", total_sales)
# Find growth in sales (Q2 − Q1)
growth_in_sales = sales_q2 - sales_q1
print("Growth in sales (Q2 − Q1):\n", growth_in_sales)
# Compute average sales per product (column-wise)
average_sales_per_product = np.mean(total_sales, axis=0)
print("Average sales per product (column-wise):", average_sales_per_product)
# Find the region with highest total sales in Q2
total_sales_q2 = np.sum(sales_q2, axis=1)
region_with_highest_sales_q2 = np.argmax(total_sales_q2)
print("Region with highest total sales in Q2 (0-indexed):", region_with_highest_sales_q2)
# Transpose Matrix B to view product-wise regional sales
transposed_sales_q2 = sales_q2.T
print("Transposed Matrix B (product-wise regional sales):\n", transposed_sales_q2)
