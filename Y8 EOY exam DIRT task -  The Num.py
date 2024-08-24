from time import sleep
from random import randint
def givenum():
    return int(input("Give me a num:"))
num1 = givenum()
if num1 > 100 and num1 < 2000:
    print("Good num...")
else:
    print("Bad num...")
sleep(5)
num2 = givenum()
num3 = givenum()
num4 = givenum()
totalnum = num2 + num3 + num4
if num2 == num3 and num3 == num4:
    tripletotalnum = totalnum * 3
    print("The treble of the sum of your nums is" , tripletotalnum,"...")
else:
    print("The total of your nums is" , totalnum,"...")
sleep(5)
randnum = randint(1,9)
print("I have a num between 1 and 9")
sleep(5)
guessnum = int(input("Can you guess my num?:"))
while guessnum != randnum:
    if guessnum < randnum:
        print("No, my num is higher than that")
    else:
        print("No my num is lower than that")
    guessnum = int(input("Can you guess my num?:"))
print("Yes, that is my num!Now you can have my num :)")
sleep(5)
print("And I will have your num...")

    

    

    
    
