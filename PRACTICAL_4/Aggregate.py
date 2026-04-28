def cal(course,marks):   #Defining a function which takes no. of course and marks as a parameter.
    if any(mark<40 for mark in marks):   #any is a key word that iterate each element and check condition of fail for each input of marks.
        return "Fail"
    total_marks=sum(marks)  #sum is a built in function adding all the marks.
    agg=total_marks*100/(course*100)    #calculates the aggregate function.
    print(f"Aggregated Percentage:{agg:2f}")   # aggregating function upto two decimal after point.
    if(agg>=75):           #if else conditions for checking its grade.
        return "Distinction"
    elif(75<agg>=60):
        return "First class"
    elif(60<agg>=50):
        return "Second class"
    else:
        return "Third class"
    
n=int(input("Enter the number of courses : ")) 
mark=list(map(int,input("Enter the marks of the courses : ").split()))   #spliting input and converting it into list
print(cal(n,mark))    #calling function
    



