# Dictionary operations and management
d={}   #initializing an empty dictionary to store key-value pairs
print("Empty Dictionary: {}")
n=int(input("Number of items: "))
for i in range(n):   #loop to take input of key-value pairs from the user and store them in the dictionary
    key=input("key: ")
    value=input("value: ")
    d[key]=value    #adding the key-value pair to the dictionary 
print("Dictionary:",d)

update_key=input("Enter the key to update: ")
if update_key in d:
    d[update_key]=input("Enter the new value: ")   #updating the value of the specified key in the dictionary
    print("Value updated")
else:
    print("Key not found")
retrieve_key=input("Enter the key to retrieve: ")
if retrieve_key in d:     #checking if the specified key exists in the dictionary and if it does, retrieving 
    print(f"Key: {retrieve_key}, Value: {d[retrieve_key]}")
else:
    print("Key not found")

get_key=input("Enter the key to get using the get() method: ")
if get_key in d:
    print(f"Key: {get_key}, Value: {d.get(get_key)}")    #using the get() method to retrieve the value of the specified key 
else:
    print("Key not found")
delete_key=input("Enter the key to delete: ")
if delete_key in d:   
    del d[delete_key]   #deleting the specified key-value pair from the dictionary if the key exists
    print("Deleted")
else:
    print("Key not found")

print("Updated Dictionary:",d)
