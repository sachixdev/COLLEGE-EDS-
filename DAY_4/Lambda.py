num=int(input("Enter the number : "))   #taking input from the user.
a=lambda num : num**2   #lambda function for square of number.
print("Square of number is ",a(num))   #calling function and passing argument num.
check=lambda num:"Positive" if num>0 else"Negative" if num<0  else "zero"   #lambda function for checking number is positive ,negative or zero.

print(check(num))   #calling function and passing argument num.