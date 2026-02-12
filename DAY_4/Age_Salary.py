from datetime import datetime   #importing datetime function from the datetime module 
def Age(Birth_date):    #defining a function age with parameter Birth_date
    birth_year=int(Birth_date.split("-")[-1])   #first spliting the date of birth by - and then fetching the last element i.e. year and then converting it into the integer.
    current_year=datetime.now().year   #fetching the current date and reading only the current year
    return current_year-birth_year     #calculating the age

def Salary(salary_rupees):      #defining the function salary that converts indian rupees into USD.
    usd=salary_rupees*0.012     #1 INR = 0.012 USD
    return usd

Birth_date=input("Enter the Date of Birth in the form DD-MM-YY : ")    #taking input of the birth date of the user
salary_rupees=int(input("Enter the amount of salary in rupees : "))   

print(Age(Birth_date))
print(Salary(salary_rupees))    #calling functions