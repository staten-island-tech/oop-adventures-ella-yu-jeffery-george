global map
import math
global count
count=0
map=["           ###,---,#","            ##| W |#   Turn 00","   #####    ##|ASD|#  /‾‾‾‾‾‾‾\ ","#######     ##'---'#","###         ########","##         ######  #","##   #       ###   #","#   ###        #  ##","#  #####   #      ##","#    ###  ##     ###","##    ######    ####","##   #######    ####","###########      ###"]
playerX=1
playerY=1

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
def otherRepeatedCode(theMap,a,b,x,y,msg):
    repeatedCodeLol("nah",x,y,theMap,1)
    theMap[6] = theMap[6] + a
    theMap[7] = theMap[7] + b
    return msg
def doTheMovarena(x,y,mapName,count,travel):
    mapName[y] = (mapName[y][:x]+"O"+mapName[y][(x+1):])
    count = count + 1
    #Below: depending on user input of direction, change the variables and print a new map
    if travel == "restart":
        print("Restarting...")
        return "restart"
    if travel == "w":
        if y == 0 or mapName[y-1][x] == "#":
            return otherRepeatedCode(map," ⌈ That direction ⌉"," ⌊  goes nowhere. ⌋",x,y,"noooo")
        else:
            repeatedCodeLol("y",x,y,mapName,-1)
    elif travel == "s":
        if y == 12 or mapName[y+1][x] == "#":
            return otherRepeatedCode(map," ⌈ That direction ⌉"," ⌊  goes nowhere. ⌋",x,y,"noooo")
        else:
            repeatedCodeLol("y",x,y,mapName,1)
    elif travel == "a":
        if x == 0 or mapName[y][x-1] == "#":
            return otherRepeatedCode(map," ⌈ That direction ⌉"," ⌊  goes nowhere. ⌋",x,y,"noooo")
        else:
            repeatedCodeLol("x",x,y,mapName,-1)
    elif travel == "d":
        if x == 19 or mapName[y][x+1] == "#":
            return otherRepeatedCode(map," ⌈ That direction ⌉"," ⌊  goes nowhere. ⌋",x,y,"noooo")
        else:
            repeatedCodeLol("x",x,y,mapName,1)
    else:
        repeatedCodeLol("nah",x,y,mapName,1)
        otherRepeatedCode(map," ⌈ wrong syntax ⌉"," ⌊      lol     ⌋",x,y,"canyoutype??")
    mapName[1] = mapName[1][:(len(mapName[1])-2)]+f"{(math.floor(count/10) - (10*math.floor(count/100)))}"+f"{count- (10*math.floor(count/10))}"
    for i in range(len(mapName)):
        print(mapName[i])

def move(x,y,mapName):
    # x and y are the axis, as x increases it goes right and as y increases it goes down
    for i in range(len(mapName)):
        print(mapName[i])
    while True:
        travel = input("Input the keys w,a,s,d, or input the word exit: ").lower()
        theMovarenaHasBeenDone = doTheMovarena(x,y,mapName,count,travel)
        if theMovarenaHasBeenDone == "exit":
            break
        if theMovarenaHasBeenDone != "noooo" and theMovarenaHasBeenDone != "canyoutype??":
            if travel == "w":
                y = y - 1
            elif travel == "s":
                y = y + 1
            elif travel == "a":
                x = x - 1
            elif travel == "d":
                x = x + 1
        else:
            for i in range(len(mapName)):
                print(mapName[i])
map = move(playerX,playerY,map)