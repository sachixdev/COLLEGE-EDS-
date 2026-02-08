## Write a Python program to check whether a number is positive, negative or zero.

def Number(num):
    num=int(input("Enter a number : "))
    if num>0:
        print(num,"is a positive number.")
    elif num<0:
        print(num,"is a negative number.")
    else:
        print("The number is zero.")

Number(9)