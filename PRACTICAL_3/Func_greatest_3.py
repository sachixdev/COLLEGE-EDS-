# Write a function to find the greatest of three numbers.

def Greatest_of_3(a,b,c):   #Defining a function for greatest number
    if a>b and a>c:     #checking wether a the greatest number.
        return a
    elif b>c and b>a:    #checking wether b the greatest number.
        return b
    elif c>a and a>b:    #checking wether c the greatest number.
        return c
    else:
        return "All are equal"   

print(Greatest_of_3(100,2000,200))      #Calling function
