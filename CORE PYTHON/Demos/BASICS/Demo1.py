#program to calculate area of rectangle
L = int(input("Enter the length of rectangle:"))
B = int(input("Enter the breadth of rectangle:"))
area = L * B
print(f"Area of reactangle with length {L} and breadth {B} is {area}")

#percentage calculation 
M1 = int(input("Enter marks of subject 1 "))
M2 = int(input("Enter marks of subject 2 "))
M3 = int(input("Enter marks of subject 3 "))
M4 = int(input("Enter marks of subject 4 "))
marks_gain = M1 + M2 + M3 + M4
total_marks = 400
percentage = (marks_gain / total_marks) * 100
print(f"Percentage of marks is {percentage}%")