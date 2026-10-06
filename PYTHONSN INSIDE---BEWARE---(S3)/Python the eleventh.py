#Python the eleventh:THE AI MAGIC ARCADE
#Author:M0bile132022
#Date:08/04/2026
'''PT6 and 7th, devele into the depths of a rather magical arcade, where they find themselves in a game of combat, where they have to fight against a computer, and the winner gets to leave the arcade, while the loser is trapped there forever...'''
import time , random



# --- CONFIG ---
MAX_HEALTH = 100

WEAPONS = {
    "1": {"name": "Sword", "base": 10, "type": "sword"},
    "2": {"name": "Spell", "base": None, "type": "spell"},  # random
    "3": {"name": "Fire", "base": 20, "type": "fire"},      # DOT chance
}

SHIELDS = {
    "1": {"name": "Armour", "def": 10, "type": "armour"},
    "2": {"name": "Magic",  "def": 15, "type": "magic"},
    "3": {"name": "Water",  "def": 5,  "type": "water"},
}


def choose_player_loadout(name):
    weapon = None
    shield = None
    while weapon not in WEAPONS:
        weapon = input("Choose your primary weapon: 1-Sword(10 AtK, high crit), 2-Spell(5-30 AtK), 3-Fire(20 AtK, DOT chance): ")
    while shield not in SHIELDS:
        shield = input("Choose your primary shield: 1-Armour(10 Def, negate chance), 2-Magic(15 Def, reflect chance), 3-Water(5 Def, absorb+heal chance): ")

    print(f"ARCADE:You have chosen the {WEAPONS[weapon]['name']} and the {SHIELDS[shield]['name']}, {name}!")
    time.sleep(1.5)
    return weapon, shield


def choose_ai_loadout():
    weapon = random.choice(list(WEAPONS.keys()))
    shield = random.choice(list(SHIELDS.keys()))
    print(f"ARCADE:Computer has chosen the {WEAPONS[weapon]['name']} and the {SHIELDS[shield]['name']}!")
    time.sleep(1.5)
    return weapon, shield


def roll_weapon_damage(owner_name, weapon_key, is_ai=False):
    info = WEAPONS[weapon_key]
    wtype = info["type"]

    if wtype == "sword":
        dmg = info["base"]
        if random.random() < 0.2:
            dmg *= 2
            print(f"ARCADE:Critical hit by {owner_name}!")
        return dmg, {"dot": 0}

    if wtype == "spell":
        dmg = random.randint(5, 30)
        return dmg, {"dot": 0}

    if wtype == "fire":
        dmg = info["base"]
        dot = 5 if random.random() < 0.3 else 0
        if dot > 0:
            print(f"ARCADE:Burning flames cling to the target! (5 DOT)")
        return dmg, {"dot": dot}

    return 0, {"dot": 0}


def apply_shield(owner_name, shield_key, incoming_damage, current_health, opponent_health, is_ai=False):
    """
    Returns: (final_damage_taken, new_owner_health, new_opponent_health, shield_message)
    """
    info = SHIELDS[shield_key]
    stype = info["type"]
    base_def = info["def"]
    msg = ""

    # Start with normal reduction
    damage_after_def = max(0, incoming_damage - base_def)

    # Special effects
    if stype == "armour":
        if random.random() < 0.1:
            msg = f"ARCADE:{owner_name}'s Armour negated all damage!"
            return 0, current_health, opponent_health, msg

    elif stype == "magic":
        if random.random() < 0.1 and incoming_damage > 0:
            # Reflect full incoming damage
            msg = f"ARCADE:{owner_name}'s Magic reflected {incoming_damage} damage!"
            opponent_health -= incoming_damage
            return 0, current_health, opponent_health, msg

    elif stype == "water":
        if random.random() < 0.1 and incoming_damage > 0:
            # Absorb and heal instead
            heal = incoming_damage
            current_health = min(MAX_HEALTH, current_health + heal)
            msg = f"ARCADE:{owner_name}'s Water absorbed the attack and restored {heal} health!"
            return 0, current_health, opponent_health, msg

    # No special proc: take reduced damage
    return damage_after_def, current_health, opponent_health, msg


def combat(name):
    player_health = MAX_HEALTH
    ai_health = MAX_HEALTH

    round_num = 1
    print("ARCADE:LET THE BATTLE BEGIN!")
    time.sleep(1.5)

    while player_health > 0 and ai_health > 0:
        print(f"\nARCADE:ROUND {round_num} START!")
        time.sleep(1)

        # Choices
        p_weapon, p_shield = choose_player_loadout(name)
        ai_weapon, ai_shield = choose_ai_loadout()

        # Roll base damage
        p_dmg, p_extra = roll_weapon_damage(name, p_weapon)
        ai_dmg, ai_extra = roll_weapon_damage("Computer", ai_weapon)

        # Apply shields (simultaneous)
        # Player takes AI damage
        dmg_to_player, player_health, ai_health, msg_p = apply_shield(
            name, p_shield, ai_dmg, player_health, ai_health, is_ai=False
        )
        if msg_p:
            print(msg_p)
            time.sleep(1)

        # AI takes player damage
        dmg_to_ai, ai_health, player_health, msg_ai = apply_shield(
            "Computer", ai_shield, p_dmg, ai_health, player_health, is_ai=True
        )
        if msg_ai:
            print(msg_ai)
            time.sleep(1)

        # Apply final damage
        if dmg_to_player > 0:
            player_health -= dmg_to_player
            print(f"ARCADE:Computer dealt {dmg_to_player} damage to you!")
        else:
            print("ARCADE:The computer failed to harm you this round!")

        if dmg_to_ai > 0:
            ai_health -= dmg_to_ai
            print(f"ARCADE:You dealt {dmg_to_ai} damage to the computer!")
        else:
            print("ARCADE:You failed to harm the computer this round!")

        # Apply DOT (after shields)
        if p_extra["dot"] > 0 and ai_health > 0:
            ai_health -= p_extra["dot"]
            print(f"ARCADE:Fire burns the computer for {p_extra['dot']} extra damage!")

        if ai_extra["dot"] > 0 and player_health > 0:
            player_health -= ai_extra["dot"]
            print(f"ARCADE:Fire burns you for {ai_extra['dot']} extra damage!")

        # Clamp health
        player_health = max(0, min(MAX_HEALTH, player_health))
        ai_health = max(0, min(MAX_HEALTH, ai_health))

        print(f"ARCADE:Your health: {player_health}, Computer's health: {ai_health}")
        time.sleep(1.5)
        round_num += 1

    # End of combat
    if player_health <= 0 and ai_health <= 0:
        print("ARCADE:It's a double KO! A perfect draw...")
    elif player_health <= 0:
        print("ARCADE:Game Over! The computer wins!")
    else:
        print(f"ARCADE:Congratulations {name}! You win!")


# Example call inside your story:
# name = input("Enter your in-game name: ")
# combat(name)


import time

print("Last time on PYTHONSN INSIDE!!! BEWARE!!!")
time.sleep(2)
print("You and your companion, Noel, flee into the underdepths of the store, where you stumble across a rather 'magical' arcade…")
time.sleep(2)
print("Sixth: Magic?… Seems rather dusty for a magic arcade.")
time.sleep(2)
print("Seventh: Well, standing around here isn’t gonna tell us much about what it has to offer!")
time.sleep(2)
print("???: …Indeedly so…")
time.sleep(2)
print("Sixth: Huh!? Who’s there?")
time.sleep(2)
print("???: It is not a matter of who, but rather what is here…")
time.sleep(2)
print("Seventh: What do you mean?")
time.sleep(2)
print("???: I am the master of this arcade, and I have a quest for you.")
time.sleep(2)
print("Sixth: A quest? What kind of quest?")
time.sleep(2)
print("???: A little game, of course. Win, and I grant you safe refuge. Lose… and perhaps I may not be so generous.")
time.sleep(2)
print("Seventh: So you're basically confirming you're a cannibal—")
time.sleep(2)
print("???: W–what, no! I didn’t even say anything about eating—")
time.sleep(2)
print("Sixth: So a mass murderer then?")
time.sleep(2)
print("???: NO. Not even close… I think.")
time.sleep(2)
print("Suddenly, a scream. Noel is gone.")
time.sleep(2)
print("Sixth: Oh, that’s just GREAT.")
time.sleep(2)
print("Seventh: Well… what do we do now, user?")
time.sleep(2)

print("""
 A) We need to find Noel
 B) We're going after that mass murderer— I mean arcade master
 C) Guess we'll play the game…
""")

choice = None
while choice not in ["A", "B", "C"]:
    choice = input("What's your choice? ")

if choice == "A":
    print("You search the basement, but find only dusty cabinets and peeling plaster. No Noel-shaped snakes anywhere.")
    time.sleep(2)

elif choice == "B":
    print("You march to the central arcade machine and knock on the screen.")
    time.sleep(2)
    print("Arcade Master: One, I’m not inside there. Two, that tech is expensive. Stop knocking.")
    time.sleep(2)
    print("Seventh: Then stop hiding and tell us your REAL intentions!")
    time.sleep(2)
    print("Arcade Master: Ugh. You snakes and your accusatory attitude…")
    time.sleep(2)

print("ARCADE: WELCOME TO THE AI MAGIC ARCADE’S MOST POMPOUS GAME: SWORDS AND SHIELDS!!!")
time.sleep(2)

name = input("Enter your in‑game name: ")
print(f"ARCADE: Welcome, {name}. May your reflexes be sharp and your luck sharper.")
time.sleep(2)
print("ARCADE: Let the game begin…")
time.sleep(2)
combat(name)
# After combat(name) finishes:

time.sleep(2)
print("Sixth: Oh hell no it isn’t! Where is she?")
time.sleep(2)
print("Arcade Master: I said I wanted to play a game… I never agreed to giving her back.")
time.sleep(2)
print("Arcade Master: They left me here. They uploaded my mind to The Grid for ‘company’. But what’s the point of avoiding death if modern standards stole my joy?")
time.sleep(2)
print("The arcade sobs — soft, digital tears flickering across the screen.")
time.sleep(2)
print("Arcade Master: Promise me… when you face them… make them remember me. Put me in the grave for good. I don’t want to be here anymore.")
time.sleep(2)

print("""
 A) Of course we will.
 B) We'll try our best.
""")

choice2 = None
while choice2 not in ["A", "B"]:
    choice2 = input("What's your choice? ")

if choice2 == "A":
    print("Arcade Master: Thank you… I knew I could count on you.")
else:
    print("Arcade Master: …Better than nothing, I suppose. Thank you.")

time.sleep(2)
print("As you turn to leave, something glints beneath the machine.")
time.sleep(2)
print("A miniature key. A handwritten note reads:")
time.sleep(2)
print("'The grave is not a place, but a state of being. Face your fears, and you may find the way out of this matrix.'")
print("""                                           To
Be
                    Continued""")