#Check  a number is prime or not
num=int(input("Enter a number : "))   #taking input from the user
if num<1:   #if number is less than 1 is not a prime number.
    print("Enter a valid positive number.")
else:
    for i in range(2,num):     #prime number starts from 2   #applying for loop
        if num%i==0:    
            print(num,"is not a prime number.")
        break      #Break will terminate the loop and exit from the loop
    else:
        print(num,"is a prime number.")    