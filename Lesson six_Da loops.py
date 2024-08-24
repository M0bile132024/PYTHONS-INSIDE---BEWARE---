# Da loops
import random
import time


line_number = 0
count = 0
while line_number < 50:
    line_number = line_number + 1
    print("Line number" , line_number , ",there oughta be a easier way to do this...")
    print("Please let there be an easier way to do lines.")
    tens = line_number * 10
    print(tens)
time.sleep(3)
maxi = int(input("How about one more number:"))
print("Phew, finnaly done!!!")
time.sleep(2)
lesson = str(input("How about you? What lesson are you in?:"))
while lesson != "Computing":
    print("Oh I'm ss- ory , please try again....")
    time.sleep(2)
    lesson = str(input("How about you? What lesson are you in?:"))
print("that is coor- rect!!!")
time.sleep(5)
while count < maxi:
    count = count + 1
    print("Is it the end of my personal school day yet.I better check for the" , count,"th time...")
    time.sleep(0.5)
name = str(input("Sorry , what was your name again?"))
while name != "Mobi":
    if name == "Dave":
        break
    print("Oh I'm ss- ory , please try again....")
    time.sleep(3)
    name = str(input("Sorry , what was your name again?"))
if name == Dave:
    print("Dave.... hey that's my na-name.")
    time.sleep(2)
    maxi = int(input("how about..... one more number....:"))
    addition = maxi + 3
    print("Thy answer... is three....")
    time.sleep(2)
    jumbleword = lesson[0] + name[1] + lesson[2] + name[3] + lesson[4]
    print(jumbleword)
    time.sleep(2)
    print("Yeah , I don't feel so well....and ... my names.... not Dave?.....(faints)")
print("that is coor- rect....(faints...)")
time.sleep(3)
print("To be continued....")
time.sleep(6)


