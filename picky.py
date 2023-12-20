class picks():
    import random
    def pot():    
        mini=("Mini Potion: Restores 150 hp to user.")
        small=("Small Potion: Restores 200 hp to user.")
        standard=("Standard Potion: Restores 350 hp to user")
        medium=("Medium Potion: Restores 500 hp to user.")
        large=("Large Potion: Restores 650 hp to user.")

        potions=[]
        potions.append(mini)
        potions.append(small)
        potions.append(standard)
        potions.append(medium)
        potions.append(large)

        chance= random.choice(potions)
        print(f"Item found! {chance}")
