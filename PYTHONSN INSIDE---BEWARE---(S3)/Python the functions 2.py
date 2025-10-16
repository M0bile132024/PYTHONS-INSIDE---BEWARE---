#Python the functions 2
#Author:M0bile132022
#Date:13/10/25
'''Functions used in season 3'''
import time
import random
def Python_the_tenths_Hockey_n_Gambling_Music_Store():
    print("Noel:Ah, new vistors...I'm Noel, and welcome to Python the tenth's Hockey & Gambling Music Store!")
    time.sleep(2)
    print("Noel:Chose which area you wish to visit frist:")
    time.sleep(2)
    areas = ["Music Quiz Segment",
    "Music Select Zone",
    "The Dice game District",
    "The Card game Region",
    "Ice Hockey Sector"]
    i = 0
    for x in areas:
        i += 1
        print(f"{i}.{x}")
    area = int(input("Noel:Input the number of the area you wish to visit into this ticket machine"))
    if area == 1:
        print(f"Ticket machine:YOU HAVE CHOSEN {areas[area-1]} , PLEASE PROCEED")
        time.sleep(2)
        Music_Quiz_Segment()
def Music_Quiz_Segment():
    song_names = ["Press Start","10.000","Code Red","Win the race","Electrodynamix"]
    artist_names = ["MDk","Coldbreakz","Dr Phonics","ietchvader","DJ-Nate"]
    random_song = random.uniform(
    print("Noel:Welcome to Music Quiz Segment, my area :)")

