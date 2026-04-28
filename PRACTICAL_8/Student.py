import pandas as pd   # Importing the pandas library for data manipulation and analysis

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])   # Assuming the file has three columns: Name, Age, and Grade, separated by whitespace


# write your code here..

print("First five rows:")
print(data.head())   # Display the first five rows of the DataFrame
avg_age = round(data["Age"].mean(),2)
print("Average age:",avg_age)
filtered = data[data["Grade"]<="B"]  # Filter the DataFrame to include only students with a grade of B or lower (assuming grades are ordered such that A < B < C, etc.)
print("Students with a grade up to B")

print(filtered)  # Display the filtered DataFrame