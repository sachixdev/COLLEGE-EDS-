#Count digits in a number .
count =0  #initializing a variable count to 0, which will be used to keep track of the number of digits in the input number.
num=int(input("Enter a number : "))   #taking input from the user and converting it to an integer using the int() function
for i in str(num):   #converting the input number to a string using the str() function, which allows us to iterate through each character (digit) in the number using a for loop.
    count+=1
print("The number of digits in the number is : ",count)   #printing the total count of digits in the input number to the user.
