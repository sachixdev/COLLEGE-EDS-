# Linear Search Algorithm
def linear_search(arr,key):    #function to perform linear search
    for i in range(len(arr)):     #loop to traverse the array
        if arr[i] == key:
            return i          #if key is found return the index
    return -1
arr = list(map(int,input("Enter the elements of the array: ").split()))  #taking input of the array
key = int(input())
result = linear_search(arr,key)    #calling the linear search function and storing the result
if result != -1:            #if the result is not -1 then the key is found and we print the index
    print(result)
else:
    print("Not Found")



  