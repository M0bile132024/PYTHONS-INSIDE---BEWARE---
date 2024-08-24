# Code  my rights here
import time
poundtransferal = int(input("Please enter amount of £ to transfer £"))
if poundtransferal >= 50 and poundtransferal <= 60:
    print("Your amount of £s are within range!Transferring....")
    time.sleep(3)
    print("Transferred successfully!Now before you can go, we need to check if your overdrawn.")
    balance = int(input("Please enter your current balance £"))
    if balance < 0:
        print("WARNING YOU ARE OVERDRAWN!")
        house = str(input("PLEASE ENTER HOUSE(AQ=Aquinas , AU=Augustine , IG=Ignatius , N = Newman):"))
        if house == "AQ":
            print("Please visit the House of Lecture theartring on Monday, for a 'said' assembly...")
            time.sleep(3)
        elif house == "AU":
            print("Please visit the House of Lecture theartring on Tuesday, for a 'said' assembly...")
            time.sleep(3)
        elif house == "IG":
            print("Please visit the House of Lecture theartring on Wednesday, for a 'said' assembly...")
            time.sleep(3)
        elif house == "N":
            print("Please visit the House of Lecture theartring on Friday, for a 'said' assembly...")
            time.sleep(3)
        else:
            print("INVALID HOUSE!! Guess i'm visiting your MOTHER!!")
            time.sleep(5)
            print("Huh, she ain't picking the phone... Oh well then , let's hear about the latest football!")
            MC = int(input("How many did Man city score last game:"))
            MU = int(input("And how about United:"))
            if MC > MU:
                print("Go Man City!!! :D")
                time.sleep(3)
                if MU == 0:
                    print("But sorry Man united :(")
                    time.sleep(3)
            elif MC < MU:
                print("Go Man United!!! :)")
                if MC == 0:
                    print("But sorry Man City :C")
                    time.sleep(3)
            elif MC == MU:
                print("Ah , a draw I see")
                time.sleep(3)
                if MC == 0:
                    print("And both zero!Come on!!! *thumbs down*")
                    time.sleep(3)
            print("Ah , she's here.Well prepare for hell, son....")
            time.sleep(1)
            print("Thanks for banking at Python Banks, we'll see you next time....")
            time.sleep(6)
    else:
        print("Thanks for banking at Python Banks, we'll see you next time....")
        time.sleep(3)
else:
    print("Uh oh! The £s you'd inputted are not within range. Please proceed to restart the program.")
    time.sleep(3)