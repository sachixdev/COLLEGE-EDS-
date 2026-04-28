# Student marks management using list operations
marks = [67,78,89,90,98]        #list of marks
print(marks)
marks[2]=76     #updating the marks at index 2 to 76
print("After updating marks: ",marks) 
marks.insert(1,80)    #inserting marks 80 at index 1
print("After inserting marks: ",marks)
marks.remove(67)    #removing marks 67 from the list
print("After removing marks: ",marks)
marks.pop(1)     #removing marks at index 1 using pop method
print("After popping marks: ",marks)
print("Final marks: ",marks)