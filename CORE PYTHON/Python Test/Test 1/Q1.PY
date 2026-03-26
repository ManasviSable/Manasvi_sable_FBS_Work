#Calculare area and circumference of rectangle with circle in one of its breadth
l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
r = b / 2
area_rectangle = l * b
circumference_rectangle = 2 * (l + b)
area_circle = 3.14 * r * r
circumference_circle = 2 * 3.14 * r
total_area = area_rectangle + area_circle
total_circumference = circumference_rectangle + circumference_circle
print("The area of the rectangle is:", area_rectangle)