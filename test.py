
def sip():
    user_health=200
    hpp=input("Which potion would you like to use? small, medium or large?").lower()
    if hpp=="small":
        user_health+=200
    elif hpp=="medium":
        user_health+=500
    elif hpp==("large"):
        user_health+=800

    print(user_health) 
sip()