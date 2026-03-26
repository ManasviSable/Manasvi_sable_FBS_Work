#Find the sum of three-digit number.
num = int(input("Enter a three-digit number in the form of abc:"))
sum = num // 100 + (num % 100) // 10 + num % 10
print("Sum of three-digit number is:", sum)