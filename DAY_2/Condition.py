import math
num=int(input("Enter a number : "))
if 0<=num<10:
    square=math.pow(num,2)
    print("The square of the number is : ",square)
elif 10<=num<100:
    square_root=math.sqrt(num)
    print("The square root of the number is : ",square_root)
elif 100<=num<1000:
    cube_root=math.cbrt(num)
    print("The cube of the number is : ",cube_root)
else:
    print("The number is out of range")