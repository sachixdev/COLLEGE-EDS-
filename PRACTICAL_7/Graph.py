import matplotlib.pyplot as plt  # Importing the matplotlib library for plotting

labels = ['A','B','C']# Define the labels for the pie chart
sizes = [40,35,25]# Define the sizes for each slice of the pie chart

plt.pie(sizes, labels=labels, autopct='%1.1f%%')# Create a pie chart with the specified sizes and labels, and display the percentage on each slice

plt.title("Pie Chart")# Set the title of the pie chart

plt.show()# Display the pie chart

 