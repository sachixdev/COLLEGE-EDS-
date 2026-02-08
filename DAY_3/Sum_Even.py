#Find the sum of all the even numbers from 1 to n.
sum=0
i=0
num=int(input("Enter a number :"))
for i in range(0,num+1,2):
    sum+=i
print("The sum of all even numbers from 1 to",num,"is :",sum)

#Alternative way 
sum=0
i=1
num=int(input("Enter a number :"))
for i in range(1,num+1):
    if i%2==0:
        sum+=i
print("The sum of all the even numbers from 1 to",num,"is :",sum)