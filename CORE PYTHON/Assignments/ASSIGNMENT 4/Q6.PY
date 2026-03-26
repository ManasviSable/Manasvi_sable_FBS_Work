#WAP to check if a given number is prime number or not.
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if n % i == 0:
        print(n, "is not a prime number.")
        break
else:
    print(n, "is a prime number.")