class base_character:
    def __init__(self,name, numbers, inventory):
        self.name= name
        self.numbers=numbers
        self.inventory=inventory
    def set_add(self,health, attack):
        self.name.add(health, attack)
        print(f"You have chosen the following stats: {health},{attack}")
