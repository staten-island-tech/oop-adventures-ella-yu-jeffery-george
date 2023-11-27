import math
import random
n = random.randint(0,138)*5
def createNewOpponent(n,d):
    #n is a random number from 0 to 690 deciding the opponents stats
    #d is the difficulty, best from -5 to 5, with 0 being around the player's stats
    return [n,math.floor(((-10*n/3)+2000+(100*d))/5)*5]
    #first item is the attack, second is the health

print(createNewOpponent(n,0))