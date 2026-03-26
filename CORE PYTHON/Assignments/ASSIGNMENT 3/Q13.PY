#Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For the first 50 units: Rs. 0.50/unit
# For the next 100 units: Rs. 0.75/unit
# For the next 100 units: Rs. 1.20/unit
# For units above 250: Rs. 1.50/unit
unit = int(input("Enter the number of units consumed: "))
if unit <= 50:
    bill = unit * 0.50
elif unit <= 150:
    bill = 50 * 0.50 + (unit - 50) * 0.75
elif unit <= 250:
    bill = 50 * 0.50 + 100 * 0.75 + (unit - 150) * 1.20
else:
    bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (unit - 250) * 1.50

print("Total electricity bill: Rs.", bill)