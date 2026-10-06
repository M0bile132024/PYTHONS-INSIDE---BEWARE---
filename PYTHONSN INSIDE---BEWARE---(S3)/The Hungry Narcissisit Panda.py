#The Hungry Narcissisit Panda
#Date:21/02/2026
#Author:M0bile132024

#ignore this
'''
# Creating ritual calendar for Chimaobi's English Renewal Scroll and Quest Scroll over Spring Term 2026

import pandas as pd

# Define the calendar data
calendar_data = {
    "Week": [1, 2, 3, 4, 5, 6],
    "Ritual Focus": [
        "Legacy Lens: Mythic Metaphors",
        "Scroll of Echoes: Rewrite & Reflect",
        "Ceremonial Rehearsal: Dramatic Reading",
        "Legacy Lens: Character Legacy",
        "Scroll of Echoes: Mythic Essay Draft",
        "Ceremonial Rehearsal: Final Performance"
    ],
    "Milestone Goal": [
        "Choose 1 topic and reframe mythically",
        "Complete 2 rewritten paragraphs with reflection",
        "Perform 1 dramatic reading with props",
        "Analyze a character’s legacy in mythic terms",
        "Submit mythic-themed English assignment",
        "Present final reading or essay to audience"
    ],
    "Reward Ceremony": [
        "Scroll seal: Stamp your scroll",
        "Celebratory walk: Reflect on growth",
        "Legacy post: Share quote or insight",
        "Scroll seal: Add symbol of character",
        "Legacy post: Share mythic metaphor",
        "Ceremonial badge: Declare your ascent"
    ]
}

# Create DataFrame
calendar_df = pd.DataFrame(calendar_data)

# Save to CSV
output_path = "/mnt/data/Chimaobi_English_Ritual_Calendar_Spring2026.csv"
calendar_df.to_csv(output_path, index=False)

print("Created ritual calendar for Chimaobi’s English Renewal Scroll and Quest Scroll over Spring Term 2026.")
'''

#Imports
from time import sleep as s
import pyperclip


#Subroutines
def eats_it(emoji):
    '''Process emoji eaten'''
    try:
        if emoji == "alt+f4 yourself":
            print("Er- Erm BYE! >C")
            return "break"
        code_point = ord(emoji)
        binary_code = format(code_point, 'b')
        print("*chomps on it*")
        s(2)
        print(f"Emoji: {emoji}, Unicode: U+{code_point:X}, Binary: {binary_code}")
        copy_to_clipboard(f"Emoji: {emoji}, Unicode: U+{code_point:X}, Binary: {binary_code}")
        s(2)
        print("But I still want to do this all n-...noon so here we go again....")
        s(2)
        return "continue"
    except:
        print("*chomps on it*")
        s(2)
        print("Wh-what is this?It taste like c- You know what , just give me an actual emoji this time OK!")
        return "continue"
def copy_to_clipboard(result):
    '''Copy the Unicode and Binary representation to clipboard'''
    try:
        pyperclip.copy(result)
        print("Copied to clipboard!")
    except:
        print("Failed to copy to clipboard. Please try again.")
#Main code    
while True:
    emoji = input("Konichuwa,I am The Hungry Narcissisit Panda who will convert your emoji to Unicode/Binary,now hand me your ba- I mean emoji(or you can just tell me to 'alt-f4 yourself'...):").lower().strip()
    if eats_it(emoji) == "break":
        break
    else:
        continue
print("You pen-")
exit()
