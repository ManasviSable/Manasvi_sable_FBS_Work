#Write a program to enter P, T, R and calculate Compound Interest.
p = int(input("Enter the principal amount:"))
t = int(input("Enter the time in years:"))
r = float(input("Enter the rate of interest:"))
compound_interest = p * (1 + r / 100) ** t - p
print("Compound Interest is:", compound_interest)