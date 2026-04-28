#Calculating total and average marks using a for loop
marks = [78,85,63,90,88]      #list of marks
total = 0      #variable to store total marks
for mark in marks:     #loop to traverse the marks list
    total += mark
average = total / len(marks)      #calculating average marks by dividing total by the number of marks
print("Total marks: ", total)
print("Average marks: ", average)     #printing total and average marks