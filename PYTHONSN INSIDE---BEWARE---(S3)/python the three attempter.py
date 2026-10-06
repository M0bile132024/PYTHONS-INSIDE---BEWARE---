#Python the three attempter
correct_username = "admin"
correct_password = "python123"
attempts = 3

success = False

while not success and attempts > 0:
    print(f"Attempts left = {attempts}")
    username = input("Please enter username:")
    password = input("And password:")
    if username == correct_username and password == correct_password:
        success = True
    else:
        print("Username or/and password is incorrect, please try again")
        attempts -= 1
if success:
    print("Access granted, welcome to the M A T R I X.co")
else:
    print("Account locked,please contact your administrator")


