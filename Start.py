import random
from player import base_character
from tal import talents
from picky import picks
global user_health
global user_attack
global turns
global sets

turns=random.randint(3,5)

def creation():
    g=input("Enter your name: ")
    me=base_character(g,[],[])
    sets = {"a": (1000,150), "b":(2000,50), "c":(900,300), "d":(15000,120)}
    print(sets)
    basic=input("Enter your chosen set, enter only the letter.").lower()
    if basic in sets:
        me.set_add(*sets[basic])
        global user_health
        global user_attack
        user_health = sets[basic][0]
        user_attack = sets[basic][1]  
    else:
        print("Set Choice not found.")
creation()

def creating():
    more=talents([])

    kits= {"1": "Health increase by 50% of base attack decrease 20%",
                 "2": "Heath decreased by 20% of base, attack increase by 50%",
                 "3": "Health increase by 100% of base cannot attack next 2 turns",
                 "4": "Health decrease by 50% attack increase by 130%"}
    print(kits)
    skill_set=input("Choose a kit number:").lower()   

    if skill_set in kits:
        more.gain(kits[skill_set],turns)
    else:
        print("Kit number not found.")
creating()

def adventure_time():
    print("Starting journey.")
    
    travel=input("Which direction would you like to go? Used W,A,S,D").lower()
    shiny=picks()
    while user_health != 0:
        if travel==travel:
            fight=[1,2,3,4,5,6,7,8]
            steps=random.randint(1,10)
        if steps not in fight:
            print("Item found")
            print(shiny.drops(1, 2, 3))
        else:
            print("Enemy present")
adventure_time()
#choose attack or use item, after (turns) show skill allow them to use skill. 
#if attack is chosen they attack equal to the current attack #, then opponent attacks, loop till someone hits 0
def attk():
    while user_health !=0:
        hom=input("Attack or use item?").lower()
        count=1
        if hom == "attack":
            mhp=opponent_health - user_attack
            print(f"Minus {user_attack}. Opponent health is {mhp} ")
            muhp=user_health - opponent_attack
            print(f"Minus {attack}. Current health is {mhp} ")
            count=count+1
        elif hom== "item" or "use item":
            print(f"Health increased by {item}. Health:{health}")
            count=count+1
        #go back to attack

    while user_health !=0:
        print("OK")
        if count== turns:
            print("Skill active.")
            ham=input("Attack or use item?").lower()
            if ham=="attack":
                ho=input("Normal attack or skill?").lower()
            elif ho in "normal attack":
                print(f"Minus {attack}. Opponent health is {mhp} ")
                mhp=opponent_health - user_attack
                print(f"Minus {attack}. Current health is {mhp} ")
                muhp=user_attack - opponent_attack
            else:
                print("nah")
            #print(f"Health changed to {#}, Attack changed to {#}")
            #print(f"Minus {attack}. Opponent health is {mhp} ")
            #mhp=opponent_health - user_attack
            #print(f"Minus {attack}. Current health is {mhp} ")
            #muhp=user_health - opponent_attack
attk()

