num1 = float(input("Enter a 1st number : "))
num2 = float(input("Enter a 2nd number : "))
num3 = float(input("Enter a 3rd number : "))

# 1st way
if(num1>num2):
    if(num1>num3):
        print(num1," is greater.")
if(num2>num1):
    if(num2>num3):
        print(num2," is greater.")
if(num3>num1):
    if(num3>num2):
        print(num3," is greater.")

# 2nd way
if(num1>num2):
    if(num1>num3):
        print(num1," is greater.")
    else:
        print(num3," is greater.")
elif(num2>num1):
    if(num2>num3):
        print(num2," is greater.")
    else:
        print(num3," is greater.")
else:
    print("Enter valid numbers.")
