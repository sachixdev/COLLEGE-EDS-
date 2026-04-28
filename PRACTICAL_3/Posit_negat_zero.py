## Write a Python program to check whether a number is positive, negative or zero.

def Number(num):    #defining a function with single parameter num
    num=int(input("Enter a number : "))     #Taking input from the user
    if num>0:    #checking wether number is positive.
        print(num,"is a positive number.")
    elif num<0:   #checking wether number is negative.
        print(num,"is a negative number.")
    else:
        print("The number is zero.")     #number is zero.

Number(9)    #calling function 