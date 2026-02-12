from datetime import datetime    #importing datetime function from the datetime module.
birth=int(input("Enter the Birth year : "))   #taking birth year of the user
current=datetime.now().year   #fetching current year 
age=current-birth      #calculating the age of the user by subtracting current year-birth year.
print("Your current age is : ",age)     #printing the age