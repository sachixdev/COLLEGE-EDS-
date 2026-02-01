age=int(input("Enter your age : "))
if 0<=age<5:
    print("You are a toddler.")
elif 5<=age<12:
    print("You are a child.")
elif 12<=age<20:
    print("You are a teenager.")
elif 20<=age<50:
    print("You are a Youth.")
else:
    print("You are a senior citizen")
