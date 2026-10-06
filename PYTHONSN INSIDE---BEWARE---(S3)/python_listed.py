# List revision evidence sheet
import time
import random
def mmmmm(list):
    print(f"Mmmmmmmmmm,yes {len(list)} ruby....")
    time.sleep(2)
# Problem 1: Declare a list with items and output them.
list_of_random_things = ["DVD" , "Gum" , "Printer" , "Nail polish"]
print(list_of_random_things)
time.sleep(2)
print("You want it?")
time.sleep(2)
print("It's yours my friend!")
time.sleep(2)
print("As long as you have enough rubies!")
time.sleep(2)
# Problem 2: Ask the user to add three items to a list.
# Problem 3: Allow unlimited items and display the count.
appendable_thing = 0
while appendable_thing != "NO!":
    appendable_thing = input("GIVE ME A RUBY(unless you shout 'NO!')!:")
    if appendable_thing != "NO!":
        list_of_random_things.append(appendable_thing)
    mmmmm(list_of_random_things)
# Problem 4: Remove an item from a predefined list
appendable_thing = 0
while appendable_thing != "NO!":
    appendable_thing = input(f"{list_of_random_things}\nNOW WHAT RUBY SHALL YOU WANT(unless you shout 'NO!')!:")
    if appendable_thing in list_of_random_things:
        list_of_random_things.remove(appendable_thing)
        mmmmm(list_of_random_things)
    elif appendable_thing == "NO!":
        time.sleep(2)
        break
    else:
        print("Sorry,but I can't do credit!\nMaybe try again when you're a little....mmmmmmm knowledgable!")
        time.sleep(2)
print("....will you give me a moment to sort my ruby register:")
time.sleep(2)
random_integers = [random.randint(1, 10000) for _ in range(1000)]
random_integers.sort()
i = 0
j = 0
while True:
    i = random_integers[j]
    if i > 50:
        break
    else:
        print(f"Ruby ID {j}:{i}")
    j += 1
print("ALRIGHT THAT'S ENOUGH RUBIES!")





