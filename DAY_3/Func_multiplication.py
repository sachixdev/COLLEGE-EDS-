# Function to print multiplication table of a given number

def multiplication(a):     #defining a function of multiplication 
    for i in range(1,11):    #applying for loop of range 1 to 11
        print(a,"x",i,"=",a*i)    #printing multiplication table
        i+=1     #increment by 1

multiplication(5)   #calling function