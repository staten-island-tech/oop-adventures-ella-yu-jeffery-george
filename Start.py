import random
from player import base_character
from tal import talents
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
              
def creation():
    print("""
Health= 1000
Attack= 150

Health= 2000
Attack= 50
        
Health= 900
Attack= 300
        
Health= 1500
Attack= 120
        
""")

#creation()

me=base_character(g,[],[])
h=int(input("Enter the health of your choice: "))
a=int(input("Enter the attack of your choice: "))
me.set_add(h,a)


def creating():
    print("Here are all possible talents")    
    print("""
Kit one: health increase by 50% of base attack decrease 20%"
Kit two: heath decreased by 20% of base, attack increase by 50%
Kit three: health increase by 200% of base, cannot attack next 2 turns
Kit four: health decrease by 50% attack increase by 130%
""")
skill_set=input("Choose a kit: ").lower
    
more=talents([])
    
if skill_set=="kit one" or "one":
    print("Kit one selected")
    more.gain("Health increase by 50% of base attack decrease 20%", turns)
elif skill_set=="kit two" or "two":
    print("Kit two selected")
    more.gain("Heath decreased by 20% of base, attack increase by 50%", turns)
elif skill_set=="kit three" or "three":
    print("Kit three selected")
    more.gain("Health increase by 100% of base cannot attack next 2 turns", turns)
else:
    print("Kit four selected")
    more.gain("Health decrease by 50% attack increase by 130%", turns)
#creating()

def adventure_time():
    print("Starting journey.")

    travel=input("Which direction would you like to go? Left, right, up, down?").lower()
#randomize enemy spawn depending on what direction is chosen
    while h > 0:    
        if travel==travel:
            fight=[1,2,3,4,5,6,7,8]
            steps=random.randint(1,10)
        safe=[9,10]
        if steps in fight:
            print("Enemy present")
        #import the opponent class
        elif steps in safe:
            print("Item found")
        
        else:
            h=0 
    
    
#Call all functions!