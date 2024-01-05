import random
global RandomNumberTOIJSDOIFJDOSF
class opponent():
    def createNewOpponent(self,d,n):
        self.d=d
        self.n=n
        RandomNumberTOIJSDOIFJDOSF = random.randint(1,60)*5
        #n is a random number from 0 to 300 deciding the opponents stats
        #d is the difficulty, best from -5 to 5, with 0 being around the player's stats
        return [((-10*RandomNumberTOIJSDOIFJDOSF/3)+2000+(100*d))/5//1*5,(320+RandomNumberTOIJSDOIFJDOSF)*(d/10+1)]
        #first item is the health, second is the attack
        #print(f"Opponent health and attack {createNewOpponent(-5,n)}")
#x = opponent.createNewOpponent(0)[0]
#y = opponent.createNewOpponent(0)[1]
#print(x,y)
class boss(opponent):
    def __init__(self,d,n):
        super().__init__(self,d,n)
        RandomNumberTOIJSDOIFJDOSF = random.randint(1,60)*3
        #n is a random number from 0 to 300 deciding the opponents stats
        #d is the difficulty, best from -5 to 5, with 0 being around the player's stats
        return [((-10*RandomNumberTOIJSDOIFJDOSF/3)+2000+(100*d))/5//1*5,(400+RandomNumberTOIJSDOIFJDOSF)*(d/10+1)]