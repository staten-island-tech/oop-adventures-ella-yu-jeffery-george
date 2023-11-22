import math
import random
n = random.randint(0,6900)/10
def createNewOpponent(n):
    # n is a number from 0 to 100
    return [n,(-10*n/3)+2300]

print(createNewOpponent(n))