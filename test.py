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