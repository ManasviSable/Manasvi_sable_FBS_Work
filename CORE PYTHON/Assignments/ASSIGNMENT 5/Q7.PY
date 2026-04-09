#Write a program to solve the following series : a. 1! + 2! + 3! + 4! + .....n! b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent) c. Find the sum of a geometric series from 1 to n where the common ratio is 2. d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10 e. x - x2/3 + x3/5 - x4/7 + .... to n terms
#a
n = int(input("Enter the value of n: "))
factorial_sum = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    factorial_sum += factorial
print("The sum of the series 1! + 2! + ... + n! is:", factorial_sum)
#b
n = int(input("Enter the value of N: "))
power_sum = 0
for i in range(1, n + 1):
    power_sum += n ** i
print("The sum of the series N + N^2 + ... + N^N is:", power_sum)   
#c
n = int(input("Enter the value of n: "))
geometric_sum = 0
for i in range(1, n + 1):
    geometric_sum += 2 ** i
print("The sum of the geometric series is:", geometric_sum)
#d
a = float(input("Enter the value of a: "))
s = 0
for i in range(1, 11):
    s += a ** i / i 
print("The sum of the series S = a + a^2/2 + ... + a^10/10 is:", s)
#e
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
s = 0   
for i in range(1, n + 1):
    s += (-1) ** (i + 1) * (x ** i) / (2 * i - 1)
print("The sum of the series is:", s)       