import time
import random
from Python_the_second_Func import The_Bar
#Python_the_Tenth:F-string Street alpha 1.5
#Author:M0bile132022
#Date:08/08/2025
'''Description:Now on the run, the crew seeks hostage on the weridest street in Pythonic....'''
def waiting_dots(amount_of_dots = 3,waiting_time = 2):
    time.sleep(waiting_time)
def Processing(Processing="Processing",amount_of_dots = 3,waiting_time = 1):
    print(Processing,end="")
    for i in range(amount_of_dots):
        print(".",end="")
        time.sleep(waiting_time)

qa1 = None
def The_Infinite_Inn():
    print("You and your crew enter the inn, which is dimly lit, with a warm fire burning in the corner.")
    waiting_dots()
    print("Sixth:For an inn, this ain't that bad")
    waiting_dots()
    if qa1 == "A2":
        print("Seventh:Yeah it's outside was clearly telling a different story...")
    elif qa1 == "A3":
        print("Seventh:Yeah, I mean, I guess it's not that bad, but I still don't trust this likes of this place...")
    else:
        print("Seventh:Yeah, perhaps your right, it's looking rather cozy in here.")
    waiting_dots()
    print("You notice a sign on the wall that reads:")
    waiting_dots()
    print("'Welcome to The Infinite Inn!'")
    waiting_dots()
    print("'Where every room is infinite, and every stay is eternal.'")
    waiting_dots()
    print("You and your crew decide to take a seat by the fire and warm up for a while.")
    waiting_dots()
    print("As you relax, you notice a strange figure in the corner of the room, watching you intently,before at their acknowledgement, approaching you,carry an intent yet jolly smile.")
    waiting_dots()
    print("???:Hello,hello new friend, my name is Python the Tenth, and welcome back to my spectacular inn!")
    waiting_dots()
    print("Sixth:...erm,sorry but do we know you from somewhere?")
    waiting_dots()
    print("Sdventh:Yeah you're acting as if you've known us forever!")
    waiting_dots()
    print("Python the Tenth:Oh, please my friends I know many people from far and wide,all who have rested in my inn one or hundreds of times!")
    waiting_dots()
    print("Sixth + Seventh:._.")
    waiting_dots()
    print("Python the Tenth:And you, my friend, are no exception!")
    waiting_dots()
    print("Python the Tenth:You see, my inn is a place of infinite possibilities.You can rest, read, even reimagine your current predicament,it's all down to you!")
    waiting_dots()
    print("Python the Tenth:Now, I've unfortunately got matters to attend to,but allow my guest to entertain you!And yes, do help yourself to our refreshments in our bar, Waiter will be tending there tonight.")
    waiting_dots(3,5)
    print("Sixth:Well, glads that over, at least we won't rest bored")
    waiting_dots()
    print("Seventh:We'll if there's one thing certian, I don't care what user, I'm going to enjoy myself in the bar")
    waiting_dots()
    while q2 != "A" or q2 == "B" or q2 == "C":
        print("""Choices:
              - A)Rest in the inn
              - B) Read a book
              - C) Go to the bar""")
        q2 = input("").strip().upper()
        match q2:
            case "A":
                break
            case "B":
                print("You decide to take the frist book off the shelf,'A Guide To Infinity' and read , which is surprisingly interesting")
                waiting_dots()
                if "Memory_fragments" in Inventory:
                    print("You feel a strange connection to the book, as if you had already experienced this book.")
                    waiting_dots()
                    inventory_change(1,"Memory_fragments")
                    print("You feel a bit more knowledgeable about the concept of infinity.")
                else:
                    print("You learn a lot from the book, and feel a bit more knowledgeable about the concept of infinity.")
                waiting_dots()
                print("Sixth:Hey you'd been looking that thing for a good while now,must be something real intresting within those pages...")
                waiting_dots()
                print("Sixth:Reminds me of the old dungeon libary, where I used to spend my time reading books all the time...yeah those were good times...")
            case "C":
                print("You decide to go to the bar with Python the Seventh, where you find a wide selection of drinks and snacks.")
                waiting_dots()
                print("You notice a tattered sign that simply reads:")
                waiting_dots()
                print("'Loop Bar'")
                waiting_dots()
                print("As you approach the bar, the Waiter walks to the bar, blanky waiting for your orders.")
                waiting_dots()
                print("Seventh:I'll have....your finest icecream sundae please!")
                waiting_dots()
                print("The waiter held the same expression and turned to you ,giving you a old menuchode to order on.")
                waiting_dots()
                order = The_Bar()
                waiting_dots()
Inventory = {
    "Flashlights":1,
    "Glowing_books":1,
    "Syntax_keys":1
}
Location = "The_Cabin"
Sanity = 100
status = None
player_name = input("Name:")
print("\n")
print("LAST TIME ON PYTHONS_INSIDE_BEWARE!!!")
waiting_dots()
print("You barely made it through the endless subway of Python the 9th.")
waiting_dots()
print("However, now that Python the Fourth can no longer be found...")
waiting_dots()
print("We...I'm not really sure what will happen next.")
waiting_dots()
print("However, you should definitely stop fantasizing and conduct your crew because we know that the Feds are undoubtedly watching you.")
waiting_dots()
print("Right now, you and your team are standing outside the Subway cabin, attempting to decide what to do next.")
time.sleep(2)
print("Sixth:Hey user,you done brainstorming?Listen,I can already hear the police from here,and I ain't going back to that dungeon...")
waiting_dots()
print("Seventh:Yeah, I don't want to go back to that dungeon either....I mean , I certianely don't want to have to go rescue him again...(Sixth:It wasn't that hard...)")
waiting_dots()
print("Sixth:So... erm what do we do now?")
waiting_dots()
print("Seventh:Hmmmm,Well I was thinking,there is a place we can stay....that'll certianely keep us safe from the feds for a good while")
waiting_dots()
print("Sixth:Hmph,And where is said that?")
waiting_dots()
print("Seventh:Ahem,they call it ...'F-string street'.....  Nasty place that is.A lot of bad snakes roam around those,real beaters, many... who most certianely dont know how to pay for their ice-cream...(Sixth:Wow,very scary...)")
waiting_dots()
print("Sixth:Ok then,i say we take it-")
waiting_dots()
print("Seventh:Woah,woah woah,not so fast, Sixth.I mean, didn't you listen to my 'Nasty place' and 'Bad snakes' part? I mean, mind you, these people once tried to steal my entire van!")
waiting_dots()
print("Sixth:Yeah, but they didn't, did they? So let's just scuttle over there,figure out a plan, and then we roll out of there like lightining easy-peasy!")
waiting_dots()
print("Seventh:Hmmm, fair point, but you missed out on the survial part-")
waiting_dots()
print("Sixth:No you're missing out on the point, it's just a creepy street,it probably isn't as bad as you think it to be.")
waiting_dots()
print("Seventh goes slient for bit, before coiming back to the convo")
print("Seventh:y'know what?Enough chit-chatting like this, we don't have all day, I say we let the user decide, what do you say user?")
waiting_dots()
q1 = input("Do you want to go to F-string street? (yes/no): ").strip().lower()
if q1 == "no":
    print("Sixth:User, are you sure? I mean, we don't have much of a choice, and I don't want to end up in the dungeon again...")
    waiting_dots()
    print("Seventh:Yeah, I mean, we can always try to find another place, but I don't think there is one around here...")
    waiting_dots()
    print("Sudddnely,you hear a loud noise, and see a group of pythons approaching you, looking rather angry,and thus,without second thought,hop in the van to F-string Street.")
print("Sixth:Great! Let's go then!")
waiting_dots()
print("Seventh:Fine, but if they try to steal my van, I am not responsible for what happens next...")
waiting_dots()
print("You and your crew are now heading towards F-string street...")
waiting_dots(6,1)
Location = "F-string_Street"
print("You arrive at F-string street,at around sunset, and it is a nasty place indeed.The street is dimly lit, with an old sign hanging above, reading:\n")
print(f"{player_name}, you shouldn't be here....or should you....")
waiting_dots()
print("You take a quick glance at the crew, who don't seem to notice anything on he board, but shiver in the frostbiten,smoky air,as a lampost nearby flickers uncontrolably.")
waiting_dots()
print("You aslo catch sight of an inn nearby, that you guys could probably stay in for the night.")
waiting_dots()
print("Sixth:Yeah,on second thoughts, I think I'll let you lead the way....")
waiting_dots()
print("Seventh:Not so cocky now,are ya...")
waiting_dots()
print("""Choices:
- A) Approach the inn
- B) Inspect the lampost
- C) Check your inventory for anything warm""")
q2 = input("")
def sanity_change(change):
    global Sanity
    print("You feel a slight change in your perspective,which you can't explain...")
    waiting_dots()
    print("You gained:") if change > 0 else print("You lost")
    print(f"{change:-} Sanity""")
    Sanity += change

def Entrance_to_inn():
    print("You lead your crew to the inn,in which its door is locked.")
    waiting_dots()
    print("Sixth:Great it's already closed for the night")
    waiting_dots()
    print("Seventh:And I wouldn't advise a break-in at this time...")
    waiting_dots()
    print("""You also notice a codeplaque that states:
def home(): return '?'
#Safety
#Truth
#Escape""")
    waiting_dots()
    print("You suddenly reliase that you must define home")
    waiting_dots()
    print("""Choices:
- A1) Type 'safety'
- A2) Type 'truth' 
- A3) Type 'escape'""")
    qa1 = input("")
    match qa1:
        case "A1":
            print("The plaque glows yellow,and the door unlocks,allowing you and your crew to enter.")
            waiting_dots()
            print("Sixth:Wow lucky guess:D")
            waiting_dots()
            print("Seventh:It's as if you'd already done this before!")
        case "A2":
            print("The plaque glows green,and the door opens for you,allowing you and your crew to enter.")
            waiting_dots()
            print("As wellas this, a shiny purple crystal appears in front of you,floating into your inventory")
            waiting_dots()
            inventory_change(1,"Memory_fragments")
            waiting_dots()
            print("Sixth:Hey user something up?")
            waiting_dots()
            print("Seventh:Yeah you look like you just spotted a rattlesnake...")
        case "A3":
            print("The plaque glows a vivid red,before the door vaporized rightin front of your eyes,allowing you and your crew to enter.")
            waiting_dots()
            sanity_change(-2)
            waiting_dots()
            print("Sixth:User you look a bit shaken.")
            waiting_dots()
            print("Seventh:Perhaps they split vemon on the door...")
        case _:
            print("Your binary suddenly fluctuates,and the plaques flashes yellow ,opening the door,allowing you and your crew to enter.")
            waiting_dots()
            print("Sixth:Since when could you do that")
            waiting_dots()
            print("Seventh:Doesn't matter,at least we're in")

def inventory_change(change,item):
    print("You gained:") if change > 0 else print("You lost")
    print(f"{change:-} {item}""")
    if item in Inventory:
        Inventory[item] += change
    else:
        Inventory[item] = change
     


    

if q2 == "A":
    Entrance_to_inn()
    Location = "The_Inn"
elif q2 == "B":
    print("You decide to inspect the lampost.")
    waiting_dots()
    print("""On it a codeplaque reads:
f'{time}: You are {status}'""")
    waiting_dots()
    print("You try touching it,but the light flickers violently")
    waiting_dots()
    print("Sixth:Someone needs to hire a electrician B]")
    waiting_dots()
    print("Seventh:I'm pretty sure that lampost has always been like that.Real creepy stuff.")
    waiting_dots()
    print("""Choices:
- B1) Read the status  
- B2) Reformat the lampost 
- B3) Ignore it""")
    qb1 = input("")
    match qb1:
        case "B1":
            print(f"You read the codeplaque status variable = {status}")
            waiting_dots()
            sanity_change(-1)
            waiting_dots()
            print("Sixth:User you look a bit shaken.")
            waiting_dots()
            print("Seventh:Perhaps they split vemon on the post...")
        case "B2":
            print("You reformat the lightpost, the plaque glowing yellow,and the lamp stopped flickering")
            status = "Debugging"
            waiting_dots()
            print(f"You now read the codeplaque status variable = {status}")
            waiting_dots()
            print("Sixth:Now that's how you fix a lampost!")
            waiting_dots()
            print("Seventh:But...it didn't even touch the lamp....")
        case "B3"|_:
            print("You ingore the lampost.Nothing happens.")
            waiting_dots()
            print("Sixth:Not sure what I expected...")
    waiting_dots()
    Entrance_to_inn()
elif q2 == "C":
    print("You open your inventory.It appears to be a literal dictionary")
    print(Inventory)
    print("""Choices:
- C1) Equip flashlight 
- C2) Search for hidden item  
- C3) Close inventory""")
    qc1 = input("")
    match qc1:
        case "C1":
            print("You use the flashlight.Your crew was slighty warmed")
            waiting_dots()
            print("Seventh:You sure their isn't a heater within that book?")
        case "C2":
            print("You search the dictionary")
            waiting_dots(4)
            print("You found a slivery key within some stuck pages,which floated into your inventory page")
            waiting_dots()
            inventory_change(1,"Syntax_keys")
        case "C3"|_:
            print("You close your inventory.")
    Entrance_to_inn()
else:
    print("Sixth:Oh my god, it'sfreezing out here people!I say we go check that inn out.")
    waiting_dots()
    print("Seventh:*shivering and whispering* For once he actuallyhas point. After all their houses service can't be that bad...")
    waiting_dots()
    Entrance_to_inn()




        

    

