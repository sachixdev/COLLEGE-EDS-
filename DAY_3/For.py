#For loop in python
i=1  #initializing a variable i to 1, which will be used as the starting point for the loop.
num=int(input("Enter a number : "))   
for i in range(1, num):   
    print(i, end=" ")   #print numbers in the same line
print("\nDone!")  

# Alternative way to print numbers in new lines
i=1
for i in range(1, num):    #looping through numbers from 1 to num-1 using the range() function
    print(i)
print("Done!")