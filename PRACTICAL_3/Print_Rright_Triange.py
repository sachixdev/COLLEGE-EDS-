#write a python program to print a pattern of right angle triangle in the form of a right angled triangle
num=int(input("Enter the number of rows : "))
#1st way to print right angle triangle
i=1
for i in range(1,num+1):     #general easy way by using for loop
    print("*"*i)
    i+=1

#2nd way to print right angle triangle
i=1
for i in range(1,num+1):     #by using nested for loop 
    for j in range(1,i+1):    #for mostly pattern printing nested loop is used.
        print("*",end="")
    print()  #print new line after each row
    i+=1