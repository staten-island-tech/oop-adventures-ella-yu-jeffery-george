import random
count=22
class boss():
    def __init__(self,d,n):
        self.d=d
        self.n=n
        RandomNumberTOIJSDOIFJDOSF = random.randint(1,60)*3
        #n is a random number from 0 to 300 deciding the opponents stats
        #d is the difficulty, best from -5 to 5, with 0 being around the player's stats
        self.stats= [((-10*RandomNumberTOIJSDOIFJDOSF/3)+2000+(100*d))/5//1*5,(400+RandomNumberTOIJSDOIFJDOSF)*(d/10+1)]
        if count==22:
            print("Boss Present")
            final=boss(-3,n)
            boss_stats=final.stats
            boss_health=boss_stats[0]
            boss_attack=boss_stats[1]
            
            print(f"Boss stats are the following:\nHealth: {boss_health}\nAttack: {boss_attack}")
UH= 2000
UA=200
OA=150
OH=3000
stop = 0
counter1=0
counter2=0

while OH>stop:
    UH-=OA
    counter1+=1
    if UH==stop:
        print("Reached 00")
        break

while UH>stop:
    OH-=UA
    counter2+=1
    if OH==stop:
        print("Reached 0")
        break

if counter1<counter2:
    print("Opponent wins")
elif counter1>counter2:
    print("User wins")
else:
    ("monkey scratch")
