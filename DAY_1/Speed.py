#Calculate the speed of an object given the distance it has traveled and the time it took to travel that distance.
Dist=int(input("Enter the distance in meters: "))
time=int(input("Enter the time in seconds : "))
speed=Dist/time #calculating the speed by dividing the distance by the time
print("The speed is : ",speed,"m/s")
speed_kmh=speed*3.6 #converting the speed from meters per second to kilometers per hour by multiplying it by 3.6
print("The speed is : ",speed_kmh,"km/h")
