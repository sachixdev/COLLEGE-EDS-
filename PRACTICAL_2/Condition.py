# This program takes a number as input from the user and performs different mathematical operations based on the range in which the number falls.
import math  # importing the math module to use mathematical functions like pow(), sqrt(), and cbrt()
num=int(input("Enter a number : "))   # taking input from the user and converting it to an integer using the int() function
if 0<=num<10:
    square=math.pow(num,2)  # calculating the square of the number using the pow() function from the math module, where the first argument is the base (the number) and the second argument is the exponent (2 for squaring)
    print("The square of the number is : ",square)
elif 10<=num<100:
    square_root=math.sqrt(num)   # calculating the square root of the number using the sqrt() function from the math module, which returns the non-negative square root of the number
    print("The square root of the number is : ",square_root)
elif 100<=num<1000:
    cube_root=math.cbrt(num)  # calculating the cube root of the number using the cbrt() function from the math module, which returns the cube root of the number
    print("The cube of the number is : ",cube_root)
else:
    print("The number is out of range")