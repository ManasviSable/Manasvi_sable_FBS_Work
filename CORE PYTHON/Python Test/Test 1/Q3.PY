#Write a program to accept distance in km and convert it into meters and centimeters both.
km = float(input("Enter the distance in kilometers: "))
meters = km * 1000
centimeters = km * 100000
print("The distance in meters is:", meters)
print("The distance in centimeters is:", centimeters)