#Reverse a number
num=input("Enter a number to be reversed : ")  #taking input from the user as a string to preserve leading zeros if any
reversed_num=num[ : : -1]   #reversing the number by slicing the string with a step of -1
print("The reversed number is : ",reversed_num)  #printing the reversed number to the user
print("The type of the reversed number is : ",type(reversed_num))   #printing the type of the reversed number to the user, which will be a string since we reversed it as a string.
