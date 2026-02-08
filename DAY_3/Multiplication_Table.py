#Write a program to print multiplication table of a given number.
num=int(input("Enter a number to generate multiplication table: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
    i+=1
