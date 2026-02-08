# Function to check if a number is even or odd

num=int(input("Enter a number : "))    #Taking input from the user and type casting into integer.
def even_odd(num):    #defining a function give num as a parameter.
    if num%2==0:    #checking condition wether number is even or odd.
        return "Even"
    else:
        return "Odd"
print(even_odd(num))    #Calling function and printing the output.