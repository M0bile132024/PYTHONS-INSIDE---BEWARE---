# Write your code here :-)
import time
quitting = 0
checkout = 0
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
        while checkout == 0:
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
    else:
        print("𝕿𝖍𝖆𝖙 𝖎𝖘 𝖓𝖔𝖙 𝖆 𝖔𝖕𝖙𝖎𝖔𝖓....")
        time.sleep(5)
            
        
            



























#I know where you live , you know
