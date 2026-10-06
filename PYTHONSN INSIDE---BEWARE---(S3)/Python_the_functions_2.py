#Python the functions 2
#Author:M0bile132022
#Date:13/10/25
'''Functions used in season 3'''
import time
import random
import os
from webbrowser import get
import pygame
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
    i = 0
    while True:
        if i == 3:
            break
        time.sleep(2)
        print("Noel:Chose which area you wish to visit:")
        time.sleep(2)
        areas = ["Music Quiz Segment",
        "Music Select Zone",
        "The Dice game District"]
        i = 0
        for x in areas:
            i += 1
            print(f"{i}.{x}")
        area = int(input("Noel:Input the number of the area you wish to visit into this ticket machine:"))
        if area == 1:
            print(f"Ticket machine:YOU HAVE CHOSEN {areas[area-1]} , YOU MAY PROCEED")
            time.sleep(2)
            Music_Quiz_Segment()
            i += 1
        elif area == 2:
            print(f"Ticket machine:YOU HAVE CHOSEN {areas[area-1]} , YOU MAY PROCEED")
            time.sleep(2)
            Music_Select_Zone()
            i += 1
        elif area == 3:
            print(f"Ticket machine:YOU HAVE CHOSEN {areas[area-1]} , YOU MAY PROCEED")
            time.sleep(2)
            Dice_Game_District()
            i += 1
        else:
            print("Noel:Invalid choice, please try again!")
    print("Sixth:Well, I have to say Noel, this wacky shop of yours sure does provide some good entertainment!")
    time.sleep(2)
    print("Seventh:Yeah,and for once we could be worr free about being hunted down by those prison guards outside the window!")
    time.sleep(2)
    print("Sixth:(。_。)")
    time.sleep(2)
    print("Seventh:What?")
    time.sleep(2)
    print("Sixth:Ermmmm,Noel....you wouldnt happen to have a survival bunker in here as well heh....")
    time.sleep(2)
    print("Noel:Well we do have a underground arcade section.But it's being renovated so i'd suggest-")
    time.sleep(2)
    print("Seventh:WE'LL TAKE IT!PLEASE ANYTHING BUT OUTSIDE!!")
    time.sleep(2)
    print("Noel:Jeez,with the amount of noise you're making,hiding may well become obsolete!But sure, follow me!")
    
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
    i = 0
    while True:
        
        print(f"Noel:The artist is {artist_names[int(random_song_and_artist)]} and the first letter of each word in the song title is {song_names[int(random_song_and_artist)][0]}")
        first_guess = input("Noel:What is your first guess?:").lower()
        if first_guess == song_names[int(random_song_and_artist)].lower():
            print("Noel:Correct!You score 3 points!")
            time.sleep(2)
            print("Noel:Let's try another song!")
            time.sleep(2)
        else:
            print("Noel:Incorrect!You have one more chance!")
            time.sleep(2)
            second_guess = input("Noel:What is your second guess?").lower()
            if second_guess == song_names[int(random_song_and_artist)].lower():
                print("Noel:Correct!You score 1 point!")
                time.sleep(2)
                print("Noel:Let's try another song!")
                time.sleep(2)
            else:
                print(f"Noel:Incorrect!The correct answer was {song_names[int(random_song_and_artist)]}.")
                time.sleep(2)
                print("Noel:Thanks for playing!Come again!")
                break
        i += 1
        if i == 5:
            break
        random_song_and_artist = random.uniform(0,4)
        time.sleep(2)
        print("Noel:Here is your next song!")
        time.sleep(2)
    print("Noel:Alright I think that's enough of the Music Quiz Segment!Hope you enjoyed it!")
def Music_Select_Zone():
    '''Music Select Zone function'''
    print("Noel:Welcome to the Music Select Zone!")
    time.sleep(2)
    print("Noel:Here, you can select your favourite music and listen to it while you play other games!")
    time.sleep(2)
    print("Noel:Let's get started!")
    time.sleep(2)
    folder_path = input("Noel:Please enter the path to your music folder:")
    try:
        music_files = list_music_files(folder_path)
        if not music_files:
            print("No music files found in the folder.")
            return

        print("\nAvailable Songs:")
        for idx, song in enumerate(music_files, start=1):
            print(f"{idx}. {song}")

        # Get user choice
        try:
            choice = int(input("\nEnter the number of the song to play: "))
            if choice < 1 or choice > len(music_files):
                print("Invalid choice.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        selected_song = os.path.join(folder_path, music_files[choice - 1])
        play_music(selected_song)
    except FileNotFoundError as e:
        print(e)
    print("Noel:Alright I think that's enough of the Music Select Zone!Hope you enjoyed it!")

    




def list_music_files(folder_path):
    """List all .mp3 and .wav files in the given folder."""
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' does not exist.")

    music_files = [f for f in os.listdir(folder_path)
                   if f.lower().endswith(('.mp3', '.wav'))]
    return music_files

def play_music(file_path):
    """Play the selected music file."""
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Now playing: {os.path.basename(file_path)}")
        print("Press Ctrl+C to stop playback.")

        # Keep the program running while music plays
        try:
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except KeyboardInterrupt:
            print("\nPlayback stopped by user.")
            pygame.mixer.music.stop()

    except pygame.error as e:
        print(f"Error playing file: {e}")
def Dice_Game_District():
    '''Dice Game District function'''
    print("Noel:Welcome to the Dice Game District!")
    time.sleep(2)
    print("Noel:This is a two player game, so who do you want to play against?")
    time.sleep(2)
    print("Sixth:I'll try,..but I ain't going easy on ya!")
    time.sleep(2)
    print("Seventh:Dice games?Sounds fun i'm in!")
    time.sleep(2)
    choice = input("Noel:Type 'Sixth' to play against Sixth or 'Seventh' to play against Seventh:")
    while choice.lower() not in ('sixth', 'seventh'):
        print("Noel:Invalid choice. Please type 'Sixth' or 'Seventh'.")
        time.sleep(2)
        choice = input("Noel:Type 'Sixth' to play against Sixth or 'Seventh' to play against Seventh:")
    if choice.lower() == 'sixth':
        print("Sixth:Good choice!I haven't been gambling in ages so.. consider this a warmup!")
    elif choice.lower() == 'seventh':
        print("Seventh:Oh boy,this game gonna sick.Best stay on your toes User, for I won't be holding back!")
    time.sleep(2)
    print("Noel:Let's get started!")
    time.sleep(2)
    try:
        play_dice_game(choice)
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")




def roll_dice():
    """Simulate rolling a 6 sided dice and return the result."""
    return random.randint(1, 6)

def get_player_choice(player_name):
    """Ask the player if they want to roll again."""
    while True:
        choice = input(f"{player_name}, roll the dice? (y/n): ").strip().lower()
        if choice in ('y', 'n'):
            return choice
        print("Invalid choice. Please enter 'y' or 'n'.")

def play_dice_game(choice):
    print("Welcome to the Dice Game!")
    print("First player to reach 20 points wins.\n")

    # Initialize scores
    scores = {"Player 1": 0, choice: 0}


    # Game loop
    print("Let's start the game!")
    rounds = 0
    while scores["Player 1"] < 20 and scores[choice] < 20:
        print(f"\nRound {rounds + 1}")
        print(f"Current Scores: Player 1: {scores['Player 1']} | {choice}: {scores[choice]}")
        print("User's turn:")
        if get_player_choice("User") == 'y':
            roll = roll_dice()
            print(f"You rolled a {roll}!")
            scores["Player 1"] += roll
        else:
            print("You chose not to roll. Ending your turn.")
        # Here you would implement the logic for the opponent's turn (Sixth or Seventh)
        # For simplicity, let's just simulate the opponent's turn with a random roll
        print(f"{choice}'s turn:")
        if choice == 'Sixth':
            #some random dialogue snippets for sixth
            ran_dialogue = random.uniform(0,1)
            if ran_dialogue < 0.5:
                print("Sixth:Alright, let's see what I get!")
            else:
                print("Sixth:Hmm, not sure about this...")
        else:
            #some random dialogue snippets for seventh
            ran_dialogue = random.uniform(0,1)
            if ran_dialogue < 0.5:
                print("Seventh:Let's see if I can beat you this time!")
            else:
                print("Seventh:Oh, this is gonna be good!")
        opponent_roll = roll_dice()
        print(f"{choice} rolled a {opponent_roll}!")
        scores[choice] += opponent_roll
        rounds += 1
    print("Game over!")    
    if scores["Player 1"] >= 20:
        print("Congratulations! You win!")
        if choice == 'Sixth':
            #some random dialogue snippets for sixth
            ran_dialogue = random.uniform(0,1)
            if ran_dialogue < 0.5:
                print("Sixth:Darn,guess my gaming days really are behind me....")
            else:
                print("Sixth:Huh, you may have won this time,but next time,i'll be sure to bring a luckier offensive!")
        else:
            #some random dialogue snippets for seventh
            ran_dialogue = random.uniform(0,1)
            if ran_dialogue < 0.5:
                print("Seventh:Aww,I thought I was sure to win?...Oh well, guess I was wrong!")
            else:
                print("Seventh:This is why I don't play gambling games often...I just can't seem to win at them!")
    elif scores[choice] >= 20:
        print(f"Sorry, {choice} wins!")
        if choice == 'Sixth':
            #some random dialogue snippets for sixth
            ran_dialogue = random.uniform(0,1)
            if ran_dialogue < 0.5:
                print("Sixth:Whoooee, looks like I still got it!")
            else:
                print("Sixth:Not bad for a warmup, eh?")
        else:
            #some random dialogue snippets for seventh
            ran_dialogue = random.uniform(0,1)
            if ran_dialogue < 0.5:
                print("Seventh:Wow, I actually won! I guess I'm not as bad at this as I thought!")
            else:
                print("Seventh:I can't believe I won! This is amazing!")

def ran_dialogue(d1,d2):
    '''Random dialogue function'''
    ran_dialogue = random.uniform(0,1)
    if ran_dialogue < 0.5:
        print(d1)
    else:
        print(d2)









def Authentication():
    '''Authentication function'''
    print("Ticket machine:*LOUD BEEP* ERROR!AUTHENTICATION REQUIRED TO PROCEED!!!")
    time.sleep(2) 
    print("Sixth:What?But we just got here...")
    time.sleep(2)
    print("Noel:Oh don’t mind that thing, it does it very now and again.Just make a new account, I'll verify you, and you’ll be playing in a jiff!")
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
Dice_Game_District()
