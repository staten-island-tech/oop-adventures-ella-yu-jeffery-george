class base_character:
    def __init__(self,name,numbers, inventory):
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

#leave in picky and see if it works
    #class picks():
    #    def drops(self, small,medium,large):
    #        self.small=small
    #        self.medium=medium
    #        self.large=large
    #        potions={"small": 200, "medium": 500, "large": 800}
    #        
    #        picked= random.choice(list(potions.keys()))
    #       return f"Item found: {picked} potion. Replenishes {potions[picked]} health"
    #    @staticmethod
    #    def use_potions(self, user_health):
    #        hpp=input("Which potion would you like to use? small, medium or large?").lower()
    #        if hpp=="small":
    #            user_health+=200
    #        elif hpp=="medium":
    #            user_health+=500
    #        elif hpp==("large"):
    #            user_health+=800
    #
    #        return user_health
        
        
        
    
    #def creation():
    #    global user_health
    #    global user_attack
    #    global me
    #    g=input("Enter your name: ")
    #    me=base_character(g,[],[])
    #    sets = {"a": (1000,250), "b":(2000,150), "c":(900,300), "d":(1500,220)}
    #    print(sets)
    #    basic=input("Enter your chosen set, enter only the letter.").lower()
    #    if basic in sets:
    #        me.set_add(*sets[basic])
    #        user_health = sets[basic][0]
    #        user_attack = sets[basic][1]  
    #    else:
    #        print("Set Choice not found.")
