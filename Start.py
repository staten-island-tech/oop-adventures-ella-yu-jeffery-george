import random
g=input("Would you like to start? Yes or No? ").capitalize()
if g=="No":
    print("Ok")
else:
    print("Build your character.")
    from player import base_character
    print("""
A:
Health= 1000
Attack= 150

B:
Health= 2000
Attack= 50
        
C:
Health= 900
Attack= 300
        
D:
Health= 1500
Attack= 120
        
""")
me=base_character("Bob", [])

go=input("Enter the stat set of your choice: ").capitalize()

me.set_add(go)

if go=="A":
    print("Health 100, attack 150")
elif go=="B":
    print("Health 2000, attack 50")
elif go=="C":
    print("Health 900, attack 300")
else:
    print("Health 1500, attack 200")
    
print("""
One: health increase by 150% of base, attack decrease 20%
Two: heath decreased by 20% of base, attack increase by 50%
Three: health increase by 200% of base, cannot attack next 2 turns
Four: health decrease by 50% attack increase by 130%
""")
skill_set=input("Choose a talent: ").lower
#put the chosen stats into a list that can be changed
print("Starting journey.")

travel=input("Which direction would you like to go? Left, right, up, down?").lower()
#randomize enemy spawn depending on what direction is chosen
counter=random.randint(1,11)
if counter==(1,7):
    print("Enemy present")
else:
    print("Item found")