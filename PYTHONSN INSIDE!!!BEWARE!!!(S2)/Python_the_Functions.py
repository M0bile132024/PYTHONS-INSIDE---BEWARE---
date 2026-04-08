import time
import random
def waiting_dots(amount_of_dots = 3,waiting_time = 1):
    for i in range(amount_of_dots):
        print(".")
        time.sleep(waiting_time)
def Processing(Processing="Processing",amount_of_dots = 3,waiting_time = 1):
    print(Processing,end="")
    for i in range(amount_of_dots):
        print(".",end="")
        time.sleep(waiting_time)
def The_Dungeon_Libary():
    quitting = 0
    while quitting == 0:
        book_list = []
        days_list = []
        cost_list = []
        choice = 0
        book_index = 0
        print("𝗛𝗲𝗹𝗹𝗼, 𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗗𝘂𝗻𝗴𝗲𝗼𝗻 𝗹𝗶𝗯𝗿𝗮𝗿𝘆:","𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗯𝗼𝗼𝗸𝘀","𝗣𝗿𝗲𝘀𝘀 𝟮 𝘁𝗼 𝗯𝗼𝗿𝗿𝗼𝘄/𝗯𝘂𝘆 𝗯𝗼𝗼𝗸𝘀","𝗣𝗿𝗲𝘀𝘀 𝟯 𝘁𝗼 𝗿𝗲𝗻𝗲𝘄 𝗯𝗼𝗼𝗸𝘀","𝗢𝗿 𝟰 𝘁𝗼 𝗾𝘂𝗶𝘁 𝘁𝗵𝗶𝘀 𝗶𝗻𝗾𝘂𝗶𝗿𝘆",sep="\n")
        choice = int(input(">>>"))
        print("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴!")
        time.sleep(5)
        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            checkout = 0
            while checkout == 0:
                #Return books
                if choice == 1:
                    book_list.append(str(input("𝗘𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗻𝗮𝗺𝗲 𝗼𝗳 𝗮 𝗯𝗼𝗼𝗸 𝘆𝗼𝘂'𝘃𝗲 𝗯𝗼𝗿𝗿𝗼𝘄𝗲𝗱:")))
                    days_list.append(int(input("𝗔𝗻𝗱 𝗵𝗼𝘄 𝗺𝗮𝗻𝘆 𝗱𝗮𝘆𝘀 𝗵𝗮𝘃𝗲 𝘆𝗼𝘂 𝗵𝗮𝗱 𝘁𝗵𝗶𝘀 𝗯𝗼𝗼𝗸?:")))
                    print("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴!")
                    time.sleep(5)
                    if days_list[book_index] == 0:
                        cost_list.append(float(0))
                    elif days_list[book_index] >= 1 and days_list[book_index] <= 5:
                        cost_list.append(float(days_list[book_index] * 0.5))
                    elif days_list[book_index] >= 6 and days_list[book_index] <= 10:
                        cost_list.append(float(days_list[book_index] * 1))
                    elif days_list[book_index] > 10:
                        cost_list.append(float(days_list[book_index] * 5))
                    else:
                        print("𝖀𝖓𝖘𝖚𝖈𝖈𝖊𝖘𝖘𝖋𝖚𝖑𝖑𝖞 𝖑𝖔𝖌𝖌𝖊𝖉 𝖈𝖔𝖘𝖙𝖘!:")
                        book_list.pop(book_index)
                        days_list.pop(book_index)
                        if len(book_list) == 0:
                            checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                            continue
                        else:
                            minindex = 0
                            for x in book_list:
                                print("Book index:",x,"Book name:",book_list[minindex],"Days taken:",days_list[minindex],"Cost(£/$)",round(cost_list[minindex], 2),sep = "|")
                                minindex += 1
                            checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                            continue
                    print("𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗹𝗼𝗴𝗴𝗲𝗱 𝗰𝗼𝘀𝘁𝘀!:")
                    if len(book_list) == 0:
                        checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                        book_index += 1
                        continue
                    else:
                        minindex = 0
                        for x in book_list:
                            print("Book index:",minindex,"Book name:",book_list[minindex],"Days taken:",days_list[minindex],"Cost(£/$)",round(cost_list[minindex], 2),sep = "|")
                            minindex += 1
                        checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                        book_index += 1
                        continue
                #Borrow/buy
                if choice == 2:
                    book_list.append(str(input("𝗘𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗻𝗮𝗺𝗲 𝗼𝗳 𝗮 𝗯𝗼𝗼𝗸 𝘆𝗼𝘂 wish to 𝗯𝗼𝗿𝗿𝗼𝘄:")))
                    days_list.append(int(input("𝗔𝗻𝗱 𝗵𝗼𝘄 𝗺𝗮𝗻𝘆 𝗱𝗮𝘆𝘀 do you wish to have this 𝗯𝗼𝗼𝗸?:")))
                    print("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴!")
                    time.sleep(5)
                    if days_list[book_index] == 0:
                        cost_list.append(float(0))
                    elif days_list[book_index] >= 1 and days_list[book_index] <= 5:
                        cost_list.append(float(days_list[book_index] * 0.5))
                    elif days_list[book_index] >= 6 and days_list[book_index] <= 10:
                        cost_list.append(float(days_list[book_index] * 1))
                    elif days_list[book_index] > 10:
                        cost_list.append(float(days_list[book_index] * 5))
                    else:
                        print("𝖀𝖓𝖘𝖚𝖈𝖈𝖊𝖘𝖘𝖋𝖚𝖑𝖑𝖞 𝖑𝖔𝖌𝖌𝖊𝖉 𝖈𝖔𝖘𝖙𝖘!:")
                        book_list.pop(book_index)
                        days_list.pop(book_index)
                        if len(book_list) == 0:
                            checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                            continue
                        else:
                            minindex = 0
                            for x in book_list:
                                print("Book index:",x,"Book name:",book_list[minindex],"Days wishing to take for:",days_list[minindex],"Cost(£/$)",round(cost_list[minindex], 2),sep = "|")
                                minindex += 1
                            checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                            continue
                    print("𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗹𝗼𝗴𝗴𝗲𝗱 𝗰𝗼𝘀𝘁𝘀!:")
                    if len(book_list) == 0:
                        checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                        book_index += 1
                        continue
                    else:
                        minindex = 0
                        for x in book_list:
                            print("Book index:",minindex,"Book name:",book_list[minindex],"Days wishing to take for:",days_list[minindex],"Cost(£/$)",round(cost_list[minindex], 2),sep = "|")
                            minindex += 1
                        checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                        book_index += 1
                        continue
                #Renew
                if choice == 3:
                    book_list.append(str(input("𝗘𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗻𝗮𝗺𝗲 𝗼𝗳 𝗮 𝗯𝗼𝗼𝗸 𝘆𝗼𝘂 want to renew:")))
                    days_list.append(int(input("𝗔𝗻𝗱 𝗵𝗼𝘄 𝗺𝗮𝗻𝘆 𝗱𝗮𝘆𝘀 do you want to renew it for?:")))
                    print("𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴!")
                    time.sleep(5)
                    if days_list[book_index] == 0:
                        cost_list.append(float(0))
                    elif days_list[book_index] >= 1 and days_list[book_index] <= 5:
                        cost_list.append(float(days_list[book_index] * 0.5))
                    elif days_list[book_index] >= 6 and days_list[book_index] <= 10:
                        cost_list.append(float(days_list[book_index] * 1))
                    elif days_list[book_index] > 10:
                        cost_list.append(float(days_list[book_index] * 5))
                    else:
                        print("𝖀𝖓𝖘𝖚𝖈𝖈𝖊𝖘𝖘𝖋𝖚𝖑𝖑𝖞 𝖑𝖔𝖌𝖌𝖊𝖉 𝖈𝖔𝖘𝖙𝖘!:")
                        book_list.pop(book_index)
                        days_list.pop(book_index)
                        if len(book_list) == 0:
                            checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                            continue
                        else:
                            minindex = 0
                            for x in book_list:
                                print("Book index:",x,"Book name:",book_list[minindex],"Additional days:",days_list[minindex],"Cost(£/$)",round(cost_list[minindex], 2),sep = "|")
                                minindex += 1
                            checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                            continue
                    print("𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗹𝗼𝗴𝗴𝗲𝗱 𝗰𝗼𝘀𝘁𝘀!:")
                    if len(book_list) == 0:
                        checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                        book_index += 1
                        continue
                    else:
                        minindex = 0
                        for x in book_list:
                            print("Book index:",minindex,"Book name:",book_list[minindex],"Additional days:",days_list[minindex],"Cost(£/$)",round(cost_list[minindex], 2),sep = "|")
                            minindex += 1
                        checkout = int(input("𝗣𝗿𝗲𝘀𝘀 𝟭 𝘁𝗼 𝗴𝗼 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝗼𝗿 𝟬 𝘁𝗼 𝗿𝗲𝘁𝘂𝗿𝗻 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝗼𝗸"))
                        book_index += 1
                        continue
                if choice == 4:
                    print("Ok,buh-bye!!!")
                    quitting = 1
                    choice = 0
                    checkout = 1

        else:
            print("𝕿𝖍𝖆𝖙 𝖎𝖘 𝖓𝖔𝖙 𝖆 𝖔𝖕𝖙𝖎𝖔𝖓....")
            time.sleep(5)
def Dungeon_BMI_Checker():
    BMI = 0
    Categorisation = 0
    Advice = 0
    while Categorisation != "Normal":
        weight = int(input("𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙩𝙝𝙚 𝘿𝙪𝙣𝙜𝙚𝙤𝙣 𝘽𝙈𝙄 𝘾𝙝𝙚𝙘𝙠𝙚𝙧, 𝙥𝙡𝙚𝙖𝙨𝙚 𝙚𝙣𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙘𝙪𝙧𝙧𝙚𝙣𝙩 𝙬𝙚𝙞𝙜𝙝𝙩(𝙆𝙂 𝙩𝙤 𝙣𝙚𝙖𝙧𝙚𝙨𝙩 𝙬𝙝𝙤𝙡𝙚 𝙣𝙪𝙢𝙗𝙚𝙧):"))
        height = int(input("𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙩𝙝𝙚 𝘿𝙪𝙣𝙜𝙚𝙤𝙣 𝘽𝙈𝙄 𝘾𝙝𝙚𝙘𝙠𝙚𝙧, 𝙥𝙡𝙚𝙖𝙨𝙚 𝙚𝙣𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙘𝙪𝙧𝙧𝙚𝙣𝙩 𝙝𝙚𝙞𝙜𝙝𝙩(𝙈𝙚𝙩𝙚𝙧𝙨 𝙩𝙤 𝙣𝙚𝙖𝙧𝙚𝙨𝙩 𝙬𝙝𝙤𝙡𝙚 𝙣𝙪𝙢𝙗𝙚𝙧):"))
        print("Processing...")
        time.sleep(3)
        BMI = float(weight/(height ** 2))
        if BMI < 18.5:
            Categorisation = "Underweight"
            Advice = '''𝙈𝙚𝙖𝙨𝙪𝙧𝙚𝙨:
    .𝙄𝙣𝙘𝙧𝙚𝙖𝙨𝙚 𝙮𝙤𝙪𝙧 𝙘𝙖𝙡𝙤𝙧𝙞𝙚 𝙞𝙣𝙩𝙖𝙠𝙚 𝙗𝙮 𝙘𝙤𝙣𝙨𝙪𝙢𝙞𝙣𝙜 𝙖𝙣 𝙖𝙙𝙙𝙞𝙩𝙞𝙤𝙣𝙖𝙡 500 𝙘𝙖𝙡𝙤𝙧𝙞𝙚𝙨 𝙥𝙚𝙧 𝙙𝙖𝙮.
    .𝙄𝙣𝙘𝙡𝙪𝙙𝙚 𝙛𝙤𝙤𝙙𝙨 𝙧𝙞𝙘𝙝 𝙞𝙣 𝙥𝙧𝙤𝙩𝙚𝙞𝙣, 𝙫𝙞𝙩𝙖𝙢𝙞𝙣𝙨, 𝙖𝙣𝙙 𝙢𝙞𝙣𝙚𝙧𝙖𝙡𝙨 𝙩𝙤 𝙨𝙪𝙥𝙥𝙤𝙧𝙩 𝙮𝙤𝙪𝙧 𝙝𝙚𝙖𝙡𝙩𝙝.
    .𝙒𝙤𝙧𝙠 𝙬𝙞𝙩𝙝 𝙖 𝙙𝙞𝙚𝙩𝙞𝙩𝙞𝙖𝙣 𝙩𝙤 𝙘𝙧𝙚𝙖𝙩𝙚 𝙖 𝙝𝙚𝙖𝙡𝙩𝙝𝙮 𝙚𝙖𝙩𝙞𝙣𝙜 𝙥𝙡𝙖𝙣.
    .𝙎𝙚𝙚𝙠 𝙝𝙚𝙡𝙥 𝙛𝙤𝙧 𝙪𝙣𝙙𝙚𝙧𝙡𝙮𝙞𝙣𝙜 𝙢𝙚𝙙𝙞𝙘𝙖𝙡 𝙤𝙧 𝙢𝙚𝙣𝙩𝙖𝙡 𝙝𝙚𝙖𝙡𝙩𝙝 𝙘𝙤𝙣𝙙𝙞𝙩𝙞𝙤𝙣𝙨 𝙞𝙛 𝙣𝙚𝙘𝙚𝙨𝙨𝙖𝙧𝙮. '''
        elif BMI >= 18.5 and BMI <= 24.9:
            Categorisation = "Normal"
        elif BMI >= 25 and BMI <= 29.9:
            Categorisation = "Overweight"
            Advice = '''𝙈𝙚𝙖𝙪𝙨𝙪𝙧𝙚𝙨:
    .𝙀𝙖𝙩 𝙖 𝙝𝙚𝙖𝙡𝙩𝙝𝙮, 𝙧𝙚𝙙𝙪𝙘𝙚𝙙-𝙘𝙖𝙡𝙤𝙧𝙞𝙚 𝙙𝙞𝙚𝙩 𝙖𝙨 𝙧𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙮 𝙮𝙤𝙪𝙧 𝙂𝙋 𝙤𝙧 𝙬𝙚𝙞𝙜𝙝𝙩 𝙡𝙤𝙨𝙨 𝙢𝙖𝙣𝙖𝙜𝙚𝙢𝙚𝙣𝙩 𝙝𝙚𝙖𝙡𝙩𝙝 𝙥𝙧𝙤𝙛𝙚𝙨𝙨𝙞𝙤𝙣𝙖𝙡 (𝙨𝙪𝙘𝙝 𝙖𝙨 𝙖 𝙙𝙞𝙚𝙩𝙞𝙩𝙞𝙖𝙣).
    .𝙀𝙭𝙚𝙧𝙘𝙞𝙨𝙚 𝙧𝙚𝙜𝙪𝙡𝙖𝙧𝙡𝙮.
    .𝘾𝙤𝙣𝙨𝙞𝙙𝙚𝙧 𝙖𝙙𝙙𝙞𝙣𝙜 𝙥𝙝𝙮𝙨𝙞𝙘𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙖𝙛𝙩𝙚𝙧 𝙧𝙚𝙖𝙘𝙝𝙞𝙣𝙜 𝙖 𝙢𝙞𝙣𝙞𝙢𝙪𝙢 𝙤𝙛 10 𝙥𝙚𝙧𝙘𝙚𝙣𝙩 𝙬𝙚𝙞𝙜𝙝𝙩-𝙡𝙤𝙨𝙨 𝙜𝙤𝙖𝙡.
    .𝙏𝙖𝙡𝙠 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙙𝙤𝙘𝙩𝙤𝙧 𝙖𝙗𝙤𝙪𝙩 𝙩𝙝𝙚 𝙝𝙚𝙖𝙡𝙩𝙝 𝙗𝙚𝙣𝙚𝙛𝙞𝙩𝙨 𝙖𝙣𝙙 𝙩𝙝𝙚 𝙧𝙞𝙨𝙠𝙨 𝙤𝙛 𝙩𝙧𝙚𝙖𝙩𝙢𝙚𝙣𝙩 𝙤𝙥𝙩𝙞𝙤𝙣𝙨 𝙛𝙤𝙧 𝙚𝙭𝙩𝙧𝙚𝙢𝙚 𝙤𝙗𝙚𝙨𝙞𝙩𝙮.
    .𝘾𝙝𝙖𝙣𝙜𝙚 𝙮𝙤𝙪𝙧 𝙙𝙞𝙚𝙩. 𝙔𝙤𝙪 𝙢𝙖𝙮 𝙗𝙚 𝙧𝙚𝙛𝙚𝙧𝙧𝙚𝙙 𝙩𝙤 𝙖 𝙙𝙞𝙚𝙩𝙞𝙘𝙞𝙖𝙣 𝙬𝙝𝙤 𝙘𝙖𝙣 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪 𝙬𝙞𝙩𝙝 𝙖 𝙥𝙡𝙖𝙣 𝙩𝙤 𝙡𝙤𝙨𝙚 𝙤𝙣𝙚 𝙩𝙤 𝙩𝙬𝙤 𝙥𝙤𝙪𝙣𝙙𝙨 𝙥𝙚𝙧 𝙬𝙚𝙚𝙠.
    .𝙈𝙚𝙙𝙞𝙘𝙖𝙩𝙞𝙤𝙣. 𝙎𝙤𝙢𝙚 𝙥𝙚𝙤𝙥𝙡𝙚 𝙘𝙖𝙣 𝙗𝙚𝙣𝙚𝙛𝙞𝙩 𝙛𝙧𝙤𝙢 𝙢𝙚𝙙𝙞𝙘𝙖𝙩𝙞𝙤𝙣 𝙩𝙤 𝙝𝙚𝙡𝙥 𝙬𝙞𝙩𝙝 𝙬𝙚𝙞𝙜𝙝𝙩 𝙡𝙤𝙨𝙨 𝙛𝙤𝙧 𝙚𝙭𝙩𝙧𝙚𝙢𝙚 𝙤𝙗𝙚𝙨𝙞𝙩𝙮.
    .𝙎𝙪𝙧𝙜𝙚𝙧𝙮.
    '''
        elif BMI >= 30 and BMI < 100:
            Categorisation = "Obese"
            Advice = '''𝙈𝙚𝙖𝙪𝙨𝙪𝙧𝙚𝙨:
    .𝙀𝙖𝙩 𝙖 𝙝𝙚𝙖𝙡𝙩𝙝𝙮, 𝙧𝙚𝙙𝙪𝙘𝙚𝙙-𝙘𝙖𝙡𝙤𝙧𝙞𝙚 𝙙𝙞𝙚𝙩 𝙖𝙨 𝙧𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙮 𝙮𝙤𝙪𝙧 𝙂𝙋 𝙤𝙧 𝙬𝙚𝙞𝙜𝙝𝙩 𝙡𝙤𝙨𝙨 𝙢𝙖𝙣𝙖𝙜𝙚𝙢𝙚𝙣𝙩 𝙝𝙚𝙖𝙡𝙩𝙝 𝙥𝙧𝙤𝙛𝙚𝙨𝙨𝙞𝙤𝙣𝙖𝙡 (𝙨𝙪𝙘𝙝 𝙖𝙨 𝙖 𝙙𝙞𝙚𝙩𝙞𝙩𝙞𝙖𝙣).
    .𝙀𝙭𝙚𝙧𝙘𝙞𝙨𝙚 𝙧𝙚𝙜𝙪𝙡𝙖𝙧𝙡𝙮.
    .𝘾𝙤𝙣𝙨𝙞𝙙𝙚𝙧 𝙖𝙙𝙙𝙞𝙣𝙜 𝙥𝙝𝙮𝙨𝙞𝙘𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙖𝙛𝙩𝙚𝙧 𝙧𝙚𝙖𝙘𝙝𝙞𝙣𝙜 𝙖 𝙢𝙞𝙣𝙞𝙢𝙪𝙢 𝙤𝙛 10 𝙥𝙚𝙧𝙘𝙚𝙣𝙩 𝙬𝙚𝙞𝙜𝙝𝙩-𝙡𝙤𝙨𝙨 𝙜𝙤𝙖𝙡.
    .𝙏𝙖𝙡𝙠 𝙩𝙤 𝙮𝙤𝙪𝙧 𝙙𝙤𝙘𝙩𝙤𝙧 𝙖𝙗𝙤𝙪𝙩 𝙩𝙝𝙚 𝙝𝙚𝙖𝙡𝙩𝙝 𝙗𝙚𝙣𝙚𝙛𝙞𝙩𝙨 𝙖𝙣𝙙 𝙩𝙝𝙚 𝙧𝙞𝙨𝙠𝙨 𝙤𝙛 𝙩𝙧𝙚𝙖𝙩𝙢𝙚𝙣𝙩 𝙤𝙥𝙩𝙞𝙤𝙣𝙨 𝙛𝙤𝙧 𝙚𝙭𝙩𝙧𝙚𝙢𝙚 𝙤𝙗𝙚𝙨𝙞𝙩𝙮.
    .𝘾𝙝𝙖𝙣𝙜𝙚 𝙮𝙤𝙪𝙧 𝙙𝙞𝙚𝙩. 𝙔𝙤𝙪 𝙢𝙖𝙮 𝙗𝙚 𝙧𝙚𝙛𝙚𝙧𝙧𝙚𝙙 𝙩𝙤 𝙖 𝙙𝙞𝙚𝙩𝙞𝙘𝙞𝙖𝙣 𝙬𝙝𝙤 𝙘𝙖𝙣 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪 𝙬𝙞𝙩𝙝 𝙖 𝙥𝙡𝙖𝙣 𝙩𝙤 𝙡𝙤𝙨𝙚 𝙤𝙣𝙚 𝙩𝙤 𝙩𝙬𝙤 𝙥𝙤𝙪𝙣𝙙𝙨 𝙥𝙚𝙧 𝙬𝙚𝙚𝙠.
    .𝙈𝙚𝙙𝙞𝙘𝙖𝙩𝙞𝙤𝙣. 𝙎𝙤𝙢𝙚 𝙥𝙚𝙤𝙥𝙡𝙚 𝙘𝙖𝙣 𝙗𝙚𝙣𝙚𝙛𝙞𝙩 𝙛𝙧𝙤𝙢 𝙢𝙚𝙙𝙞𝙘𝙖𝙩𝙞𝙤𝙣 𝙩𝙤 𝙝𝙚𝙡𝙥 𝙬𝙞𝙩𝙝 𝙬𝙚𝙞𝙜𝙝𝙩 𝙡𝙤𝙨𝙨 𝙛𝙤𝙧 𝙚𝙭𝙩𝙧𝙚𝙢𝙚 𝙤𝙗𝙚𝙨𝙞𝙩𝙮.
    .𝙎𝙪𝙧𝙜𝙚𝙧𝙮.
    '''
        elif BMI > 100:
            print("𝘾𝙖𝙡𝙘𝙪𝙖𝙩𝙞𝙤𝙣𝙨 𝙨𝙪𝙘𝙚𝙨𝙨𝙛𝙪𝙡!")
            time.sleep(3)
            print("BMI value",round(BMI,2),sep="|")
            time.sleep(3)
            waiting_dots(7,3)
            print("YOU")
            time.sleep(3)
            print("ARE")
            time.sleep(3)
            print("DEAD!")
            time.sleep(3)
            print("Ending 1:No big suprise...", "https://youtu.be/PSoeUntSXlI?si=RUkrXJ-LAs_NB5wV", sep="\n")
            quit()
        else:
            print("𝘾𝙖𝙡𝙘𝙪𝙖𝙩𝙞𝙤𝙣𝙨 𝙪𝙣𝙨𝙪𝙘𝙚𝙨𝙨𝙛𝙪𝙡!")
            time.sleep(2)
            print("BMI value",round(BMI,2),sep="|")
            time.sleep(2)
            print("𝙋𝙡𝙚𝙖𝙨𝙚 𝙩𝙧𝙮 𝙖𝙜𝙖𝙞𝙣 𝙬𝙞𝙩𝙝 𝙫𝙖𝙡𝙞𝙙 𝙫𝙖𝙡𝙪𝙚𝙨")
            time.sleep(2)
            continue
        print("𝘾𝙖𝙡𝙘𝙪𝙖𝙩𝙞𝙤𝙣𝙨 𝙨𝙪𝙘𝙚𝙨𝙨𝙛𝙪𝙡!")
        time.sleep(2)
        print("BMI value",round(BMI,2),"Categorisation",Categorisation,sep="|")
        time.sleep(2)
        if Categorisation != "Normal":
            print("𝘼𝙡𝙡𝙤𝙬𝙖𝙣𝙘𝙚:𝙐𝙣𝙨𝙪𝙘𝙚𝙨𝙨𝙛𝙪𝙡")
            time.sleep(3)
            print(Advice)
        continue
def PT8th_Ice_cream_truck():
    print("Alright,now we're here, you see that icecream truck?")
    time.sleep(3)
    print("The fella in there knows me well, so when you walk up to him...")
    ice_cream_container_dict = {
        1:"Cone",
        2:"Bowl",
        3:"Cup",
        4:"Bucket"
    }
    ice_cream_scoops_dict = {
        1:"1 scoop",
        2:"2 scoops",
        3:"3 scoops",
        4:"4 scoops",
        5:"5 scoops"
    }
    ice_cream_toppings_dict = {
        1:"some flakes",
        2:"some chocolate sprinkles",
        3:"some strawberry coulis",
        4:"Some Oreo bits",
        5:"some marshmellows",
        6:"whipped cream",
        7:"some sprinkles",
        8:"some damm toffe"
    }
    ice_cream_container_price = {
        1:0.5,
        2:0.8,
        3:1.1,
        4:1.4
    }
    ice_cream_scoops_price = {
        1:1,
        2:2,
        3:3,
        4:4,
        5:5
    }
    ice_cream_toppings_price = {
        1:0.4,
        2:0.3,
        3:0.6,
        4:0.9,
        5:1,
        6:1.2,
        7:0.2,
        8:0.1
    }
    random_order_list = [ice_cream_container_dict.get(random.randint(1,len(ice_cream_container_dict))),ice_cream_scoops_dict.get(random.randint(1,len(ice_cream_scoops_dict))),ice_cream_toppings_dict.get(random.randint(1,len(ice_cream_toppings_dict)))]
    waiting_dots()
    print(random_order_list)
    print("Now move, quick!!!")
    print("And be careful, a lot mess up here....")
    time.sleep(3)
    checkout_list = []
    while checkout_list[0:3] != random_order_list:
        order_list = []
        checkout_list = []
        total_price = 0
        input("𝐻𝑒𝓁𝓁𝑜,𝓌𝑒𝓁𝒸𝑜𝓂𝑒 𝓉𝑜 𝒫𝓎𝓉𝒽𝑜𝓃 𝒯𝒽𝑒 𝟪𝓉𝒽 Strawberry 𝐼𝒸𝑒𝒸𝓇𝑒𝒶𝓂 𝓉𝓇𝓊𝒸𝓀, 𝓌𝒽𝒶𝓉 𝒸𝒶𝓃 𝐼 𝒹𝑜 𝒻𝑜𝓇 𝓎𝑜𝓊!")
        print("𝒜𝓁𝓇𝒾𝑔𝒽𝓉, 𝓌𝒽𝒶𝓉 𝒸𝑜𝓃𝓉𝒶𝒾𝓃𝑒𝓇 𝒶𝓇𝑒 𝓌𝑒 𝓉𝒶𝓁𝓀𝒾𝓃𝑔(𝓉𝓎𝓅𝑒 𝓃𝓊𝓂𝒷𝑒𝓇):")
        order_list.append(int(input(ice_cream_container_dict)))
        print("𝒜𝓃𝒹 𝒽𝑜𝓌 𝓂𝒶𝓃𝓎 𝓈𝒸𝑜𝑜𝓅𝓈 𝓎𝑜𝓊 𝓈𝒶𝓎(𝓉𝓎𝓅𝑒 𝓃𝓊𝓂𝒷𝑒𝓇):")
        order_list.append(int(input(ice_cream_scoops_dict)))
        print("𝐹𝒾𝓃𝒶𝓁𝓎, 𝑜𝓃𝑒 𝒻𝓇𝑜𝓂 𝓂𝓎 (𝒶𝓁𝓂𝑜𝓈𝓉) 𝒶𝓂𝒶𝓏𝒾𝓃𝑔 𝑜𝒸𝓉𝓊𝓅𝓁𝑒 𝓉𝑜𝓅𝓅𝒾𝓃𝑔 𝓈𝑒𝓁𝑒𝒸𝓉𝒾𝑜𝓃:(𝓉𝓎𝓅𝑒 𝓃𝓊𝓂𝒷𝑒𝓇):")
        order_list.append(int(input(ice_cream_toppings_dict)))
        print("Ｐｒｏｃｅｓｓｉｎｇ")
        checkout_list.append(ice_cream_container_dict.get(order_list[0]))#0(Assortments)
        checkout_list.append(ice_cream_scoops_dict.get(order_list[1]))#1
        checkout_list.append(ice_cream_toppings_dict.get(order_list[2]))#2
        checkout_list.append(ice_cream_container_price.get(order_list[0]))#3(Prices)
        checkout_list.append(ice_cream_scoops_price.get(order_list[1]))#4
        checkout_list.append(ice_cream_toppings_price.get(order_list[2]))#5
        total_price = (checkout_list[3] + checkout_list[4] + checkout_list[5]) * 1.2
        time.sleep(3)
        print("Ｓｕｃｅｓｓｆｕｌｌｙ ｐｒｏｃｅｓｓｅｄ！")
        print("Ice cream container",checkout_list[0],"Number of scoops",checkout_list[1],"Topping",checkout_list[2],"Total price+VAT(£/$)",total_price,sep="|")
        time.sleep(5)
        print("𝒢𝑜𝑜𝒹, 𝒾𝓈𝓃'𝓉 𝒾𝓉")
        time.sleep(5)
        print("𝐼 𝒷𝑒𝓉 𝓎𝑜𝓊 𝒷𝒶𝒹𝓁𝓎 𝓌𝒶𝓃𝓉 𝒶𝓃𝑜𝓉𝒽𝑒𝓇 𝑜𝓃𝑒....")
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
            Processing("Pumping the gas", 3, int(round((gas_dose/10)/3, 1)))
            gas_put_in += gas_dose
            print(f"\n{dose}st/nd/rd/th dose sucessfully pumped....\nYou now have {gas_put_in} gallons of gas in your tank")
            dose += 1
        if gas_put_in > max_gas:
            gas_dose = int(input(f"Alright, how much do you want to unpump for your {dose}st/nd/rd/th dose(1-50 gallons):"))
            while gas_dose > 50 or gas_dose < 1:
                gas_dose = int(input(f"Alright,now that's an invalid dose, let's try that agian(1-50 gallons):"))
            Processing("Unpumping the gas", 3, int(round((gas_dose/10)/3, 1)))
            gas_put_in -= gas_dose
            print(f"\n{dose}st/nd/rd/th dose sucessfully pumped....\nYou now have {gas_put_in} gallons of gas in your tank")
            dose += 1
    print("Thanks for refuelling at Junkie's...or whatever...")
    return dose
def Double_Authentication():
    pin_attempt = 0
    pin_attempt2 = 0
    pin = random.randint(1,10000)
    while pin_attempt != pin or pin_attempt2 != pin:
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
def SUBSWAY(sizes,bread_type,fillings,location):
    sizes_dict = {
        "3-inch":1.45,
        "6-inch":1.65,
        "9-inch":1.85,
        "MEGA 12-inch":2.05
    }
    sizes_list = list(sizes_dict.keys())

    bread_type_dict = {
        "Plain":0.40,
        "Wheat":0.65,
        "Oat":0.90,
        "Barley":1.05,
        "Garlic":1.30,
        "Cheese & herbs":1.55,
        "Italian":1.80
    }
    bread_type_list = list(bread_type_dict)
    fillings_dict = {
        "Cheese & Tomato":0.95,
        "Italian Bacon & Peperoni":1.10,
        "Tuna & Mayo":0.95,
        "Turkey & Ham":1.35,
        "Chicken Teriyaki":1.40,
        "Steak & Cheese":1.95,
        "Hunted snake":16.09,
        "Hunted chicken":2.95,
        "Meat-feast":6.99
    }
    fillings_list = list(fillings_dict)
    location_dict = {
        "Restaurant":1.05,
        "Takeway/Premium member!!!":1,
        "Drive-thru":1.025
    }
    location_list = list(location_dict)
    print("|Size", sizes_list[sizes] , "Price" , f"£{sizes_dict[sizes_list[sizes]]}" , "\n","Bread type", bread_type_list[bread_type] , "Price" , f"£{bread_type_dict[bread_type_list[bread_type]]}" , "\n","Fillings", fillings_list[fillings] , "Price" , f"£{fillings_dict[fillings_list[fillings]]}" , "\n" , "Location", location_list[location] , "Percentage change" , f"{(location_dict[location_list[location]]-1)*100:.1f}%" , "\n", "Total cost" , f"£{((sizes_dict[sizes_list[sizes]]+bread_type_dict[bread_type_list[bread_type]]+fillings_dict[fillings_list[fillings]])*location_dict[location_list[location]]):.2f}",sep="|")
def Dialogue(words):
    print(words)
    time.sleep(words.split()*0.6)















