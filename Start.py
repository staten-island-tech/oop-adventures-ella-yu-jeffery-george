import random
from player import base_character
from tal import talents
from picky import picks
from newOpponentStats import opponent
from newOpponentStats import boss
from attack import attk

def run():
    global user_health
    global user_attack
    global opponent_health
    global opponent_attack
    global ho
    global turns
    global me
    turns=random.randint(2,4)

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
            user_health, user_attack, ho = more.gain(kits[skill_set], turns, user_health, user_attack)
            return user_health, user_attack, ho
        else:
            print("Kit number not found.")
            return user_health, user_attack, ho

    def hitty():
        global user_health
        global user_attack
        global opponent_health
        global opponent_attack
        global count
        global hits1
        global hits2
        global HEH

        while opponent_health>0:
            hits1+=1
            opponent_health-=user_attack
            if opponent_health <= 0:
                break 
        while HEH>0:
            hits2+=1
            HEH-=opponent_attack
            if HEH <=0:
                break 

        if hits1<hits2:
            print("Battle results\nSuccess! Next round!")
        else:
            print("Battle results\nYou loose! Try again.")

    def adventure_time():
        global user_health
        global user_attack
        global opponent_health
        global opponent_attack
        global ho

        print("Starting journey.")
        global count
        count=0

        while True:
            global HEH
            HEH=user_health
            global hits1
            global hits2
            hits1=0
            hits2=0
            shiny=picks()
            fighty=opponent()
            #loosey=boss()

            while HEH > 0:
                travel=input("Which direction would you like to go? Use W,A,S,D to move, use stop to end the game.").lower()
                if travel =="stop":
                    print("Bye.")
                    break
                else:
                    count+=1 
                    print(f"Turn {count}")

                fight=[1,2,3,4]
                steps=random.randint(1,5)
                
                if steps not in fight:
                    print("Item found")
                    item=shiny.drops(1, 2, 3)
                    me.add_item(item)
                else:
                    print("Enemy present")
                    n = random.randint(1,60)*5
                    stats= fighty.createNewOpponent(-5,n)
                    opponent_health=stats[0]
                    opponent_attack=stats[1]
                    print(f"""Opponent has the following stats,
            Health:{opponent_health} 
            Attack:{opponent_attack}""")
            
                    while opponent_health > 0:
                        hom=input("Attack or use item?").lower()

                        if hom == "attack":
                            hitty()
                        elif hom=="item":
                            print (me.inventory)
                            user_health=picks.use_potions(user_health)
                            print(f"Health is now {user_health}")
#Fix the turn counting
                    if count%turns==0 and hits1<hits2:
                        print("Skills avaiable.")
                        ham=input("Attack, skill or use item?").lower()
                
                        if ham =="skill":
                            user_health, user_attack, ho = creating()
                            print(f"Stats updated:\nHealth: {user_health}\nAttack: {user_attack}")
                            count+=1
                            print(f"Turn {count}")
                            hitty()
                        elif ham == "attack":
                            count+=1
                            print(f"Turn {count}")
                            hitty()
                        elif ham =="item":
                            print("Which item do you wanna use?")
                            print (me.inventory)
                            user_health=picks.use_potions(user_health)
                            print(f"Health is now {user_health}")
                        else:
                            print("Error")
                            #remove the used item from the inventory
                        #if count==22:
                        #   print("Boss Present")
                        #    final=loosey.boss(-3,n)
                        #    boss_health=final[0]
                        #    boss_attack=final[1]
                            
                        #    print(f"Boss stats are the following:\nHealth: {boss_health}\nAttack: {boss_attack}")
                        #    hitty()
                            #if they win, end game

    creation()
    adventure_time()
run()

