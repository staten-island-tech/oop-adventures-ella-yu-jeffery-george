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
    
class safe(base_character):
    def __init__(self,name, numbers, inventory):
        super().__init__(name, numbers, inventory)
        self.label=label
        self.safe.append(inventory)