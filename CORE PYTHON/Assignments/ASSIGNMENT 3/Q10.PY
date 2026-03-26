#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
male_age = int(input("Enter male's age:"))
female_age = int(input("Enter female's age:"))
if male_age >=21 and female_age >=18:
    print("eligible to marry.")
else:
    print("Both are not eligible to marry.")