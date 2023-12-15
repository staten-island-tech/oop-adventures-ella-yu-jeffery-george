import random
from player import base_character
from tal import talents
from picky import picks
global turns
turns=random.randint(3,5)
def beninging():
    g=input("Would you like to play? Yes or No? ").capitalize()
    if g=="No":
        print("Ok")
    else:
        print("Build your character.")
beninging()

g=input("Enter name:")  
              
def BASE():
    print("""
Here are the possible base stats

Set A
Health= 1000
Attack= 150

Set B
Health= 2000
Attack= 50
  
Set C      
Health= 900
Attack= 300
     
Set D       
Health= 1500
Attack= 120
        
""")
BASE()
def creation():
    basic=input("Enter your chosen set, enter only the letter.").lower()
    me=base_character(g,[],[])
    if basic=="a":
        me.set_add(1000,150)
    elif basic=="b":
        me.set_add(2000,50)
    elif basic=="c":
        me.set_add(900,300)
    elif basic=="d":
        me.set_add(1500,120)
    else:
        print("Set Choice not found.")
creation()

def KITS():
    print("Here are all possible talents")    
    print("""
Kit one: health increase by 50% of base attack decrease 20%"
Kit two: heath decreased by 20% of base, attack increase by 50%
Kit three: health increase by 200% of base, cannot attack next 2 turns
Kit four: health decrease by 50% attack increase by 130%
""")
KITS()

def creating():
    more=talents([])

    skill_set=input("Choose a kit number:").lower()   

    if skill_set=="one":
        more.gain("Health increase by 50% of base attack decrease 20%", turns)
    elif skill_set=="two":
        more.gain("Heath decreased by 20% of base, attack increase by 50%", turns)
    elif skill_set=="three":
        more.gain("Health increase by 100% of base cannot attack next 2 turns", turns)
    elif skill_set=="four":
        more.gain("Health decrease by 50% attack increase by 130%", turns)
    else:
        print("Kit number not found.")
creating()

def adventure_time():
    print("Starting journey.")

    travel=input("Which direction would you like to go? Left, right, up, down?").lower()
#randomize enemy spawn depending on what direction is chosen
    while  me(1) > 0:   #Issue 1  
        if travel==travel:
            fight=[1,2,3,4,5,6,7,8]
            steps=random.randint(1,10)
            safe=[9,10]
            
        if steps in fight:
            print("Enemy present")
        #import the opponent class
        else:
            print("Item found")
            print(random.choice(potions))
            me=safe(potions)
        
adventure_time()