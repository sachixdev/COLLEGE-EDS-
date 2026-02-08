#Print fibonacci series up to n terms using recursive function
def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
n=int(input("Enter how many terms : "))
print("Fibonacci Series : ")

for i in range(n):
    print(Fibonacci(i),end=" ")

