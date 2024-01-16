class talents():
    global turns
    def __init__(self,me):
        self.title= []
        self.me=me

    def creating(self, turns,user_health,user_attack):
        kits= {"1": "Health increase by 50% of base attack decrease 20%",
        "2": "Heath decreased by 20% of base, attack increase by 50%", 
        "3": "Health increase by 100% of base health", 
        "4": "Health decrease by 50% attack increase by 130%"}

        print(kits)
        skill_set=input("Choose a skill number:").lower()   

        if skill_set in kits:
            user_health, user_attack = self.gain(kits[skill_set], turns, user_health, user_attack)
        else:
            print("Kit number not found.")
        return user_health, user_attack
        
    def gain(self,effect, turns,user_health, user_attack):
            self.title.append(effect)
            self.title.append(turns)

            if "Health increase by 50%" in effect:
                user_health *= 1.5
            elif "Heath decreased by 20%" in effect:
                user_health *= 0.8
                user_attack *= 1.5
            elif "Health increase by 100%" in effect:
                user_health *= 2
            elif "Health decrease by 50%" in effect:
                user_health *= 0.5
                user_attack *= 1.3
                
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

            print(f"Stats updated:\nHealth: {user_health}\nAttack: {user_attack}")

            return user_health, user_attack