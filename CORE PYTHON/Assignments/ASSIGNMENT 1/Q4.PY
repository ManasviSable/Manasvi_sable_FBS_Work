#program to calculate simple interest
p = int(input("Enter the principal amount:"))
r = float(input("Enter the rate of interest:"))
t = int(input("Enter the time in years:"))
simple_interest = (p * r * t) / 100
print("Simple Interest is:", simple_interest)
