# Function to check if a number is perfect
def perfect():
    num = int(input("Enter a number: "))
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")

perfect()
