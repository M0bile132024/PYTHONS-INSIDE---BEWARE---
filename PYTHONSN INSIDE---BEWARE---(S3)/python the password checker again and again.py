# Python the password checker again and again V.1.3
password = 0
attempts = 0
max_attempts = 5
total = 0
number = 0
num_of_num = 0

passA = input("Please enter a password:")
passB = input("Please enter it again to verifiy it:")
passC = input("Just one more time for absoulute verification::")
if passA == passB and passB == passC:
    print("Passwords match!")
    print("Access granted!")
    print("\n\n\n\n\n\n\nWelcome to [],please enter your password now:")
    while password != passA or attempts >= max_attempts:
        password = input(">")
        if password != passA and attempts < max_attempts:
            attempts += 1
            if attempts >= max_attempts:
                print("Incorrect password.")
            else:
                print("Incorrect password,please try again")
    if attempts >= max_attempts:
        print("""Unfortunately,due to too many incorrect attempts the [] has been locked down for security reasons.

    Please try again n e v e r....""")
    else:
        print("Access granted!You may proceed...")
        print("\n\n\n\n\n\n\n")
        while True:
            number = input("Here at [] we like nums for some reason,so give me a num(excluding 0)(type 'exit' to end program):")
            if number == "exit":
                break
            elif int(number) == 0:
                print("...")
            else:
                print("Processing...")
                total += int(number)
                num_of_num += 1
                print("Num successfully recorded, please proceed with next num")
        print(f"Your total num is {total}!")
        print(f"And your num of nums is {num_of_nums}")
else:
    if passA != passB and passB != passC:
        print("All passwords do not match!")
        print("Access denied!")

    elif (passA == passB and passB != passC) or (passA != passB and passB == passC) or (passA == passC and passB != passA):
        print("One password does not match!")
        print("Access denied!")

    else:
        print("Two passwords do not match!")
        print("Access denied!")





