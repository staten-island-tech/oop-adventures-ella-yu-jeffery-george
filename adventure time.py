class possibility:    
    def __init__():
        global user_health
        global user_attack
        global opponent_health
        global opponent_attack
        global ho
        global count
        count=0

        while True:
            global HEH
            HEH=user_health
            global hits1
            global hits2
            global user_health
            global user_attack
            global opponent_health
            global opponent_attack
            
            hits1=0
            hits2=0
            shiny=picks()
            fighty=opponent()

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
                        else:
                            print("Which item do you wanna use?")
                            print (me.inventory)
                            user_health=picks.use_potions(user_health)
                            print(f"Health is now {user_health}")