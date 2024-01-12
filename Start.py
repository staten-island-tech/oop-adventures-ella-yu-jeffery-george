import random
from player import base_character
from tal import talents
from picky import picks
from newOpponentStats import opponent
from attack import attk
from adventuretime import journey

def run():
    global user_health
    global user_attack
    global me
    turns=random.randint(2,4)
    input("Would you like to play? Yes or no?").lower()
    user_begin=journey(open)

    def creation():
        global user_health
        global user_attack
        global me
        g=input("Enter your name: ")
        me=base_character(g,[],[])
        sets = {"a": (1000,250), "b":(2000,150), "c":(900,300), "d":(1500,220)}
        print(sets)
        basic=input("Enter your chosen set, enter only the letter.").lower()
        if basic in sets:
            me.set_add(*sets[basic])
            user_health = sets[basic][0]
            user_attack = sets[basic][1]  
        else:
            print("Set Choice not found.")

    def creating():
        global user_health
        global user_attack
        global ho
        more=talents([])

        kits= {"1": "Health increase by 50% of base attack decrease 20%",
        "2": "Heath decreased by 20% of base, attack increase by 50%", 
        "3": "Health increase by 100% of base health", 
        "4": "Health decrease by 50% attack increase by 130%"}

        print(kits)
        skill_set=input("Choose a skill number:").lower()   

        if skill_set in kits:
            user_health, user_attack = more.gain(kits[skill_set], turns, user_health, user_attack)
            return user_health, user_attack
        else:
            print("Kit number not found.")
            return user_health, user_attack
#run the adventure time class, have the attack class also work.

    creation()
run()

