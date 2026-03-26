#Write a program to accept 3 digit number. If first digit is double of second digit and half of third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
n = int(input("Enter a three digit number as abc:"))
a = n // 100
b = (n // 10) % 10
c = n % 10
if a == 2 * b and a == c / 2:
    print("Yes, you have done it.")
else:  
    print("Please try next time.")
