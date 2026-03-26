#WAP to check if given number Strong Number.
n = int(input("Enter a number: "))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum += fact
    temp //= 10
if sum == n:
    print(n, "is a Strong Number.")
else:
    print(n, "is not a Strong Number.") 