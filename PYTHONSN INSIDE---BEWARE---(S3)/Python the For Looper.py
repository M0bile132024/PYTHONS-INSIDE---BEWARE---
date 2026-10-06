# Python the For Looper
# Author:M0bile13026
# Date:08/07/2026



while True:
    total = 0
    count = 0
    even_count = 0
    odd_count = 0
    print("""\nTask 1: Count to 100
Task 2: Count to 50
Task 3: Count Backwards
Task 4: Even Numbers
Task 5: Odd Numbers
Task 6: Five Times Table
Task 7: User's Times Table
Task 8: Custom Range
Task 9:Count Between Two Numbers
Task 10: Squares
Task 11/12: Running Total & Average
Task 13: Count Positive Numbers""")
    loop = int(input("Which number?:"))
    print("\n")
    if loop == 1:
        # Task 1: Count to 100
        '''
        Task: Write a program that outputs the numbers 1 to 100, one number per line.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        for num in range(100):
            print(num + 1)
    elif loop == 2:
        # Task 2: Count to 50
        '''Task: Write a program that outputs the numbers 1 to 50.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        for num in range(50):
            print(num + 1)
    elif loop == 3:
        # Task 3:Count Backwards
        '''Task: Write a program that outputs the numbers 20 down to 1.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        for num in range(20):
            print(20-num)
    elif loop == 4:
        # Task 4: Even Numbers
        '''Task: Write a program that outputs all the even numbers from 2 to 100.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        for num in range(2,102,2):
            print(num)
    elif loop == 5:
        # Task 5: Odd Numbers
        '''Task: Write a program that outputs all the odd numbers from 1 to 99.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        for num in range(1,101,2):
            print(num)
    elif loop == 6:
        # Task 6: Five Times Table
        '''Task: Output the 5 times table from 1 to 12.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        for num in range(5,65,5):
            print(num)
    elif loop == 7:
        # Task 7: User's Times Table
        '''Task: Ask the user for a number and output its times table to 12.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        times_table = int(input("What times table do you want?:"))
        for num in range(times_table,times_table * 13,times_table):
            print(num)
    elif loop == 8:
        # Task 8: Custom Range
        '''Task: Ask the user for a number and output every number from 1 up to that number.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        end_num = int(input("Print numbers from 1 to...:"))
        for num in range(1,end_num+1):
            print(num)
    elif loop == 9:
        # Task 9:Count Between Two Numbers
        '''Task: Ask the user for a start and end number then output every number between them.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        start_num = int(input("Print numbers from...:"))
        end_num = int(input("...to...:"))
        for num in range(start_num,end_num+1):
            print(num)
    elif loop == 10:
        # Task 10: Squares
        '''Task: Output the square of every number from 1 to 20.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        for num in range(1,21):
            print(num ** 2)
    elif loop == 11 or loop == 12:
        # Task 11: Running Total
        '''Task: Ask how many numbers will be entered, input them using a for loop and output the total.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        # Task 12: Average
        '''Task: Modify Task 11 so the average is also displayed.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        how_many_num = int(input("How many nums do you want to enter?:"))
        for num in range(how_many_num):
            number = int(input("Enter a num:"))
            total += number
        print(f"The total of your nums is {total}")
        print(f"And the mean is {total/how_many_num}")
    elif loop == 13:
        # Task 13: Count Positive Numbers
        '''Task: Input 10 numbers and count how many are positive.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        for num in range(10):
            number = int(input("Enter a num:"))
            if number > 0:
                count += 1
        print(f"There are {count} positive nums among your nums...")
    elif loop == 14:
        # Task 14: Count Even and Odd
        '''Task: Input 10 numbers and count how many are even and odd.
        Success Criteria
        •	✓ Uses a for loop correctly
        •	✓ Produces the required output
        •	✓ Uses meaningful variable names
        •	✓ Program has been tested'''

        for num in range(10):
            number = int(input("Enter a num:"))
            if number // 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        print(f"There are {even_count} even nums among your nums...")

    else:
        print("Invalid number idiot")



