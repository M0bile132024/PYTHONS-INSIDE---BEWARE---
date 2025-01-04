#The icecreamed one
print("Note=from prespective of PY8th\n\n\n\n\n\n\n\n\n\n\n")
import time
import random
import turtle
def waiting_dots(amount_of_dots = 3,waiting_time = 1):
    for i in range(amount_of_dots):
        print(".")
        time.sleep(waiting_time)
def Processing(Processing="Processing",amount_of_dots = 3,waiting_time = 1):
    print(Processing,end="")
    for i in range(amount_of_dots):
        print(".",end="")
        time.sleep(waiting_time)
def The_Junkie_Gas_Station():
    max_gas = int(input("𝑾𝒆𝒍𝒐𝒄𝒎𝒆 𝒕𝒐 𝒎𝒆 𝒈𝒂𝒔 𝒔𝒕𝒂𝒕𝒊𝒐𝒏,𝒉𝒐𝒘 𝒎𝒖𝒄𝒉 𝒈𝒂𝒔 𝒚𝒐𝒖'𝒅 𝒏𝒆𝒆𝒅...(Gallons):"))
    gas_put_in = 0
    gas_dose = 0
    dose = 1
    while gas_put_in != max_gas:
        if gas_put_in < max_gas:
            gas_dose = int(input(f"Alright, how much do you want to pump for your {dose}st/nd/rd/th dose(1-50 gallons):"))
            while gas_dose > 50 or gas_dose < 1:
                gas_dose = int(input(f"Alright,now that's an invalid dose, let's try that agian(1-50 gallons):"))
            Processing("Pumping the gas",3,round((gas_dose/10)/3,1))
            gas_put_in += gas_dose
            print(f"\n{dose}st/nd/rd/th dose sucessfully pumped....\nYou now have {gas_put_in} gallons of gas in your tank")
            dose += 1
        if gas_put_in > max_gas:
            gas_dose = int(input(f"Alright, how much do you want to unpump for your {dose}st/nd/rd/th dose(1-50 gallons):"))
            while gas_dose > 50 or gas_dose < 1:
                gas_dose = int(input(f"Alright,now that's an invalid dose, let's try that agian(1-50 gallons):"))
            Processing("Unpumping the gas",3,round((gas_dose/10)/3,1))
            gas_put_in -= gas_dose
            print(f"\n{dose}st/nd/rd/th dose sucessfully pumped....\nYou now have {gas_put_in} gallons of gas in your tank")
            dose += 1
    print("Thanks for refuelling at Junkie's...or whatever...")
    return dose
def Double_Authentication():
    pin_attempt = 0
    pin_attempt2 = 0
    pin = random.randint(1,10000)
    while pin_attempt != pin or pin-attempt2 != pin:
        random_myserty = random.randint(1,2)
        print("""𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗣𝘆𝘁𝗵𝗼𝗻𝗶𝗰 𝗔𝘂𝘁𝗵𝗼𝗿𝗶𝘁𝗲𝘀 𝗗𝗼𝘂𝗯𝗹𝗲 𝗔𝘂𝘁𝗵𝗲𝗻𝘁𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝘀𝘆𝘀𝘁𝗲𝗺,
𝘁𝗵𝗲 𝗻𝗲𝘄𝘀𝗲𝘁, 𝗮𝗻𝗱 𝗯𝗲𝘀𝘁 𝗼𝗳 𝗵𝗶𝘀 𝗶𝗻𝘃𝗲𝗻𝘁𝗶𝗼𝗻𝘀!""")
        pin_attempt = int(input("𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝗮 𝗽𝗶𝗻:"))
        pin_attempt2 = int(input("𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝗽𝗶𝗻 𝗮𝗴𝗮𝗶𝗻 𝘁𝗼 𝘃𝗲𝗿𝗶𝗳𝘆:"))
        Processing("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴")
        if pin_attempt > pin or pin_attempt < pin or pin_attempt2 > pin or pin_attempt2 < pin:
            print("𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗜𝗡!𝗣𝗟𝗘𝗔𝗦𝗘 𝗥𝗘𝗔𝗧𝗧𝗘𝗠𝗣𝗧 𝘃")
            if random_myserty == 1:
                lower_higher = "low-" if pin_attempt > pin else  "high-" if pin_attempt < pin else "Second one hig-" if pin_attempt2 > pin else "Second one lo-" if pin_attempt2 < pin else "ERROR 101:Unintentional Design"
                time.sleep(3)
                print("Pssth")
                time.sleep(3)
                print(f"It's {lower_higher}")
                print("𝗥𝗼𝗴𝘂𝗲 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝘁𝗲𝗿𝗺𝗶𝗻𝗮𝘁𝗲𝗱.")
                time.sleep(1)
    print(f"𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗜𝗡, 𝘆𝗼𝘂 𝗺𝗮𝘆 𝗲𝗻𝘁𝗲𝗿 𝗮𝘀 𝗣𝘆𝘁𝗵𝗼𝗻𝗶𝗰 𝗔𝘀𝘀𝗼𝗰𝗶𝗮𝘁𝗲{random.randint(1,10000)}!!")

    
    
print("Last time...")
time.sleep(3)
print("A dungeon break occured, of tasty sucess...")
time.sleep(1)
'''Task 1.
Write a program that asks the user to enter their age. The program should ensure that the input is a positive integer. 

If the user enters an invalid age (e.g., a negative number or zero), the program should prompt the user to enter a valid age.
'''
age = float(input("Wait a second!How old are you!?!:"))
snakecategory = 0
while snakecategory == 0:
    if age >= 30:
        snakecategory = "old"
    elif age >= 20:
        snakecategory = "middle-aged"
    elif age >= 1.5:
        snakecategory = "adult"
    elif age > 0:
        snakecategory = "child"
    else:
        age = float(input("That isn't an age, try again:"))
print(f"Huh,you look a little....Unpython-like to be a {snakecategory} python...")
'''Task 2:
2.	Ask the user to enter in the school they go to and only allow entry if they enter one of the following “St Ambrose
College”, “Saint Ambrose College”, “st ambrose” or “St Ambrose”'''
time.sleep(3)
print("""𝙊𝙝, 𝙙𝙤𝙣'𝙩 𝙢𝙞𝙣𝙙 𝙩𝙝𝙞𝙨 𝙞𝙙𝙞𝙤𝙩, 𝙝𝙚 𝙢𝙞𝙨𝙨𝙚𝙙-𝙡𝙞𝙠𝙚 𝙝𝙖𝙡𝙛 𝙤𝙛 𝙝𝙞𝙨 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣,
𝙖𝙣𝙙 𝙣𝙤𝙬 𝙞𝙨 𝙟𝙪𝙨𝙩 𝙗𝙤𝙪𝙣𝙙 𝙩𝙤 𝙨𝙚𝙡𝙡𝙞𝙣𝙜 𝙞𝙘𝙚𝙘𝙧𝙚𝙖𝙢 𝙛𝙤𝙧 𝙖 𝙡𝙞𝙫𝙞𝙣𝙜... """)
time.sleep(3)
print("""Oh, says the one, who spent his life working for a
corrupt dungeon.Besides we're entering a High-education Sector.
Hope you're school identification covers th-""")
time.sleep(4)
attempts = 3
entry = False
while entry == False or attempts != 0:
    school_identification = str(input("*Drone flies into icecream truck through open window*ＰＬＥＡＳＥ　ＥＮＴＥＲ　ＣＵＲＲＥＮＴ　ＳＣＨＯＯＬ　ＩＤＥＮＴＩＦＩＣＡＴＩＯＮ："))
    Processing("ＰＲＯＣＥＳＳＩＮＧ")
    if school_identification == "St Ambrose College" or school_identification == "Saint Ambrose College" or school_identification == "st ambrose" or school_identification == "St Ambrose":
        print("ＡＣＥＳＳ　ＧＲＡＮＴＥＤ：ＹＯＵ　ＭＡＹ　ＥＮＴＥＲ*self denoates*")
        entry = True
    else:
        attempts -= 1
        print(f"ＡＣＥＳＳ　ＤＥＮＩＥＤ：ＹＯＵ　ＨＡＶＥ {attempts}　ＭＯＲＥ　ＡＴＴＥＭＰＴＳ")
        time.sleep(3)
if attempts == 0:
    print("ＦＡＩＬＵＲＥ　ＴＯ　ＣＯＭＰＬＹ：ＹＯＵ　ＳＨＡＬＬ　ＮＯＷ　ＢＥ　ＳＨＯＴ")
    
    quit()
'''3.	Create a program using a while loop that keeps asking a user to enter a number and adds those numbers together to a total. 

When the total goes over 100, the program stops and outputs: “OVERLOAD! You have gone over 100!”
'''
time.sleep(2)
waiting_dots(3,2)
print("oh you got to be kidding me...")
waiting_dots()
print("Well fellas, it seems we're out of gas.")
time.sleep(2)
print("𝙊𝙝 𝙤𝙛 𝙘𝙤𝙪𝙧𝙨𝙚,𝙞𝙩 𝙙𝙞𝙙...")
time.sleep(2)
print("𝙏𝙝𝙖𝙣𝙠𝙛𝙪𝙡𝙡𝙮, 𝙬𝙚 𝙨𝙤 𝙝𝙖𝙥𝙥𝙚𝙣 𝙩𝙤 𝙗𝙚 𝙤𝙪𝙩𝙨𝙞𝙙𝙚 𝙖 '𝙟𝙪𝙣𝙠𝙞𝙚' 𝙜𝙖𝙨 𝙨𝙩𝙖𝙩𝙞𝙤𝙣")
time.sleep(2)
print("Huh ,stupid name for a gas station,i'd usually go to the better ones....")
time.sleep(3)
print("𝙎𝙝𝙤𝙪𝙡𝙙𝙖 𝙤𝙛 𝙩𝙝𝙤𝙪𝙜𝙝𝙩 𝙤𝙛 𝙩𝙝𝙖𝙩 𝙗𝙚𝙛𝙤𝙧𝙚, 𝙉𝙤𝙬 𝙜𝙤 𝙛𝙚𝙩𝙘𝙝 𝙪𝙨 𝙨𝙤𝙢𝙚 𝙜𝙖𝙨, 𝙪𝙨𝙚𝙧.")
attempts = The_Junkie_Gas_Station()-1
waiting_dots(3)
if attempts > 5:
    print("Hmm, took your time I see...")
    time.sleep(2)
print("Well we best be off to the 'Cabin', for I hear you and Python The 4 did your little meetup there...")
time.sleep(3)
print("\n\n\n\n---------Some Hardcore Driving Later--------\n\n\n\n")
time.sleep(5)
print("(𝙔𝙤𝙪'𝙙 𝙜𝙤𝙩 𝙩𝙤 𝙗𝙚 𝙠𝙞𝙙𝙙𝙞𝙣𝙜 𝙢𝙚),𝙒𝙝𝙮 𝙞𝙨 𝙩𝙝𝙚 𝙘𝙖𝙗𝙞𝙣 𝙖𝙪𝙩𝙝𝙚𝙣𝙩𝙞𝙘𝙖𝙩𝙚𝙙!!")
time.sleep(3)
print("Because of the investigators known as the authorites,idiot.")
time.sleep(3)
print("Now user, use your big brain,and demolish this lock!")
Double_Authentication()
waiting_dots(5)
print("𝙒𝙚𝙡𝙡 𝙣𝙤𝙬 𝙞'𝙙 𝙨𝙚𝙚𝙣 𝙚𝙫𝙚𝙧𝙮𝙩𝙝𝙞𝙣𝙜...")
print("Yeah, he just cracked a governmental code without....\nany\nhints?")
time.sleep(3)
print("Is that a Taco Place in the cabi-")
time.sleep(2)
print("To",end=" ")
time.sleep(1)
print("Be",end=" ")
time.sleep(1)
print("Continued...",end=" ")
time.sleep(1)





