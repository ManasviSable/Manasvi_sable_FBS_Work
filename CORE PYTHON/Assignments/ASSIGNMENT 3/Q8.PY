#Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)
userid = input("Enter your userid:")
password = input("Enter your password:")
if userid == "admin" and len(password) == 11:
    import random
    captcha = random.randint(1000, 9999)
    print("Your captcha is:", captcha)
    user_input = int(input("Enter the captcha:"))
    if user_input == captcha:
        print("Login successful.")
    else:
        print("Captcha verification failed.")