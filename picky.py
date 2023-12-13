from player import base_character

small_potion=boost("Small Potion", "Restores 200 hp to user.")
medium_potion=boost("Medium Potion", "Restores 500 hp to user.")
large_potion=boost("Large Potion", "Restores 800 hp to user.")

potions=[]
potions.append(small_potion)
potions.append(medium_potion)
potions.append(large_potion)

print(potions)