#Find the sum of all the even numbers from 1 to n.
sum=0    #initilizating sum is equal to 0
i=0
num=int(input("Enter a number :"))   #Taking input from the user 
for i in range(0,num+1,2):   #for loop starts from 0,ends in num+1 and move forvard by two steps
    sum+=i    #sum=sum+i
print("The sum of all even numbers from 1 to",num,"is :",sum)   #printing the sum

#Alternative way 
sum=0
i=1
num=int(input("Enter a number :"))
for i in range(1,num+1):
    if i%2==0:   #By checking even number
        sum+=i
print("The sum of all the even numbers from 1 to",num,"is :",sum)