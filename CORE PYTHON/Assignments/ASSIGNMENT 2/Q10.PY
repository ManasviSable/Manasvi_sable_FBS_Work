#Write a program to reverse three-digit number.
num = int(input("Enter a three-digit number in the form of abc:"))
reverse = (num % 10) * 100 + ((num // 10) % 10) * 10 + num // 100
print("Reverse of three-digit number is:", reverse)
