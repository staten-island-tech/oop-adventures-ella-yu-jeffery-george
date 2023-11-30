class base_character:
    def __init__(self,name, inventory):
        self.name= name
        self.inventory=inventory
    def set_add(self,health, attack):
        self.names.add(health, attack)
        print(f"You have chosen the following stats: {health, attack}")
