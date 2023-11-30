g=input("Would you like to start? Yes or No? ").capitalize()
if g=="No":
    print("Ok")
else:
    print("Build your character.")
    from player import base_character
    print("""
Stat A:
Health= 1000
Attack= 150

Stat B:
Health= 2000
Attack= 50
        
Stat C:
Health= 900
Attack= 300
        
Stat  D:
Health= 1500
Attack= 120
        
Stat E:
Health= 1800
Attack= 100""")
me=base_character("Bob", [])
me.set_add(1000,150)
print(me)