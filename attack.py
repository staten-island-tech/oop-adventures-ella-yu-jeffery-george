class attk():
    def hitty(self,hits1,hits2):
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
