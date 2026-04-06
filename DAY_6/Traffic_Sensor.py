"""A smart traffic system collects data from road sensors every hour.Each sensor record contains:
Angle of vehicle movement (in degrees) → used to analyze direction 
Speed values (km/h) → used for traffic analysis 
Status flags (integers) → represent conditions: 
Bit 0 (1) → Vehicle detected 
Bit 1 (2) → Overspeeding 
Given three NumPy arrays:
Convert angles to radians and compute sine values 
Compute average speed of vehicles 
Use bitwise operation to check: 
Which vehicles are detected (flag & 1)
"""
import numpy as np
# Sample data for angles, speeds, and status flags
angles_degrees = np.array([0, 90, 180, 270])
speeds_kmh = np.array([60, 80, 100, 120])
status_flags = np.array([1, 3, 0, 2])  # Example flags for 4 vehicles
# Convert angles to radians and compute sine values
angles_radians = np.radians(angles_degrees)
sine_values = np.sin(angles_radians)
print("Sine values of angles in radians:", sine_values)
# Compute average speed of vehicles
average_speed = np.mean(speeds_kmh)
print("Average speed of vehicles (km/h):", average_speed)
# Use bitwise operation to check which vehicles are detected (flag & 1)
vehicles_detected = (status_flags & 1) == 1
