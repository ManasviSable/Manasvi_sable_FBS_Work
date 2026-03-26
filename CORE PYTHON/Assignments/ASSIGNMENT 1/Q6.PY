#Write a Program to input two angles from user and find third angle of the triangle.
a = int(input("Enter the first angle of triangle in degrees:"))
b = int(input("Enter the second angle of triangle in degrees:"))
c = 180 - (a + b)
print("The third angle of triangle is:", c, "degrees")