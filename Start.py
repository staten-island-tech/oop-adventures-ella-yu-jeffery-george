import random
from player import base_character
from tal import talents
from picky import picks
from newOpponentStats import opponent
global user_health
global user_attack
global turns
turns=random.randint(3,5)

def creation():
    g=input("Enter your name: ")
    me=base_character(g,[],[])
    sets = {"a": (1000,150), "b":(2000,50), "c":(900,300), "d":(1500,120)}
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

    kits= {"1": "Health increase by 50% of base attack decrease 20%", "2": "Heath decreased by 20% of base, attack increase by 50%", "3": "Health increase by 100% of base cannot attack next 2 turns", "4": "Health decrease by 50% attack increase by 130%"}
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
    fighty=opponent()
    while user_health > 0:
        if travel==travel:
            fight=[1,2,3,4,5,6,7,8]
            steps=random.randint(1,10)

        if steps not in fight:
            print("Item found")
            print(shiny.drops(1, 2, 3))
        else:
            print("Enemy present")
            n = random.randint(1,60)*5
            stats= fighty.createNewOpponent(-5, n)
            opponent_health=stats[0]
            opponent_attack=stats[1]
            print(f"""Oppoenent has the following stats,
    Health:{opponent_health} 
    Attack:{opponent_attack}""")
            
        while opponent_health > 0:
            hom=input("Attack or use item?").lower()
            count=0
            if hom == "attack":
                mhp=opponent_health - user_attack
                print(f"Minus {user_attack} HP. Opponent health is now {mhp} ")
                print("Enemy turn")
                muhp=user_health - opponent_attack
                print(f"Minus {opponent_attack} HP. Current health is {muhp} ")
            count=+1

            if count== turns:
                print("Skill active.")
                ham=input("Attack or use item?").lower()
                
                if ham =="attack":
                    ho=input("Would you like to use your skill? Yes or no?").lower()
                    
                    if ho == "yes":
                        print(f"Minus {user_attack}. Opponent health is {mhp} ")
                        mhp=opponent_health - user_attack
                        print(f"Minus {user_attack}. Current health is {mhp} ")
                        muhp=user_attack - opponent_attack
                else:
                    print("nah")

adventure_time()