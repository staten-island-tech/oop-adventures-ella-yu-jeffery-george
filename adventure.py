import random

class adventure:
    def __init__ (self, user_health, user_attack, turns):
        self.user_health=user_health
        self.user_attack=user_attack
        self.turns=turns
    
    def starty(self):
        print("Starting journey")
        travel=input("Which direction would you like to go? Used W,A,S,D").lower()
        shiny=picks()
        fighty=opoonent()

        while user_health >0:
            if travel==travel:
                fight=[1,2,3,4,5,6,7,8]
                steps=random.randint(1,10)
                
                if steps not in fight:
                    print("Item found")
                    print(shiny.drops(1, 2, 3))
                else:
                    print("Enemy present")
    def battling(self):
        