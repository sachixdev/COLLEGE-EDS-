"""An image can be represented as a matrix of pixel values (0–255).
Given a 5×5 grayscale image matrix, perform:
Increase brightness by adding 30
Ensure values do not exceed 255
Find the average brightness

"""
import numpy as np
# Create a 5×5 grayscale image matrix with pixel values between 0 and 255
image_matrix = np.array([[100, 150, 200, 250, 255],
                            [50, 75, 125, 175, 225],
                            [0, 25, 255, 255, 255],
                            [255, 255, 255, 255, 255],
                            [255, 255, 255, 255, 255]])
# Print the original image matrix
print("Original image matrix:\n", image_matrix)
# Increase brightness by adding 30 and ensure values do not exceed 255
brightened_image = np.clip(image_matrix + 30, 0, 255)
# Print the brightened image matrix
print("Brightened image matrix:\n", brightened_image)
# Find the average brightness of the brightened image
average_brightness = np.mean(brightened_image)
print("Average brightness of the brightened image:", average_brightness)
