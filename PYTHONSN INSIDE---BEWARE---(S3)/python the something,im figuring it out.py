# Starter
# 1.Hello Dave
import time
def Hello_Dave(username):
    ''' Askes for the username and give special
    greeting if username == Dave'''
    if username == "Dave":
        return "HeLlO DaVe!"
    elif username == "I....am-":
        return "STEVE"
    else:
        return "hello you....."
# 2.Add Three
def Add_Three(numlist):
    ''' Asks for three nums,sum and display'''
    return sum(numlist)
user_name = input("What is your name?:")
print(Hello_Dave(user_name))
time.sleep(2)
num_list = []
for i in range(3):
    num = int(input("Give me a num!:"))
    num_list.append(num)
print(f"Le numero uno is {Add_Three(num_list)}")
