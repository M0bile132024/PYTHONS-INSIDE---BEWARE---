import random

weapons = ["Sword", "Spell", "Fire"]
shields = ["Armour", "Magic", "Water"]

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None
        self.shield = None

    def damage(self):
        points = random.randint(10, 35)
        self.health -= points

    def selectWeapon(self):
        choice = int(input("Choose your weapon: 1-Sword, 2-Spell, or 3-Fire: "))
        self.weapon = choice - 1

    def selectShield(self):
        choice = int(input("Choose your shield: 1-Armour, 2-Magic, or 3-Water: "))
        self.shield = choice - 1

class AiPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def selectWeapon(self):
        choice = random.randint(1, 3)
        self.weapon = choice - 1

    def selectShield(self):
        choice = random.randint(1, 3)
        self.shield = choice - 1

class Game:
    def __init__(self):
        self.gameOver = False
        self.round = 0

    def newRound(self):
        self.round += 1
        print(f"\n*** Round: {self.round} ***\n")

    

# Setup Game Objects
currentGame = Game()
human = Player("Mark")
ai = AiPlayer("Computer")
players = [human, ai]

# Main Game Loop
while not currentGame.gameOver:
    for player in players:
        player.selectWeapon()
        player.selectShield()
        currentGame.newRound()
        currentGame.takeTurn(human, ai)
