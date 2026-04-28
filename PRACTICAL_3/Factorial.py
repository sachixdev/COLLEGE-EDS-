#print factorial of  number
def Factorial(n):   #defining a recursive function 
    if n==0 or n==1:    #base case: if n is 0 or 1, the factorial is 1, so the function returns 1
        return 1       
    else:
        return n*Factorial(n-1)     #recursive case: if n is greater than 1, the function calls itself with n-1 and multiplies the result by n to calculate the factorial of n
    
n=int(input("Enter a number to find factorial: "))
print(Factorial(n))     #taking input from the user, converting it to an integer, and then calling the Factorial function with the input number to calculate and print the factorial of that number.