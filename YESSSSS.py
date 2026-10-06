import time
import random
houses_of_hogwarts = [
"Gryffindor",
"Hufflepuff",
"Ravenclaw",
"Slytherin"
]
m8b_response_yes = [
"It is certian",
"It is decidely so",
"Without a doubt",
"Yes,defintely",
"You may rely on it",
"As I see it,yes",
"Most likely",
"The outlook of it seems good",
"Yes",
"The stars point to yes"]
m8b_response_no = [
"It is not certian",
"It is decidely not so",
"Without a doubt,never",
"No,defintely no",
"You shouldn't rely on it",
"As I see it,no",
"Most likely not",
"The outlook of it seems terrible",
"No",
"The stars point to no"]
m8b_response_maybe = [
"It is ,or perhaps not",
"Can't exactly decide on that one",
"I'm doubting that one,ask me later",
"Not sure",
"Let me think about it",
"Erm, question too hazy,try again later",
"Neither",
"There is no answer to this one.You make it up yourself",
"Maybe",
"The stars are unresponsive right now"]
#HOUSE = houses_of_hogwarts[int(random.uniform(0,3))]
#NAME = input("And what be your name,young one...:")
def sorting_hat(house,name):
    print(f"Hello wizard/witch {name} and welcome to Hogwarts!!!")
    time.sleep(2)
    print("As a new student, you shall be assigned a house in accordance with the Spirt Division's choice,which happens to be....")
    time.sleep(5)
    print(f"{house}!",end="")
    if house == "Gryffindor":
        print("Known for its great bravery and courage!")
    elif house == "Hufflepuff":
        print("Emphasizes loyalty and hard work in all they do!")
    elif house == "Ravenclaw":
        print("Values intellect and creativity!")
    elif house == "Slytherin":
        print("Ambitious,yet cunning!")
    else:
        raise Exception("How does this even happen")
#sorting_hat(HOUSE,NAME)
time.sleep(2)
print("But wait!Before you enter the building, we must frist test your wizardly...")
time.sleep(2)
print("🎱 Behold!This spirtual Magic 8 Ball shall determine your wizardly,via a question you must ask it")
time.sleep(2)
QUESTION = input("Go on, give it a try:")
def magic_8_ball(question):
    ran_var = int(random.uniform(1,3))
    if ran_var == 1:
        answer = m8b_response_yes[random.randint(0,9)]
    elif ran_var == 2:
        answer = m8b_response_no[random.randint(0,9)]
    elif ran_var == 3:
        answer = m8b_response_maybe[random.randint(0,9)]
    else:
        raise Exception("How does this even happen")
        
    print("The 8 ball speaks!")
    time.sleep(2)
    print("It says...")
    time.sleep(2)
    print(answer)
    time.sleep(2)
magic_8_ball(QUESTION)
    
