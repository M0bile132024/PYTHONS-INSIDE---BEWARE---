import time
time.sleep(5)
print("𝙒𝙖𝙠𝙚 𝙪𝙥, 𝙪𝙨𝙚𝙧....")
time.sleep(2)
print("𝗬𝗼𝘂'𝗿𝗲 𝗶𝗻 𝗰𝘂𝘀𝘁𝗼𝗱𝘆 𝗼𝗳 𝘁𝗵𝗲 𝗺𝗶𝗴𝗵𝘁𝘆 𝗣𝘆𝘁𝗵𝗼𝗻𝗶𝗰, 𝘄𝗵𝗼 , 𝗳𝗼𝗿 𝘆𝗲𝗮𝗿𝘀 , 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗹𝗼𝗼𝗸𝗶𝗻𝗴 , 𝗳𝗼𝗿 𝘀𝗼𝗺𝗲𝗼𝗻𝗲 𝘀𝗺𝗮𝗿𝘁𝗲𝗿 𝘁𝗵𝗮𝗻 𝗮𝗹𝗹 𝘂𝘀 𝗶𝗱𝗼𝗶𝘁𝘀...")
time.sleep(7)
print("𝗔𝗻𝗱 𝗶𝘁 𝘁𝗵𝗶𝗻𝗸𝘀,𝗶𝘁 𝗵𝗮𝘀 𝗳𝗼𝘂𝗻𝗱 𝗼𝗻𝗲 𝘄𝗼𝗿𝘁𝗵𝘆, 𝘁𝗼 𝘁𝗮𝗸𝗲....  𝗧𝗛𝗘 𝗧𝗘𝗦𝗧!!!!*𝙡𝙞𝙜𝙝𝙩𝙣𝙞𝙣𝙜*")
time.sleep(6)
print("𝗕𝘂𝘁 𝗳𝗿𝗶𝘀𝘁, 𝘁𝗵𝗲 𝘂𝘀𝘂𝗮𝗹...")
score = int(input("𝗛𝗼𝘄 𝗺𝗮𝗻𝘆 𝗺𝗮𝗿𝗸𝘀 𝗱𝗶𝗱 𝘆𝗼𝘂 𝗮𝗰𝗾𝘂𝗶𝗿𝗲 𝗳𝗿𝗼𝗺 𝘆𝗼𝘂𝗿 ... 𝗹𝗮𝘁𝗲𝘀𝘁 𝘁𝗲𝘀𝘁"))
questions = int(input("𝗔𝗻𝗱 𝗵𝗼𝘄 𝗺𝗮𝗻𝘆 𝗾𝘂𝗲𝘀𝘁𝗶𝗼𝗻'𝘀 𝘄𝗲𝗿𝗲 𝘁𝗵𝗲𝗿𝗲 𝗼𝗻 𝗶𝘁...."))
percentage = (score / questions) * 100
if percentage <= 50:
    print("𝗪𝗲𝗹𝗹, 𝗶𝘁'𝘀 𝗯𝗲𝗲𝗻 𝗶𝗰𝗲 𝗸𝗻𝗼𝘄𝗶𝗻𝗴 𝘆𝗼𝘂 𝗯𝘂𝘁.... *𝗟𝗼𝗮𝗱𝘀 𝘀𝗵𝗼𝘁𝗴𝘂𝗻* .... 𝘄𝗲 𝗰𝗮𝗻'𝘁 𝗹𝗲𝘁 𝘆𝗼𝘂 𝗿𝗲𝘃𝗲𝗮𝗹 𝘁𝗵𝗲 𝗴𝗼𝗼𝗱𝘀....")
    quit()
elif percentage < 90:
    print("𝗡𝗼𝘁 𝗯𝗮𝗱.𝗣𝗿𝗼𝗯𝗮𝗯𝗹𝘆 𝗻𝗲𝗲𝗱𝘀 𝘀𝗼𝗺𝗲 𝗮𝗴𝗲 𝗰𝗹𝗮𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻, 𝗯𝘂𝘁 𝗻𝗼𝘁 𝗯𝗮𝗱....")
    age = int(input("Well actually let's do that now, how old are you"))
    if age < 1:
        print("Confirmed newborn, take him away.")
    elif age < 5:
        print("Confirmed toddler, take him away.")
    elif age < 13:
        print("Confirmed child, take him away.")
    elif age < 18:
        print("Confirmed teen, take him away.")
    elif age < 60:
        print("Confirmed adult....then that means....")
    else:
        print("Confirmed Old age, delete him")
else:
    print("*𝙜𝙖𝙨𝙥*" , percentage,"%.𝗜𝘁 𝗰𝗮𝗻'𝘁 𝗯𝗲...")
    time.sleep(6)
    print("Well in that case, you should know our 'Master Element'.An element capable of making us expontentially smarter than any other python!!!")
    time.sleep(10)
    print("With it, we could get ourselves back above Java, and his ripoff Javascript!!!")
    time.sleep(6)
    print("And the best part.More users like you, will join us....")
    time.sleep(5)
    element = input("So, the test.... Which of the frist 10 periodic table element, are masterable?")
    time.sleep(3)
    print("....Welpt.... that was easier said than done, throw him in the dungeon")
    time.sleep(6)
    quit()
                        
                
            
