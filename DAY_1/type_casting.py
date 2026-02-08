# This program demonstrates type casting in Python by converting a string representation of a number into various data types (integer, float, string, complex, and boolean) and printing the results along with their types.
num="23456"
num_int=int(num)  # converting the string representation of the number into an integer using the int() function
print("The number after type casting is : ",num_int)
print("The type of the number after type casting is : ",type(num_int)) # printing the type of the number after type casting using the type() function
num_float=float(num)
print("The number after type casting is : ",num_float)
print("The type of the number after type casting is : ",type(num_float))
num_str=str(num)
print("The number after type casting is : ",num_str)  # converting the string representation of the number into a string using the str() function (this will not change the value but will ensure it is treated as a string)
print("The type of the number after type casting is : ",type(num_str))
num_complex=complex(num)
print("The number after type casting is : ",num_complex)
print("The type of the number after type casting is : ",type(num_complex))
num_bool=bool(num) # converting the string representation of the number into a boolean using the bool() function (this will return True for any non-empty string and False for an empty string)
print("The number after type casting is : ",num_bool)
print("The type of the number after type casting is : ",type(num_bool))
