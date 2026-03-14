# Dictionary operations: insertion, update, deletion, and traversal

student = {     #initializing a dictionary with student IDs as keys and their names as values
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

print("Original Dictionary:",student)    #printing the original dictionary of student IDs and names
key =int( input())
value = input()
student[key] = value   #insertig a new key value pair into dictionary
print("After Insertion:",student)
key = int(input())
value = input()
if key in student:   #checking if the specified key exists in the dictionary and if it does, updating its value
	student.update({key: value})

print("After Update:",student)
key = int(input())
if key in student:    #checking and deleting a key-value pair from the dictionary if the specified key exists
	student.pop(key)

print("After Deletion:",student)
print("Traversing Dictionary:")   #Traversing the dictionary and printing each key-value pair in the format "key: value"
for k,v in student.items():
	print(k, ":",v)
