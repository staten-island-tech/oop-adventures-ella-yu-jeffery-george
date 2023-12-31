import random
from player import base_character
from tal import talents
from picky import picks
from newOpponentStats import opponent
from newOpponentStats import boss

def run():
    global user_health
    global user_attack
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
            user_health, user_attack = more.gain(kits[skill_set], turns, user_health, user_attack)
            return user_health, user_attack
        else:
            print("Kit number not found.")
            return user_health, user_attack

    def hitty():
        global user_health
        global user_attack
        global opponent_health
        global opponent_attack
        global hits1
        global hits2
        global HEH
        hits1=0
        hits2=0

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
        load=True

        while load==True:
            global HEH
            global n
            HEH=user_health
            global hits1
            global hits2
            hits1=0
            hits2=0
            shiny=picks()
            fighty=opponent()

            while HEH > 0:
                travel=input("Which direction would you like to go? Use W,A,S,D to move, use stop to end the game.").lower()
                if travel =="stop":
                    print("Bye.")
                    load= False
                    break
                elif travel in ["w","a","s","d"]:
                    count+=1 
                    print(f"Turn {count}")
                else:
                    print("Error.")
                    break

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
                            if not me.inventory:
                                print("No items in inventory")
                            else:
                                print(me.inventory)
                                user_health=picks.use_potions(user_health)
                                print(f"Health is now {user_health}")
                                me.inventory.remove(item)
                
                    if count%turns==0:
                        print("Skills avaiable.")
                        ham=input("Attack, skill or use item?").lower()
                
                        if ham =="skill":
                            user_health, user_attack = creating()
                            print(f"Stats updated:\nHealth: {user_health}\nAttack: {user_attack}")
                            count+=1
                            print(f"Turn {count}")
                            hitty()
                        elif ham == "attack":
                            count+=1
                            print(f"Turn {count}")
                            print("Enemy present")
                            hitty()
                        elif ham =="item":
                            print("Which item do you wanna use?")
                            print (me.inventory)
                            user_health=picks.use_potions(user_health)
                            print(f"Health is now {user_health}")

                        else:
                            print("Error")
                            #remove the used item from the inventory

            if count>10 and count%10==0:
                print("Boss Present")
                final=boss(-1,n)
                boss_stats=final.stats
                boss_health=boss_stats[0]
                boss_attack=boss_stats[1]
                
                print(f"Boss stats are the following:\nHealth: {boss_health}\nAttack: {boss_attack}")
                hitty()
                print("You have reached the end of the game! Rerun to play again.")
                load= False
                
    creation()
    adventure_time()
run()

