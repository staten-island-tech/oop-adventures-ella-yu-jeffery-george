import random
class base_character:
    def __init__(self,name, numbers, inventory):
        self.name= name
        self.numbers=numbers
        self.inventory=inventory

    def set_add(self,health, attack):
        self.numbers.append(health)
        self.numbers.append(attack)
        print(f"""You have chosen the following stats: 
Health: {health} 
Attack: {attack}
""")
    def add_item(self, picked):
        self.inventory.append(picked)
        print(f"Added to inventory. {picked}")

class picks():
    def drops(self, small,medium,large):
        self.small=small
        self.medium=medium
        self.large=large
        potions={"small": 200, "medium": 500, "large": 800}
        
        picked= random.choice(list(potions.keys()))
        return f"Item found: {picked} potion. Replenishes {potions[picked]} health"
    @staticmethod
    def use_potions(self, user_health):
        hpp=input("Which potion would you like to use? small, medium or large?").lower()
        if hpp=="small":
            user_health+=200
        elif hpp=="medium":
            user_health+=500
        elif hpp==("large"):
            user_health+=800

        return user_health