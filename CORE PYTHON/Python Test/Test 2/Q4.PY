#Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.
length = int(input("Enter the length of the wall: "))
width = int(input("Enter the width of the wall: "))
height = int(input("Enter the height of the wall: "))
area = 4 * (length * height) + 4 * (width * height)
cost_per_sqft = int(input("Enter the cost of painting per square foot: "))
total_cost = area * cost_per_sqft
print("The total cost of painting the interior of the building is:", total_cost)