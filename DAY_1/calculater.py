# This program performs basic arithmetic operations (addition, subtraction, multiplication, division, modulus, exponentiation, and floor division) on two numbers provided by the user.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2
print("The sum of two numbers is : ",sum)
diff=num1-num2 #calculating the difference of two numbers by subtracting the second number from the first number
print("The differnce of two numbers is : ",diff)
prod=num1*num2 #calculating the product of two numbers by multiplying the first number with the second number
print("The product of two numbers is: ",prod)
div=num1/num2 #calculating the division of two numbers by dividing the first number by the second number
print("The division of two numbers is : ",div)
mod = num1%num2 #calculating the modulus of two numbers by finding the remainder when the first number is divided by the second number
print("The modulus of two numbers is : ",mod)
exp =num1**num2 #calculating the exponentiation of two numbers by raising the first number to the power of the second number
print("The exponential value is : " ,exp)
floor = num1//num2 # calculating the floor division of two numbers by dividing the first number by the second number and rounding down to the nearest integer
print("The floor division value is : ",floor)
