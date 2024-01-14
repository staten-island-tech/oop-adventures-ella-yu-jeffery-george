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
    def creation(self):
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
