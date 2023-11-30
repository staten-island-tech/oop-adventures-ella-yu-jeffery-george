class actions:
    def __init__(self,health,attack,name):
        self.health = health
        self.attack = attack
        self.name = name

class attackingMove(actions):
    def __init__(self,health,attack,name,unlocked,type):
        super().__init__(health,attack,name)
        self.unlocked = unlocked
        self.type = type[0].upper() + type[1:].lower()

class item(actions):
    def __init__(self,health,name,desc,typeUseable,attEffect,defEffect):
        super().__init__(health,name)
        self.desc = desc
        self.typeUseable = typeUseable
        self.attEffect = attEffect
        self.defEffect = defEffect

response = input("What type of action do you want to make? actions, attackingMove, item: ").lower()
print(response)
theFirstOne = input("How much health should this heal for the player? ")
theSecondOne = input("How much damage to the opponent should this deal for the opponent? ")
theThirdOne = input("What's the name? ")
if response == "action":
    action = {(theThirdOne): {}}