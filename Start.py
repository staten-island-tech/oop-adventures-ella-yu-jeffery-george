import random
from player import base_character
from tal import talents
from picky import picks

global user_health
global user_attack
global turns
turns=random.randint(3,5)

def creation():
    g=input("Enter your name.")
    me=base_character(g,[],[])
    sets = {"a": (1000,150), "b":(2000,50), "c":(900,300), "d":(15000,120)}
    print(sets)
    basic=input("Enter your chosen set with health being the first value and attack being the second, enter only the letter.").lower()
    if basic in sets:
        me.set_add(*sets[basic])
        user_health = sets[basic][0]
        user_attack = sets[basic][1]
    else:
        print("Set Choice not found.")
creation()

def creating():
    more=talents([])
    kits= {"one": "Health increase by 50% of base attack decrease 20%",
            "two": "Heath decreased by 20% of base, attack increase by 50%",
            "three": "Health increase by 100% of base cannot attack next 2 turns",
            "four": "Health decrease by 50% attack increase by 130%"}
    print(kits)
    skill_set=input("Choose a kit number:").lower()   

    if skill_set in kits:
        more.gain(kits[skill_set],turns)
    else:
        print("Kit number not found.")

creating()

def adventure_time():
    print("Starting journey.")

    travel=input("Which direction would you like to go? Left, right, up, down?").lower()
#randomize enemy spawn depending on what direction is chosen
    while  me[1] > 0:   #Issue 1  
        if travel==travel:
            fight=[1,2,3,4,5,6,7,8]
            steps=random.randint(1,10)
            safe=[9,10]
            
        if steps not in fight:
            print("Item found")
            print(random.choice(potions))
            me=safe(potions)
        else:
            print("Enemy present")
            print(f"Opponent health and attack {createNewOpponent(-5,n)}")
#choose attack or use item, after (turns) show skill allow them to use skill. 
#if attack is chosen they attack equal to the current attack #, then opponent attacks, loop till someone hits 0

while user_health !=0:
    hom=input("Attack or use item?").lower()
    count=1
    if hom == "attack":
        #mhp=opponent health - user_attack
        print(f"Minus {user_attack}. Opponent health is {mhp} ")
        #muhp=user_health - opponent attack
        print(f"Minus {attack}. Current health is {mhp} ")
        count=count+1
    elif hom== "item" or "use item":
        print(f"Health increased by {item}. Health:{health}")
        count=count+1
        #go back to attack
        
    if count== turns:
        print("Skill active.")
        ham=input("Attack or use item?").lower()
        if ham=="attack":
            ho=input("Normal attack or skill?").lower()
 