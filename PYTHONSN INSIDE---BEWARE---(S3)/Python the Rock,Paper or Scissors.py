#Python the Rock, Paper or Scissors
#Date last tested: 20/02/2026
#Author:M0bile130222

#Imports
from time import sleep as s
from random import choice
from Python_the_functions_for_Python_the_Rock_Paper_or_Scissors import draw
import os
try:
    os.system('cls' if os.name == 'nt' else 'clear')
except:
    print("NOTE:OS is not supported in your program.The screen will not clear after each round/n/n/n/n/n/n/n")

    

#Varibles/List
choices = ["Rock","Paper","Scissors"]
playing, invalid = True, False
rounds = 1

#Subroutines
def who_won(player_choice,opp_choice):
    '''Basically checks all possible iterations and outputs apprioate results'''
    if ((player_choice == 1 and opp_choice == "Scissors") or
    (player_choice == 2 and opp_choice == "Rock") or
    (player_choice == 3 and opp_choice == "Paper")):
        return "Looks like you've won!\nShould we play again? (type y for yes,anything else for no):"
    elif ((player_choice == 1 and opp_choice == "Paper") or
    (player_choice == 2 and opp_choice == "Scissors") or
    (player_choice == 3 and opp_choice == "Rock")):
        return "Looks like I've won!\nPerhaps one more try? (type y for yes,anything else for no):"
    else:
        return "Huh, looks like a draw.\nGuess we better try again? (type y for yes,anything else for no):"
def rock_paper_scissors(player_choice,opp_choice):
    '''1.Test if quitting,while it is string
2.Try to convert to integer
3.If it doesn't work,then do invalid iteration
4.If success then check for valid choice:Display results and winner
5.If invalid then invalid interation'''
    global invalid
    global playing
    global rounds
    if player_choice.strip() == "q" or player_choice.strip() == "Q":
        playing = False
        return "continue"
    try:
        player_choice = int(player_choice)
    except:
        invalid = True
        return "continue"
    if player_choice >= 1 and player_choice <= 3:
            print(f"You chose: {choices[player_choice-1]}!")
            print(draw(choices[player_choice-1]))
            print(f"I chose: {opp_choice}!")
            print(draw(opp_choice))
            print(who_won(player_choice,opp_choice),end='')
            try_again = input().lower().strip()
            if try_again == "n":
                playing = False
                return "continue"
            else:
                rounds += 1
                print(f"Alright then round {rounds}, coming up!")
                print()
                os.system('cls' if os.name == 'nt' else 'clear')
    else:
        invalid = True

#Main code
#Intro
print("Welcome to Rock,Paper or Scissors!")
s(2)
#Main Iteration
while playing:
    #Input selection
    if not invalid:
        print(f"Round {rounds}:")
        print()
        print("""Please chose 1.Rock, 2.Paper or 3.Scissors(type the number)
Or enter q to quit""", end=":")
    else:
        print("Invalid choice!Please try again",end=":")
        invalid = False
    #Actual input
    player_choice = input()
    #Import Random - Opponent choice
    opp_choice = choice(choices)
    #Main selection
    if rock_paper_scissors(player_choice,opp_choice) == "continue":
        continue
print("Ok,thanks for playing!")
s(2)
print("""
⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⢀⠖⠢⡀⠀⠀⠀
⠀⠀⠀⠀⠰⠊⠁⠀⠀⠀⠀⠀⠀⠈⠑⠢⣀⠀⠀⠀⠀⡞⠀⠘⠀⡆⠀⢠⠁⡠⠒⠢
⠀⠀⣠⠂⠀⣠⣴⣶⡀⠀⠀⠀⠀⢠⣦⣄⠀⠣⡀⠀⠀⢡⠀⠀⡀⠇⠀⠇⠰⠀⢠⠊
⠀⡰⠃⠀⠀⢿⣿⠿⠁⠀⠀⠀⠀⠈⠻⢿⠗⠀⠱⡀⠀⠈⢆⠀⠀⠂⠀⠈⠁⠀⡆⠀
⠰⠁⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠀⠄⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀
⢈⠀⢣⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡆⠘⢢⣀⡀⠀⣀⠀⠀⠀⠀⢠⠆⠀
⢸⠀⠘⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠸⠀⠀⠀⠀⠀⠐⠤⠤⠂⠁⠀⠀
⠀⢧⡀⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠃⢠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢿⠀⠈⠻⣿⣷⣦⣄⣀⣀⣤⣾⡿⠋⠀⣠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠑⢄⠀⠀⠀⠉⠙⠉⠉⠉⠁⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠒⠚⠲⠶⠶⠶⠾⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
    
        
	
	
            
        

          
          
          
