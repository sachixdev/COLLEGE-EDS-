# Write a function to find the greatest of three numbers.

def Greatest_of_3(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>a and a>b:
        return c
    else:
        return "All are equal"

print(Greatest_of_3(100,2000,200))   