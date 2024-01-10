import random

class picks():
    def drops(self, small,medium,large):
        self.small=small
        self.medium=medium
        self.large=large
        potions={"small": 200, "medium": 500, "large": 800}
        
        item= random.choice(list(potions.keys())).capitalize()
        return (f"{item} potion")
    
    def use_potions(user_health):
        hpp=input("Which potion would you like to use? small, medium or large?").lower()
        if hpp=="small":
            user_health+=200
        elif hpp=="medium":
            user_health+=500
        elif hpp==("large"):
            user_health+=800

        return user_health
    
    
