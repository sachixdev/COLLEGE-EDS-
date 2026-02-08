#Write a python program to print a right angled triangle pattern of numbers.

num=int(input("Enter a numbers of rows :" ))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")  #print in a same line.
    
    print() #print in a new line.
    
    i+=1