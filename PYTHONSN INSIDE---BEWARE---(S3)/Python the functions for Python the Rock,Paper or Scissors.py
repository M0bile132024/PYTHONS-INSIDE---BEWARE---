#Python the Functions for Python the Rock,Paper or scissors 
#Date last tested: 20/02/2026
#Author:M0bile130222

#Varibles
rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """
scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
invalid = """
                ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

              ___
             q###r
              ""
    """

#Subroutines
def draw(choice):
    if choice == 1 or choice == "Rock":
        return rock
    elif choice == 2 or choice == "Paper":
        return paper
    elif choice == 3 or choice == "Scissors":
        return scissors

#Main code,if needed
if __name__ == "__main__":
    print("Rock Paper Scissors ASCII Art")
    print("Rock")
    print(rock)
    print("Paper")
    print(paper)
    print("Scissors")
    print(scissors)
    print("Invalid")
    print(invalid)

        
