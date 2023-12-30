import random 
class opponent():
    n = random.randint(1,60)*5
    def createNewOpponent(self,d,n):
        self.d=d
        self.n=n
    #n is a random number from 0 to 300 deciding the opponents stats
    #d is the difficulty, best from -5 to 5, with 0 being around the player's stats
        return [((-10*n/3)+2000+(100*d))/5//1*5,(1+d/10)*n]
    #first item is the health, second is the attack
    #print(f"Opponent health and attack {createNewOpponent(-5,n)}")



