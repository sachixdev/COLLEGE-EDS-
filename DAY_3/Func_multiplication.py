# Function to print multiplication table of a given number

def multiplication(a):
    for i in range(1,11):
        print(a,"x",i,"=",a*i)
        i+=1

multiplication(5)