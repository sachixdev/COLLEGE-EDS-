# Tuple operations and statistics
marks = (23,45,67,89,90)
print("Student Marks : ")
for i in marks:
    print(i)

total = 0
for i in marks:      #loop to calculate total marks by iterating through the marks set
    total += i
    average = total / len(marks)     #calculating average marks by dividing total by the number of marks in the set
print("Total Marks : ", total) 
print("Average Marks : ", average)
highest = max(marks)      #calculating highest marks using max function 
lowest = min(marks)        #calculating lowest marks using min function 
print("Highest Marks : ", highest)
print("Lowest Marks : ", lowest)

count = 0    
for i in marks:   #count number of students scoring above average marks
    if i>average:
        count += 1
print("Student scoring above average : ", count)   