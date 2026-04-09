#Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.
n = int(input("Enter number of students:"))
total_percentage = 0
for i in range(1,n+1):
    print(f"Marks of student{i}:")
    sub1 = int(input("Enter marks of subject 1:"))
    sub2 = int(input("Enter marks of subject 2:"))
    sub3 = int(input("Enter marks of subject 3:"))
    sub4 = int(input("Enter marks of subject 4:"))
    sub5 = int(input("Enter marks of subject 5:")) 
    total = 500
    percentage = ((sub1 +sub2 + sub3 + sub4 + sub5) / total)*100
    print(f"Percentage of student{i} is:",percentage)
    total_percentage += percentage
else :
    avg_percentage = total_percentage/n
    print(f'Average percentage',avg_percentage)