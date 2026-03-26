#Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("Enter a three-digit number: "))
reverse = (num % 10) * 100 + ((num // 10) % 10) * 10 + num // 100
if num == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")