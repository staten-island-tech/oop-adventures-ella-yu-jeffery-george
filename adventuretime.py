import random
from player import base_character
from tal import talents
from picky import picks
from newOpponentStats import opponent, boss
from attack import attk 

class journey:    
    def __init__(self,go_e, user_health, user_attack, inventory,me,turns):
        self.go_e=go_e
        self.user_health=user_health
        self.user_attack=user_attack
        self.inventory=inventory
        self.me=me
        self.turns=turns

    def go(self):
        if self.go_e =="yes":
            print("Starting journey")
            load=True
            count= 0

            while load:
                HEH=self.user_health
                hits1=0
                hits2=0
                shiny=picks()
                fighty=opponent()
                hits=attk()
                skill_set=talents(self.me)

                while HEH > 0:
                    travel=input("Which direction would you like to go? Use W,A,S,D to move, use stop to end the game.").lower()
                    if travel =="stop":
                        print("Bye.")
                        load=False
                        break
                    elif travel in ["w", "a", "s", "d"]:
                        count+=1 
                        print(f"Turn {count}")
                        fight=[1,2,3]
                        steps=random.randint(1,5)
                        
                        if steps not in fight:
                            print("Item found")
                            item=shiny.drops(1, 2, 3)
                            self.me.add_item(item)
                        else:
                            print("Enemy present")
                            n = random.randint(1,60)*5
                            stats= fighty.createNewOpponent(-5,n)
                            opponent_health=stats[0]
                            opponent_attack=stats[1]
                            print(f"Opponent has the following stats,\nHealth:{opponent_health}\nAttack:{opponent_attack}")
                            
                            while opponent_health > 0:
                                hom=input("Attack or use item?").lower()
                                if hom == "attack":
                                    hits.hitty(hits1, hits2, opponent_health, opponent_attack, self.user_attack, HEH)
                                    break
                                elif hom=="item":
                                    if item in self.me.inventory:
                                        print(self.me.inventory)
                                        self.user_health=picks.use_potions(self, self.user_health, self.me.inventory)
                                        print(f"Health is now {self.user_health}")
                                        self.me.inventory.remove(item)
                                    elif not self.me.inventory:
                                        print("No items in inventory")
                                    else:
                                        print(f"{item} not found in inventory.")
                                    break

                            if count%self.turns==0:
                                print("Skills avaiable.")
                                ham=input("Attack, skill or use item?").lower()
                        
                                if ham =="skill":
                                    count+=1
                                    print(f"Turn {count}")
                                    user_health, self.user_attack= skill_set.creating(self.turns,self.user_health, self.user_attack)
                                    hits.hitty(hits1, hits2, opponent_health, opponent_attack, self.user_attack, HEH)
                                elif ham == "attack":
                                    count+=1
                                    print(f"Turn {count}")
                                    print("Enemy present")
                                    hits.hitty(hits1, hits2, opponent_health, opponent_attack, self.user_attack, HEH)
                                elif ham =="item":
                                    print("Which item do you wanna use?")
                                    print (self.me.inventory)
                                    user_health=picks.use_potions(user_health)
                                    print(f"Health is now {user_health}")
                                    self.me.inventory.remove(item)
                                else:
                                    print("Error")

                        if count>10 and count%10==0:
                            print("Boss Present")
                            final=boss(-1,n)
                            boss_stats=final.stats
                            boss_health=boss_stats[0]
                            boss_attack=boss_stats[1]
                            
                            print(f"Boss stats are the following:\nHealth: {boss_health}\nAttack: {boss_attack}")
                            hits.hitty(hits1, hits2, boss_health, boss_attack, self.user_attack, HEH)
                            print("You have reached the end of the game! Rerun to play again.")
                            load= False
                else:
                    print("Rerun to play.")
print("K")