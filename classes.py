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

def tryInt(x):
    try:
        l = int(input(x))
    except:
        print("It should be an integer. Try again!")
        tryInt(x)
    else: 
        return l

fire = attackingMove(0,160,"Firethrower",18,"Fire")
print(fire.attack)
response = input("What type of action do you want to make? [actions, attackingMove, item]: ").lower()
print("You chose: " + response[0].upper() + response[1:])
theFirstOne = tryInt("How much health should this heal for the player? ")
theThirdOne = input("What's the name? ")
if response == "actions":
    theSecondOne = tryInt("How much damage to the opponent should this deal for the opponent? ")
    action = {"type" : "action", "name" : theThirdOne, "uses" : {"healing" : theFirstOne, "attack" : theSecondOne}}
elif response == "attackingmove":
    theSecondOne = tryInt("How much damage to the opponent should this deal for the opponent? ")
    unlocked = tryInt("At what level should this attack be unlocked at? ")
    typeAction = tryInt("What type is this action?" )
    action = {"type" : "attackingmove", "name" : theThirdOne, "uses" : {"healing" : theFirstOne, "attack" : theSecondOne}, "properties" : {"unlocked" : unlocked, "type" : typeAction}}
elif response == "item":
    desc = input("What description should this item have? ")
    attEffect = tryInt("How much should it affect the ATT damage? ")
    defEffect = tryInt("How much should it affect the defense? ")
    action = {"type" : "action", "name" : theThirdOne, "uses" : {"healing" : theFirstOne}, "properties" : {"desc" : desc, "attEffect" : attEffect, "defEffect" : defEffect}}
else:
    print("You misspelled your first response. Either write \"actions\", \"attackingMove\", or \"item\" for it. Run this again! ")

if response == "action" or "attackingmove" or "item":
    #figure out how to add variable action to the list in data(itsNotAJSONFile).py somehow
    print(action)