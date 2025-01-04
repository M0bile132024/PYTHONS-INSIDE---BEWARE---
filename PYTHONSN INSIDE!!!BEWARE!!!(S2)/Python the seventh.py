# Python the 7th
#Task 1:The Biggest of them all
import time
import random 
def waiting_dots(amount_of_dots = 3,waiting_time = 1):
    for i in range(amount_of_dots):
        print(".")
        time.sleep(waiting_time)
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
    print(random_ice_cream_list)
    print("Now move, quick!!!")
    print("And be careful, a lot mess up here....")
    time.sleep(3)
    while checkout[0:3] != random_order_list:
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
print("Hi mate,i'm Python the seventh and I work in a dungeon....")
time.sleep(5)
numbers_list = []
print("It's gets boring down here, why don't you tell me some numbers?")
time.sleep(4)
for i in range(3):
    numbers_list.append(int(input("Give me a number:")))
numbers_list.sort(reverse = True)

if numbers_list[0] == numbers_list[1]:
    if numbers_list[1] == numbers_list[2]:
        print("I'd say the biggest number...")
        time.sleep(4)
        print("Is none of those, they're all the same number!")
    else:
        print("I'd say the biggest number...")
        time.sleep(4)
        print("Would had to be" , numbers_list[0])
else:
    print("I'd say the biggest number...")
    time.sleep(3)
    print("Would had to be" , numbers_list[0])
#Task 2:Businessnake
time.sleep(2)
waiting_dots()
print("You know, before I worked down here, I was a sucessful businessnake...")
time.sleep(4)
print("""I could tell a failing one from a sucessful one, and tell a near-bankrupt
one, from the next Elon Susk...""")
time.sleep(5)
print("""Say, how about I evaluate your business.After all, I don't really have
anything better to do.""")
time.sleep(4)
numbers_list.append(float(input("""How much have you invested or spent on this business?
(or any business, I don't really care)£/$""")))
#This is numbers_list[3](Investment)
numbers_list.append(float(input("""And how has this said business earned/sold? 
(or any business, I don't really care)£/$""")))
print("Processing...")
#This is numbers_list[4](Earnings)
numbers_list.append(float(numbers_list[4]-numbers_list[3]))
#Profit(numbers_list[5])
numbers_list.append(float((numbers_list[5]/numbers_list[3])*100))
#ROI(numbers_list[6])
time.sleep(5)
print("Well then, according to my calcuations,you have currently made a profit of £",round(numbers_list[5],2) , """
,and your ROI is currently sitting at""" , round(numbers_list[6],2),"%")
time.sleep(3)
if numbers_list[5] > 0:
    if numbers_list[6] > 10:
        print("In other words,that's a sucessful business you're running there buddy!")
        #5 star business
    elif numbers_list[6] > 7:
        print("In other words,that's a good business you're running there buddy.")
        #4 star business
    else:
        print("In other words,you're business is average, buddy.")
        #3 star business
else:
    if numbers_list[6] > 10:
        print("In other words,you're business is average, buddy.")
        #3 star business
    elif numbers_list[6] > 7:
        print("In other words,it seems your business running a bit low on steam.Perhaps a bubble bath ,buddy?")
        #2 star business
    else:
        print("In other words,best make sure you've got that backup business up and running before you go bankrupt,buddy!")
        #1 star business
#Task 3:Can I get a discount?
time.sleep(2)
waiting_dots(3,2)
print("Nevertheless, during the big Snake crash of 2022, was when my business fell to the ground...")
time.sleep(5)
print("And to this day, I still have nightmares of the landlord-")
time.sleep(5)
print("Just sliding up my porch with 2 guards ,telling me to get the heck out of here...")
time.sleep(7)
print("Wait a second!")
time.sleep(1)
print("Perhaps we can help eachother out!!")
time.sleep(2)
print("""Perhaps if you'd slide a couple hundreds funds, I could 'show you the exit', and I'll be able to
kick-start my carrer again!!!""")
time.sleep(3)
numbers_list.append(float(input("What you say!!!!How much!!!!!:£/$")))
#Investment out of prision(numbers_list[7])
waiting_dots(3,3)
if numbers_list[7] >= 1000.00:
    numbers_list.append(float(numbers_list[7]*0.8))
    #20% discount(numbers_list[8])
    print("Well slap my head, that's an absoulute mouthful!!!")
    time.sleep(2)
    print("In fact,just for you, a 20% discount!!!")
    time.sleep(2)
    print("£/$",round(numbers_list[8],2),"!!!")
elif numbers_list[7] < 1000.00 and numbers_list[7] >= 500.00:
    numbers_list.append(float(numbers_list[7]*0.9))
    #10% discount(numbers_list[8])
    print("Well,that's a lot.")
    time.sleep(2)
    print("Perhaps a 10% discount will work in your favor.")
    time.sleep(2)
    print("£/$",round(numbers_list[8],2),".")
else:
    numbers_list.append(float(numbers_list[7]*1.0))
    #No discount(numbers_list[8])
    print("Welp, could of been more...")
    time.sleep(2)
    print("But it's a start....")
    time.sleep(2)
    print("£/$",round(numbers_list[8],2),"...")
'''Task 4:The plan, is simple.....

4.	Write a program that asks the user for the name of the book they borrowed and then ask how many days the book is overdue.
The program should calculate the fine for overdue library books based on the number of days overdue and output the name of the
book and the total fine in a sentence at the end:
a.	1-5 days: £0.50 per day
b.	6-10 days: £1.00 per day
c.	More than 10 days: £5.00 per day
'''
time.sleep(1)
waiting_dots(5)
print("Alright, I think the coast is clear,let's go through the libary vents, they're weaker...")
time.sleep(3)
print("Some" , "Intense" , "Venting" , "Later..." , sep="\n ... \n")
waiting_dots()
print("Ok, that vent was a lot harder to break through than I thought...")
time.sleep(2)
print("But you still remember the plan?")
time.sleep(4)
print("Return the book diversion?Doesn't ring a bell??")
waiting_dots()
print("Ok, just take this book and return it to the checkout, you figure it out there.")
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
The_Dungeon_Libary()
'''Task 5:Wii Fit
5.	Write a program that calculates the Body Mass Index (BMI) and categorizes it. The program should:
a.	Take the weight (in kilograms) and height (in meters) as input.
b.	Calculate the BMI using the formula BMI
c.	Categorise the BMI:
i.	Below 18.5: Underweight
ii.	18.5 to 24.9: Normal weight
iii.	25 to 29.9: Overweight
iv.	30 and above: Obesity
'''
time.sleep(2)
print("*gunshot*")
waiting_dots(2,1)
print("What, you were taking too long.")
time.sleep(2)
print("Besides, I've managed to dismantle most of the dungeon scanners...")
time.sleep(1)
waiting_dots()
print("Ok, I couldn't dismantle the BMI checker, but don't worry;You look in a good enough condition to pass, you'll be fine...")
time.sleep(3)
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
Dungeon_BMI_Checker()
'''Task 6:The Final Icecream
Create a computer program to let the customer pick up their options for their ice cream.  

 

The customer should be able to specify: 

 

Whether they would like their ice cream to be served in a cup (50p) or on a cone (80p) 

How many scoops (£1 per scoop) they would like to order (between 1 and 4) 

Whether they would like to add a flake (40p) 

Whether they would like to add some chocolate sprinkle (30p) 

Whether they would like to add a strawberry coulis (60p) 

 

The program will then output the order and calculate the total price '''
time.sleep(1)
print("*gunshot*")
waiting_dots()   
print("Huh, forgot I had this...")
time.sleep(3)
print("Well then, no time to lose, onto the yard!")
PT8th_Ice_cream_truck()
waiting_dots()
time.sleep(5)
print("('_')")
time.sleep(5)
print("(._.)")
time.sleep(6)
print("𝒩𝑜𝓉 𝓌𝒽𝒶𝓉 𝐼 𝑒𝓍𝓅𝑒𝒸𝓉𝑒𝒹 𝓉𝑜𝒹𝒶𝓎 𝒷𝓊𝓉-")
time.sleep(1)
print("It will have to do, now MOVE!!!!")
time.sleep(5)
waiting.dots()
print("To\nBe\nContinued...")


    
            
    

        



            
                
                
                
            
                             
        
        
                   

    
        
    



    
    



    

    
    
        
        
        

