# Function to find the maximum of two numbers

def max(a,b):    #defining a function to identify maximum of two numbers.
    if a>b:       #checking wether a is maximum.
        print(a,"is greater than",b)
    elif a<b:    #checking wether b is maximum.
        print(b,"is greater than",a)
    else:
        print("Both numbers are equal")    #both numbers are equal.


max(10,20)    #calling function