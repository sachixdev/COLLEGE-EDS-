#Print fibonacci series up to n terms using recursive function
def Fibonacci(n):   #difining a function
    if n==0:  # condition in function
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)    #recursive function calling function itself repeatedly
n=int(input("Enter how many terms : "))   #taking input from the user
print("Fibonacci Series : ")    

for i in range(n):    #appling for loop 
    print(Fibonacci(i),end=" ")   #printing fibonacci series in singal line.

