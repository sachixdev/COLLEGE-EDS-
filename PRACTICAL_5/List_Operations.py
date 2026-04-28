# List operations and management

numbers = []   #initializing an empty list to store numbers
while(True):     #infinite loop to continuously prompt the user for input until they choose to quit
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")


	ch=input("Enter choice: ")    #taking input from the user for the desired operation
	if(ch=='1'):     #if the user chooses to add a number to the list
		a=input("Integer: ")
		if a.lstrip('-').isdigit():     #checking if the input is a valid integer (including negative numbers)
			num=int(a)
			numbers.append(num)    #adding the valid integer to the list
			print("List after adding:",numbers)
		else:  
			print("Invalid input")      #if the input is not a valid integer, print an error message
	elif ch=='2':
		if not numbers:   
			print("List is empty")
		else:
			a = input("Integer: ")
			if a.lstrip('-').isdigit():
				num=int(a)
				if num in numbers:
					numbers.remove(num)    #removing the specified number from the list if it exists
					print("List after removing:",numbers)
				else:
					print("Element not found")
			else:
				print("Invalid input")
	elif ch=='3':
		if not numbers:
			print("List is empty")
		else:
			print(numbers)
	elif ch=='4':
		break    #if the user chooses to quit, break the loop and end the program
	else:
		print("Invalid choice")
	
