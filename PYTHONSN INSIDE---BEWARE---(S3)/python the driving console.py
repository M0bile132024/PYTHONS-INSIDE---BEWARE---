# Starter pt2
# 1.Kilometers
import time
import random
def kilometers(miles):
    '''Ask the user for distance in miles and convert to kilometers'''
    return miles * 1.609344
# 2.Weather check
def weather_check(weather):
    '''Askes for weather as so to give advice for what to wear'''
    if weather == "sunny" or weather == "Sunny":
        return "....\n\nI suggest you take some sunglasses with you...."
    elif weather == "rainy" or weather == "Rainy":
        return "....\n\nI suggest you take an umbrella with you...."
    else:
        return "....\n\nGuess you do you..."
# 3.Guess the number
def guess_the_number(guess):
    '''Get random number+loop until guessed'''
    random_num = random.randint(1 , 5)
    while guess != random_num:
        print("Incorrect!")
        print("Try going a bit lower...." if guess > random_num else "Try going a bit higher....")
        guess = int(input("Give me a num!:"))
    print("Correct!")



distance = int(input("Miles you're driving today....:"))
print(f"That'll be {kilometers(distance)}km....")
time.sleep(2)
weathewr = str(input("Now if you don't mind, how's the weather outside....:"))
print(weather_check(weathewr))
time.sleep(2)
print("ok being a driving console is ridiculous,let's play a game")
time.sleep(1)
g = int(input("Give me a num!:"))
guess_the_number(g)

