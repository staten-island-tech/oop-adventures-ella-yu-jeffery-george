class talents():
    def __init__(self,title):
        self.title= title

    def gain(self,effect, turns,user_health, user_attack):
        self.title.append(effect)
        self.title.append(turns)
        
        ho=input("Would you like to use your skill? Yes or no?").lower()
        if ho == "yes":
            if "Health increases by 50%" in effect:
                user_health *=1.5
            elif "Heath decreased by 20%" in effect:
                user_health *=0.8
                user_attack *=1.5
            elif "Health increase by 100%" in effect:
                user_health *=2
            elif "Health decreased 50%" in effect:
                user_health *=0.5
                user_attack *=1.3
            
        return user_health, user_attack, ho