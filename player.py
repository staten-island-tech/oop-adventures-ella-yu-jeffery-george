class base_character:
    def __init__(self,name,numbers, inventory):
        self.name= name
        self.numbers=numbers
        self.inventory=inventory
    def set_add(self,health, attack):
        self.numbers.append(health)
        self.numbers.append(attack)
        print(f"""You have chosen the following stats: 
Health: {health} 
Attack: {attack}
""")    
     
    def hitty():
        def at(self,hits1, hits2):
            super().__init__(self,numbers)
            self.hits1=hits1
            self.hits2=hits2
            global user_health
            global user_attack
            global opponent_health
            global opponent_attack
            global hits1
            global hits2
            global HEH
            hits1=0
            hits2=0

            while opponent_health>0:
                hits1+=1
                opponent_health-=user_attack
                if opponent_health <= 0:
                    break 
            while HEH>0:
                hits2+=1
                HEH-=opponent_attack
                if HEH <=0:
                    break 

            if hits1<hits2:
                print("Battle results\nSuccess! Next round!")
            else:
                print("Battle results\nYou loose! Try again.")