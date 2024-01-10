class attk:    
    def hitty():
        global user_health
        global user_attack
        global opponent_health
        global opponent_attack
        global count
        global hits1
        global hits2
        global HEH

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
        elif hits1>hits2:
            print("Battle results\nYou loose! Try again.")
        else:
            print("Battle results\nDraw!")
            k= input("Would you like to flee or fight?").lower()
            if k=="flee":
                m=["Flee successful", "Flee failed"]
                b=print(random.choice(m))
                if b=="Flee successful":
                    print("Continue with the movement.")
                else:
                    print("Fight occurs again")