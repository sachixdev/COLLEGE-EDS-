# This program categorizes a person's age into different life stages (toddler, child, teenager, youth, senior citizen) based on the age input provided by the user.
age=int(input("Enter your age : "))  # taking input from the user and converting it to an integer
if 0<=age<5:  # checking if the age is between 0 and 5 (inclusive of 0 and exclusive of 5) to categorize the person as a toddler
    print("You are a toddler.")
elif 5<=age<12:
    print("You are a child.")
elif 12<=age<20:
    print("You are a teenager.")  # checking if the age is between 12 and 20 (inclusive of 12 and exclusive of 20) to categorize the person as a teenager
elif 20<=age<50:
    print("You are a Youth.")
else:
    print("You are a senior citizen")  # if the age is 50 or above, categorizing the person as a senior citizen
