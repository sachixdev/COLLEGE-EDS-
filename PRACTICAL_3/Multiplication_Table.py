#Write a program to print multiplication table of a given number.
num=int(input("Enter a number to generate multiplication table: "))   #Taking input
for i in range(1,11):   #appling for loop in range 1 to 11
    print(num,"x",i,"=",num*i)    #printing multiplication table
    i+=1   #incrementing by 1
