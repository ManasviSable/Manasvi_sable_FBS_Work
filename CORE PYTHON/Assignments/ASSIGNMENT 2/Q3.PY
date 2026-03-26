#Convert distance given in feet and inches into meter and centimeter.
print("Enter distance in feet and inches")
feet = int(input("Enter number of feet:"))
inches = int(input("Enter number of inches:"))
distance = feet * 12 + inches
meter = distance * 0.0254
centimeter = meter * 100
print("Distance in meter is:", meter ,"m")
print("Distance in centimeter is:", centimeter ,"cm")