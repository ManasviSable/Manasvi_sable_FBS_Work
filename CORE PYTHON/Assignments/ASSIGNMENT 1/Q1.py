#Write a program to calculate the percentage of student based on marks of any 5 subjects.
sub1 = int(input("Enter marks of 1st subject of choice:"))
sub2 = int(input("Enter marks of 2nd subject of choice:"))
sub3 = int(input("Enter marks of 3rd subject of choice:"))
sub4 = int(input("Enter marks of 4th subject of choice:"))
sub5 = int(input("Enter marks of 5th subject of choice:"))
total = 500
percentage = (sub1 + sub2 + sub3 + sub4 + sub5) / total * 100
print("Percentage of student is:", percentage)