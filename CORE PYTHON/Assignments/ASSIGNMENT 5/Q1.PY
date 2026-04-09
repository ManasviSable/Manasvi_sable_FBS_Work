for i in range(1, 4):
    user_id = input(f"Attempt {i} - Enter user id: ")
    password = int(input(f"Attempt {i} - Enter password: "))

    if user_id == 'admin' and password == 123456789:
        print("Login successful")
        break
    else:
        print("Incorrect user ID or password")

else:
    print("Too many attempts. Program terminated.")