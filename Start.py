import random
from player import base_character
from tal import talents
from picky import picks
from newOpponentStats import opponent

global user_health
global user_attack
global turns
global opponent_health
global opponent_attack
global ho

turns=random.randint(2,4)

def creation():
    global user_health
    global user_attack
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
creation()

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
        user_health, user_attack, ho = more.gain(kits[skill_set], turns, user_health, user_attack)
    else:
        print("Kit number not found.")

    return user_health, user_attack, ho



def adventure_time():
    global user_health
    global user_attack
    global opponent_health
    global opponent_attack
    global ho

    print("Starting journey.")
    
    shiny=picks()
    fighty=opponent()
    count=0
    count1=0
    count2=0

    while user_health > 0:
        travel=input("Which direction would you like to go? Used W,A,S,D").lower()
        if travel==travel:
            fight=[1,2,3]
            steps=random.randint(1,5)

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
                count+=1
            
                if hom == "attack":
                    while opponent_health>0:
                        count1+=1
                        opponent_health-=user_attack
                        if opponent_health <= 0:
                            break 
                    while user_health>0:
                        count2+=1
                        user_health-=opponent_attack
                        if user_health <=0:
                            break 
                    if count1<count2:
                        print("Next round")
                    else:
                        print("You loose")

                    if count%turns==0:
                        print("Skills avaiable.")
                        ham=input("Attack, skill or use item?").lower()
                
                        if ham =="skill":
                            user_health, user_attack, ho = creating()
                            print(f"Stats updated:\nHealth: {user_health}\nAttack: {user_attack}")
                            while opponent_health>0:
                                count1+=1
                                opponent_health-=user_attack
                                if opponent_health <= 0:
                                    break 
                            while user_health>0:
                                count2+=1
                                user_health-=opponent_attack
                                if user_health <=0:
                                    break 
                            if count1<count2:
                                print("Next round")
                            elif count1>count2:
                                print("You loose")

                        elif ham == "attack":
                            while opponent_health>0:
                                count1+=1
                                opponent_health-=user_attack
                                if opponent_health <= 0:
                                    break 
                            while user_health>0:
                                count2+=1
                                user_health-=opponent_attack
                                if user_health <=0:
                                    break 
                            if count1>count2:
                                print("Next round")
                            elif count1<count2:
                                print("You loose")
                        else:
                            print("Which item do you wanna use?")

creation()
while True:
    adventure_time()
    againy= input("Do you want to play again? Yes or no?").lower()
    if againy =="no":
        break


