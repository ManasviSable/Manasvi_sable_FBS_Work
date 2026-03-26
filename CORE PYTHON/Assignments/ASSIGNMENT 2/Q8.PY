#Write a program to swap two numbers using third variable.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = a
a = b
b = c
print("After swapping, first number is:", a)
print("After swapping, second number is:", b)