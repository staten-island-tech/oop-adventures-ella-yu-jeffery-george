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
fire = attackingMove(0,160,"Firethrower",18,"Fire")
print(fire)
response = input("What type of action do you want to make? actions, attackingMove, item: ").lower()
print(response[0].upper() + response[1:])
theFirstOne = int(input("How much health should this heal for the player? "))
theThirdOne = input("What's the name? ")
if response == "action":
    theSecondOne = int(input("How much damage to the opponent should this deal for the opponent? "))
    action = {"type" : "action", "name" : theThirdOne, "uses" : {"healing" : theFirstOne, "attack" : theSecondOne}}
elif response == "attackingmove":
    theSecondOne = int(input("How much damage to the opponent should this deal for the opponent? "))
    unlocked = int(input("At what level should this attack be unlocked at? "))
    typeAction = int(input("What type is this action?" ))
    action = {"type" : "attackingmove", "name" : theThirdOne, "uses" : {"healing" : theFirstOne, "attack" : theSecondOne}, "properties" : {"unlocked" : unlocked, "type" : typeAction}}
elif response == "item":
    desc = input("What description should this item have? ")
    attEffect = input("How much should it affect the ATT damage? ")
    defEffect = input("How much should it affect the defense? ")
    action = {"type" : "action", "name" : theThirdOne, "uses" : {"healing" : theFirstOne}, "properties" : {"desc" : desc, "attEffect" : attEffect, "defEffect" : defEffect}}
else:
    print("You misspelled your first response. Either write \"actions\", \"attackingMove\", or \"item\" for it. Run this again! ")

if response == "action" or "attackingmove" or "item":
    print(action)