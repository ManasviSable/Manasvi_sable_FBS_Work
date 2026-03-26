#Write a program to check if user has entered correct userid and password.
userid = input("Enter your userid: ")
password = input("Enter your password: ")
if userid == "admin" and len(password) == 11:
    print("Login successful.")
else:
    print("Invalid userid or password.")