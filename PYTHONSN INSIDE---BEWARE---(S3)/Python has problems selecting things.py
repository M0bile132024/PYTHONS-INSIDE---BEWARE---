# Python has problems selecting things - You've gotta help him!
from time import sleep
#1. Problem 1: Exam Grade
def exam_grade(test_score):
    '''Write a program that
    asks the user for a test
    score (0–100) and prints
    the correct grade band.'''
    if test_score >= 70:
        return "Grade 9-7"
    elif test_score >= 50 and test_score <= 69:
        return "Grade 6-4"
    elif test_score < 50:
        return "Below 4"
    else:
        raise Exception("Is that (0-100)? :/")
#Problem 2 – Traffic Light​
def traffic_light(col):
    '''Write a program that:
    Asks the user to type a
    traffic light colour
    (red, amber, green).​'''
    if col == "red" or col == "Red":
        return "Stop"
    elif col == "amber" or col == "Amber":
        return "Get ready"
    elif col == "green" or col == "Green":
        return "Go"
    else:
        return "Not a traffic light colour"
#Problem 3 – Alarm Clock
def alarm_clock(curr_hour):
    '''Write a program that
    asks the user for the
    current hour (0–23).'''
    if curr_hour < 7:
        return "too early"
    elif curr_hour >= 7 and curr_hour <= 21:
        return "daytime"
    elif curr_hour > 21:
        return "time for bed"
    else:
        raise Exception("Is that (0–23) :/")
#Problem 4 – Login System
def login_sys(u_name,pw):
    '''Write a program
    that checks a username
    ('admin') and password
    ('secret').'''
    correct_u_name = 'admin'
    correct_pw = 'secret'

ts = -1
cn = "(0-100)"
while True:
    ts = int(input(f"User,I ask you for a test score{cn}:"))
    if ts < 0 or ts > 100:
        print(f"Is that {cn}? :/")
    else:
        break
print(f"The correct grade band is {exam_grade(ts)}")
sleep(2)
#str
ts = -1
cn = "(red, amber, green)"
thing = "traffic light colour"
while True:
    ts = input(f"User,type in a traffic light colour{cn}:")
    break
print(f"The correct {thing} is {traffic_light(ts)}")
sleep(2)
#int
ts = -1
cn = "(0–23)"
thing = "current hour"
while True:
    ts = int(input(f"User,I ask you for a {thing}{cn}:"))
    if ts < 0 or ts > 23:
        print(f"Is that {cn}? :/")
    else:
        break
print(f"The correct {thing} is {alarm_clock(ts)}")
sleep(2)
ts = [-1,-1]
cn = "(lowercase)"
thing = ["username","password"]
while True:
    for x in thing:
        ts[x] = input(f"User,type in a traffic light colour{cn}:")
    break
print(f"The correct {thing} is {traffic_light(ts)}")
sleep(2)



