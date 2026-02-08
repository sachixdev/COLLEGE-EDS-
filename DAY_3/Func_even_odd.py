# Function to check if a number is even or odd

num=int(input("Enter a number : "))
def even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
print(even_odd(num))