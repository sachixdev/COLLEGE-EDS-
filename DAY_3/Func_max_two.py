# Function to find the maximum of two numbers

def max(a,b):
    if a>b:
        print(a,"is greater than",b)
    elif a<b:
        print(b,"is greater than",a)
    else:
        print("Both numbers are equal")


max(10,20)