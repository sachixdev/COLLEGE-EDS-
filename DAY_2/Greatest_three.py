#Identify the greatest of three numbers
num1 = float(input("Enter a 1st number : "))  #Taking input in float values from the user
num2 = float(input("Enter a 2nd number : "))
num3 = float(input("Enter a 3rd number : "))

# 1st way
if(num1>num2):    #checking if num1 is greater than num2
    if(num1>num3):   #checking if num1 is greater than num3
        print(num1," is greater.")
if(num2>num1):
    if(num2>num3):
        print(num2," is greater.")   #checking if num2 is greater than num1 and num3
if(num3>num1):
    if(num3>num2):
        print(num3," is greater.")

# 2nd way 
if(num1>num2):
    if(num1>num3):
        print(num1," is greater.") #checking if num1 is greater than num2 and num3
    else:
        print(num3," is greater.")
elif(num2>num1):
    if(num2>num3):
        print(num2," is greater.")
    else:
        print(num3," is greater.")
else:
    print("Enter valid numbers.")  #if num1 is not greater than num2 and num2 is not greater than num1, it means that the numbers are equal or invalid, and the program prints a message asking the user to enter valid numbers.
