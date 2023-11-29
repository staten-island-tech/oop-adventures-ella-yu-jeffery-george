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

Firethrower = attackingMove(0,240,"Firethrower AHHH IT BURNS",24,"FIRE")
print(f"\"{Firethrower.name}\" stats: Attack DMG {Firethrower.attack}, Type {Firethrower.type}")
