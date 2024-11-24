# Python the 7th
#Task 1:The Biggest of them all
import time 
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
time.sleep(5)
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
numbers_list[3] = float(round(numbers_list[3],2))
numbers_list[4] = float(round(numbers_list[4],2))
numbers_list.append(float(numbers_list[4]-numbers_list[3]))
#Profit(numbers_list[5])
numbers_list.append(float((numbers_list[5]/numbers_list[3])*100))
#ROI(numbers_list[6])
time.sleep(5)
print("Well then, according to my calcuations,you have currently made a profit of £",numbers_list[5] , """
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
time.sleep(5)
print("Nevertheless, during the big Snake crash of 2022, was when my business fell to the ground...")
time.sleep(5)
print("And to this day, I still have nightmares of the landlord-")
time.sleep(3)
print("Just sliding up my porch with 2 guards and to get the heck out of here...")
time.sleep(6)
print("Wait a second!")
time.sleep(1)
print("Perhaps we can help eachother out!!")
time.sleep(1)
print("""Perhaps if you slide a couple hundreds funds, I could 'Show you the exit', and I'll be able to
kick-start my carrer again!!!""")
time.sleep(3)
numbers_list.append(float(input("What you say!!!!How much!!!!!:£/$")))
#Investment out of prision(numbers_list[7]
