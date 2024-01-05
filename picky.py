import random
item= random.choice(list(potions.keys()))
    return f"Item found: {item} potion. Replenishes {potions[item]} health"
    
def use_potions(user_health):
    hpp=input("Which potion would you like to use? small, medium or large?").lower()
    if hpp=="small":
        user_health+200
    elif hpp=="medium":
        user_health+500
    elif hpp==("large"):
        user_health+800

    return user_health
        picked= random.choice(list(potions.keys()))
        return f"Item found: {picked} potion. Replenishes {potions[picked]} health when used."
