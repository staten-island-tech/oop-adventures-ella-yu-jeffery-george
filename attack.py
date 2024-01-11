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

        if hits1<=hits2:
            print("Battle results\nSuccess! Next round!")
        else:
            print("Battle results\nYou loose! Try again.")
            map[playerY] = (map[playerY][:playerX]+" "+map[playerY][(playerX+1):])
            if travel == "w":
                    playerY = playerY + 1
            elif travel == "s":
                    playerY = playerY - 1
            elif travel == "a":
                    playerX = playerX + 1
            elif travel == "d":
                    playerX = playerX - 1