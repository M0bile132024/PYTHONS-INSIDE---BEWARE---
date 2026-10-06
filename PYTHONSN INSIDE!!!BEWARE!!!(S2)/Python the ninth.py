#Pthon The 9th:SUBSWAY
'''Task:Do subway

Eat Fresh Menu
Size:
6-Inch (£1.65) or
12-Inch (£2.05)
Bread Type:
Plain (£0.40),
Wheat (£0.65),
Italian (£0.75),
Cheese & Herbs (£0.80)
Fillings:
Cheese & Tomato (£0.95)
Italian Bacon & Peperoni (£1.10)
Tuna & Mayo (£0.95)
Turkey & Ham (£1.35)
Chicken Teriyaki (£1.40)
Steak & Cheese (£1.95)
Desirable Additions:
Add an additional 5% fee if the customer is eating in the restaurant, as opposed to taking it away
# Your dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Convert dictionary keys to a list
keys = list(my_dict.keys())

# Access the first key and its value
first_key = keys[0]
value = my_dict[first_key]

print(f"The first key is '{first_key}' with the value {value}")
'''
import time
from Python_the_Functions import Processing as Process,waiting_dots as WD
def SUBSWAY(sizes,bread_type,fillings,location):
    sizes_dict = {
        "3-inch":1.45,
        "6-inch":1.65,
        "9-inch":1.85,
        "MEGA 12-inch":2.05
    }
    sizes_list = list(sizes_dict.keys())

    bread_type_dict = {
        "Basic Plain":0.40,
        "Wheat":0.65,
        "Breakfast Oat":0.90,
        "Barley":1.05,
        "Garlic":1.30,
        "Cheesy herbs+MORE CHEESE":1.55,
        "Pitalia":1.80
    }
    bread_type_list = list(bread_type_dict)
    fillings_dict = {
        "Cheese & Tomato":0.95,
        "Pitalia Bacon & Peperoni":1.10,
        "Tuna & Mayo":0.95,
        "Turkey & Ham":1.35,
        "Chicken Teriyaki":1.40,
        "Steak & Cheese":1.95,
        "just snake":16.09,
        "Hunted chicken":2.95,
        "Meat-feast":6.99
    }
    fillings_list = list(fillings_dict)
    location_dict = {
        "Restaurant":1.05,
        "Shouldn't have chosen this":1.5,
        "Drive-thru":1.025
    }
    location_list = list(location_dict)
    print("|Size", sizes_list[sizes] , "Price" , f"£{sizes_dict[sizes_list[sizes]]}" , "\n","Bread type", bread_type_list[bread_type] , "Price" , f"£{bread_type_dict[bread_type_list[bread_type]]}" , "\n","Fillings", fillings_list[fillings] , "Price" , f"£{fillings_dict[fillings_list[fillings]]}" , "\n" , "Location", location_list[location] , "Percentage change" , f"{(location_dict[location_list[location]]-1)*100:.1f}%" , "\n", "Total cost" , f"£{((sizes_dict[sizes_list[sizes]]+bread_type_dict[bread_type_list[bread_type]]+fillings_dict[fillings_list[fillings]])*location_dict[location_list[location]]):.2f}",sep="|")
print("Welcome to the Python the 9th Subway, the most unsuspicious subway across the Pythonic East!!!!")
time.sleep(4)
print("With hundreds of the most unique toppings to put on that bread bun, here at PT9 Subway, we do that, with 200% the love.....")
time.sleep(4)
print("*sniffs*Feeling hungry?Then smash that enter key, for were going to make you...")
time.sleep(4)
print("THE")
time.sleep(1)
print("BEST")
time.sleep(1)
print("SUB")
time.sleep(1)
print("KNOWN")
time.sleep(1)
print("TO")
time.sleep(1)
print("SNAKE")
time.sleep(3)
input("getit?for we're snakes and you-you know what,nevermind just hit enter...")
print("GREAT!Let's get started!")
quitting = "a"
while len(quitting) < 2:
    print("""Let's start with i n c h e s-and I mean, I N C H E S; size always matters around these parts
          |
          |
          |
          v
          Type 0 for our 3 inch sandwich(£1.45),
          1 for our 6(1.65)
          2 is 9(£1.85)
          and 3 is for the MEGA 12-inch(£2.05)""")
    size = int(input("Take your choice:"))
    while size < 0 or size > 3:
        print("Oh, it seems that ain't on the menu, please try again")
        time.sleep(2)
        print("""Let's start with i n c h e s-and I mean, I N C H E S; size always matters around these parts
          |
          |
          |
          v
          Type 0 for our 3 inch sandwich(£1.45),
          1 for our 6(1.65)
          2 is 9(£1.85)
          and 3 is for the MEGA 12-inch(£2.05)""")
        size = int(input("Take your choice:"))
    print("""Next on the list:BREAD TYPES!You can't have your perfect sandwich without a good selection of BREAD
          |
          |
          |
          v
          Type 0 for our most basic Plain(40p),
        1 for the Wheat(65p)
        2 for Breakfast Oat bread(90p)
        3 for Drunken Barley(£1.05),
        4 for XL large Garlic bread(£1.30)
        5 for the Cheesy herbs and more cheese,encrusted in wheat(£1.55),
        And 6 for our orign bread Pitalia!(£1.80)""")
    bread_type = int(input("Take your choice:"))
    while bread_type < 0 or bread_type > 6:
        print("Oh, it seems that ain't on the menu, please try again")
        time.sleep(2)
        print("""Next on the list:BREAD TYPES!You can't have your perfect sandwich without a good selection of BREAD
          |
          |
          |
          v
          Type 0 for our most basic Plain(40p),
        1 for the Wheat(65p)
        2 for Breakfast Oat bread(90p)
        3 for Drunken Barley(£1.05)
        4 for XL large Garlic bread(£1.30)
        5 for the Cheesy herbs and more cheese,encrusted in wheat(£1.55)
        And 6 for our orign bread Pitalia!(£1.80)""")
        bread_type = int(input("Take your choice:"))
    print("""Thridly, fillings, fillings and more fillings.I pride myself on coming up with these personally....NOT saying that this menu is made up, but-nevermind
          |
          |
          |
          v
        Type 0 for Cheese & Tomato(very acceptable on subs, not sandwiches(wait did I say sandwich before....))(95p),
        Type 1 for that Pitalia Bacon & Peperoni(£1.10)
        Type 2 for the highschool Tuna & Mayo(95p)
        Type 3 for the X2 Turkey & Ham(£1.35)
        Type 4 for that Chicken Teriyaki!(£1.40)
        Type 5 for some juicy Steak & Cheese(£1.95)
        Type 6 for HUNT THE SNAKE!!!- I-I-Mean snake.Yes, just snake(16.09)
        Type 7 for chicken...(£2.95)
        And 8 for a meaty(not bloody)feast....(£6.99)""")
    fillings = int(input("Take your choice(quickly...):"))
    while fillings < 0 or fillings > 8:
        print("Oh, it seems that ain't on the menu, please try.... again....")
        time.sleep(2)
        print("""Fillings....
          |
          |
          |
          v
        Type 0 for Cheese & Tomato(acceptable on subs)(95p),
        Type 1 for the Pitalia Bacon & Peperoni(£1.10)
        Type 2 for the highschool Tuna & Mayo(95p)
        Type 3 for the X2 Turkey & Ham(£1.35)
        Type 4 for Chicken Teriyaki(£1.40)
        Type 5 for juicy Steak & Cheese(£1.95)
        Type 6 for just snake(soon....)(16.09)
        Type 7 for chicken(£2.95)
        And 8 for meatfeast(£6.99)""")
        fillings = int(input("Take your choice(now):"))
    print("""Now for consistency issues,tell us solemely
        Type 0 if you think you're in a restaurant
        And type 1, if you think you're taking away(though only our premuim members can/SHOULD be doing that)
        ....
        Oh ok, and type 2 if you think your in a drive thru""")
    location = int(input("Don't make me ask twice...."))
    while location < 0 or location > 2:
        print("Do you think I have time for your jibbering....")
        time.sleep(2)
        print("""Now for consistency issues,tell us solemely
        Type 0 if you think you're in a restaurant
        And type 1, if you think you're taking away(though only our premuim members can/SHOULD be doing that)
        ....
        Oh ok, and type 2 if you think your in a drive thru""")
        location = int(input("Don't make me ask more than twice...."))
    if location == 0:
        print("...See,all good")
    elif location == 1:
        print("Do you any details,NO!")
        time.sleep(2)
        print("Doesn't matter,it's already too late for you....")
    elif location == 2:
        print("You stoobid")
    else:
        try:
          print(x) # type: ignore
        except:
          print("Idiot")
    time.sleep(3)
    Process()
    print("\n")
    SUBSWAY(size,bread_type,fillings,location)
    time.sleep(4)
    print("But here's the thing...")
    time.sleep(4)
    print("There never was a sub....")
    time.sleep(4)
    print("This is an infinite loop distraction...")
    quitting = input("And no matter how hard you try, your crew will never defeat Python the Frist.Or as you know him better, Pythonic...")
print("Ah!Why you spit on my neck!!")
time.sleep(2)
print("And why specifically on my infinite... looping ....membrane..... device")
WD()
def Dialogue(words):
    print(words)
    time.sleep(float(len(words.split()))*0.6)

Dialogue("𝘜𝘴𝘦𝘳?")
Dialogue("𝙐𝙨𝙚𝙧 𝙬𝙝𝙚𝙧𝙚 𝙝𝙖𝙫𝙚 𝙮𝙤𝙪 𝙗𝙚𝙚𝙣!")
Dialogue("𝘼𝙨 𝙨𝙤𝙤𝙣 𝙖𝙨 𝙬𝙚 𝙤𝙥𝙚𝙣𝙚𝙙 𝙩𝙝𝙖𝙩 𝙙𝙤𝙤𝙧,𝙮𝙤𝙪 𝙟𝙪𝙨𝙩...𝙙𝙞𝙨𝙨𝙖𝙥𝙥𝙚𝙧𝙚𝙙!")
Dialogue("𝘈𝘯𝘥 𝘭𝘦𝘧𝘵 𝘶𝘴 𝘵𝘰 𝘧𝘪𝘨𝘩𝘵 𝘵𝘩𝘦𝘴𝘦 𝘨𝘰𝘰𝘯𝘴 𝘢𝘭𝘰-")
Dialogue("ENOUGH!")
time.sleep(3)
Dialogue("Well,seeming you guys all figured out what going on here.... ")
print("I'll report back to Pythonic!And then you'll all be-")
time.sleep(1.5)
Dialogue("*gunshot*")
time.sleep(3)
Dialogue("𝘒𝘦𝘦𝘱 𝘧𝘰𝘳𝘨𝘦𝘵𝘵𝘪𝘯𝘨 𝘐 𝘩𝘢𝘷𝘦 𝘵𝘩𝘪𝘴...")
Dialogue("""To
         Be
         Continued
         Next
         Season...""")





