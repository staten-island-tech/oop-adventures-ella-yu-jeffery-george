global map
import math
global count
map=["           ###,---,#","            ##| W |#   Turn 00","   #####    ##|ASD|#  /‾‾‾‾‾‾‾\ ","#######     ##'---'#","###         ########","##         ######  #","##   #       ###   #","#   ###        #  ##","#  #####   #      ##","#    ###  ##     ###","##    ######    ####","##   #######    ####","###########      ###"]
map[10] == map[10] + "OIDFSJOJDFOSIJOSDIFODSJFODSF"
playerX=1
playerY=1
def move(x,y,mapName):
    count = 0
    # x and y are the axis, as x increases it goes right and as y increases it goes down
    def repeatedCodeLol(xORy,x,y,theMap,plusOrMinusOne):
        theMap[6] = theMap[6][:len(theMap[0])]
        theMap[7] = theMap[7][:len(theMap[0])]
        if xORy == "y":
            theMap[y] = (theMap[y][:x]+"|"+theMap[y][(x+1):])
            theMap[y+plusOrMinusOne] = (theMap[y+plusOrMinusOne][:x]+"O"+theMap[y+plusOrMinusOne][(x+1):])
        elif xORy == "x":
            theMap[y] = (theMap[y][:x]+"-"+theMap[y][(x+1):])
            theMap[y] = (theMap[y][:(x+plusOrMinusOne)]+"O"+theMap[y][(x+1+plusOrMinusOne):])
        elif xORy != "nah":
            print("-----------\nCheck the code. The xORy variable is wrong.\n=======")
    def otherRepeatedCode(theMap,a,b):
        repeatedCodeLol("nah",x,y,mapName,1)
        theMap[6] = theMap[6] + a
        theMap[7] = theMap[7] + b
    if mapName[y][x] == " ":
        mapName[y] = (mapName[y][:x]+"O"+mapName[y][(x+1):])
        for i in range(len(mapName)):
            print(mapName[i])
        while True:
            travel = input("Input the keys w,a,s,d, or input the word exit: ").lower()
            count = count + 1
            #Below: depending on user input of direction, change the variables and print a new map
            if travel == "exit":
                print("Bye.")
                break
            elif travel == "w":
                if y == 0 or mapName[y-1][x] == "#":
                    otherRepeatedCode(map," ⌈ That direction ⌉"," ⌊  goes nowhere. ⌋")
                else:
                    repeatedCodeLol("y",x,y,mapName,-1)
                    y = y-1
            elif travel == "s":
                if y == 12 or mapName[y+1][x] == "#":
                    otherRepeatedCode(map," ⌈ That direction ⌉"," ⌊  goes nowhere. ⌋")
                else:
                    repeatedCodeLol("y",x,y,mapName,1)
                    y = y + 1
            elif travel == "a":
                if x == 0 or mapName[y][x-1] == "#":
                    otherRepeatedCode(map," ⌈ That direction ⌉"," ⌊  goes nowhere. ⌋")
                else:
                    repeatedCodeLol("x",x,y,mapName,-1)
                    x = x - 1
            elif travel == "d":
                if x == 19 or mapName[y][x+1] == "#":
                    otherRepeatedCode(map," ⌈ That direction ⌉"," ⌊  goes nowhere. ⌋")
                    count = count - 1
                else:
                    repeatedCodeLol("x",x,y,mapName,1)
                    x = x + 1
            else:
                repeatedCodeLol("nah",x,y,mapName,1)
                otherRepeatedCode(map," ⌈ wrong syntax ⌉"," ⌊      lol     ⌋")
            mapName[1] = mapName[1][:(len(mapName[1])-2)]+f"{(math.floor(count/10) - (10*math.floor(count/100)))}"+f"{count- (10*math.floor(count/10))}"
            for i in range(len(mapName)):
                print(mapName[i])
    else:
        print("That space is filled.")
    return mapName
map = move(playerX,playerY,map)