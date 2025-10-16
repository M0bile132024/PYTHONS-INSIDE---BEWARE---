#Python the functions 2
#Author:M0bile132022
#Date:13/10/25
'''Functions used in season 3'''
import time
import random
def Python_the_tenths_Hockey_n_Gambling_Music_Store():
    '''Brief

Noel is creating a music quiz game.

The game stores a list of song names and their artist (e.g.

the band or solo artist name).

The player needs to try and guess the song name.

The game is played as follows:

· A random song name and artist are chosen.

· The artist and the first letter of each word in the

song title are displayed.

· The user has two chances to guess the name of

the song.

· If the user guesses the answer correctly the first time, they score 3 points.

· If the user guesses the answer correctly the second time, they score 1 point. The

game repeats.

· The game ends when a player guesses the song name incorrectly the second

time.


Only authorised players can play the game.

Where appropriate, input from the user should be validated.

Design, write, test and refine a system that:

1. Allows a player to enter their details, which are then authenticated to ensure that

they are an authorised player.

2. Stores a list of song names and artists in an external file.

3. Selects a song from the file, displaying the artist and the first letter of each word of

the song title.

4. Allows the user up to two chances to guess the name of the song, stopping the

game if they guess a song incorrectly on the second chance.

5. If the guess is correct, add the points to the player’s score depending on the

number of guesses.

6. Displays the number of points the player has when the game ends.

7. Stores the name of the player and their score in an external file.

8. Displays the score and player names from the external file in order of highest to lowest score.
'''
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
    random_authentication = random.uniform(0,1)
    if random_authentication < 0.5:
        Authentication()
    song_names = ["Press Start","10.000","Code Red","Win the race","Electrodynamix"]
    artist_names = ["MDk","Coldbreakz","Dr Phonics","ietchvader","DJ-Nate"]
    random_song_and_artist = random.uniform(0,4)
    print("Noel:Welcome to Music Quiz Segment, my area :)")
    time.sleep(2)
    print("Noel:Here, you can test your music knowledge and win points!")
    time.sleep(2)
    print("Noel:Let's get started!")
    time.sleep(2)
    print("Noel:The rules are simple:")
    time.sleep(2)
    print("Noel:You have two chances to guess the name of the song.")
    time.sleep(2)
    print("Noel:If you guess the answer correctly the first time, you score 3 points.")
    time.sleep(2)
    print("Noel:If you guess the answer correctly the second time, you score 1 point.")
    time.sleep(2)
    print("Noel:The game repeats until you guess the song name incorrectly the second time.")
    print("Noel:Let's begin!")
    time.sleep(2)
    print("Noel:Here is your first song!")
    time.sleep(2)
    while True:
        
        print(f"Noel:The artist is {artist_names[int(random_song_and_artist)]} and the first letter of each word in the song title is {song_names[int(random_song_and_artist)][0]}")
        first_guess = input("Noel:What is your first guess?")
        if first_guess == song_names[int(random_song_and_artist)]:
            print("Noel:Correct!You score 3 points!")
            time.sleep(2)
            print("Noel:Let's try another song!")
            time.sleep(2)
        else:
            print("Noel:Incorrect!You have one more chance!")
            time.sleep(2)
            second_guess = input("Noel:What is your second guess?")
            if second_guess == song_names[int(random_song_and_artist)]:
                print("Noel:Correct!You score 1 point!")
                time.sleep(2)
                print("Noel:Let's try another song!")
                time.sleep(2)
            else:
                print(f"Noel:Incorrect!The correct answer was {song_names[int(random_song_and_artist)]}.")
                time.sleep(2)
                print("Noel:Thanks for playing!Come again!")
                break
        random_song_and_artist = random.uniform(0,4)
        time.sleep(2)
        print("Noel:Here is your next song!")
        time.sleep(2)
def Authentication():
    '''Authentication function'''
    print("Ticket machine:*LOUD BEEP* ERROR!AUTHENTICATION REQUIRED TO PROCEED!!!")
    time.sleep(2) 

print("Sixth:What?But we just got here...")
    time.sleep(2)
    print(" Noel:Oh don’t mind that thing, it does it very now and again.Just make a new account, I'll verify you, and you’ll be playing in a jiff!")
    time.sleep(2) 
    print("Sixth:*Sigh* Well if you insist....User, do the authentication quickly so we can proceed....")
    time.sleep(2) 
    username = input("Ticket machine:Enter your desired username:")
    password = input("Ticket machine:Enter your desired password:")
    print("Ticket machine:AUTHENTICATING...")
    time.sleep(2) 
    print(f"Ticket machine:AUTHENTICATION SUCCESSFUL!WELCOME {username}!")
    time.sleep(2) 
    print("Sixth:There,now can we proceed?")
    time.sleep(2) 
    print("Noel:Of course!Enjoy the game!")
    time.sleep(2) 
    print("Sixth:*sigh* Finally....")
    
        

