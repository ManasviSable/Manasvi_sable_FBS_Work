#Write a program to calculate the sum of following series where n is input by user. 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!
n = int(input("Enter the value of n: "))
factorial = 1
series_sum = 0
for i in range(1,n+1):
    factorial *= i
    series_sum += i/factorial
print("The sum of the given series is:",series_sum)