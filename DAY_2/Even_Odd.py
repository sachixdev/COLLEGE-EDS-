#Check whether a number is even or odd
num=int(input("Enter a number : "))  #takes input from the user

if num%2==0:  #checks if the number is divisible by 2 with no remainder, which indicates that it is an even number
    print(num," is even number.")
else:
    print(num," is odd number.") #if the number is not divisible by 2 with no remainder, it is an odd number, and the program prints that it is an odd number.