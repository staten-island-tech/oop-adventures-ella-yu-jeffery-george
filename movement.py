global map
map=['#####  ##',"#####  ##","###    ##","##     ##","##   ####","##       ","###      ","#######  "]
def printMap(mapName):
    for i in range(len(mapName)):
        print(mapName[i])
global playerX
global playerY
playerX=5
playerY=0
def move(x,y,mapName):
    # x and y are the axis, as x increases it goes right and as y increases it goes down
    if mapName[y][x] == " ":
        b = mapName[y]
        mapName[y] = (b[:x]+"O"+b[(x+1):])
        printMap(mapName)
        def repeatedCodeLol(xORy,x,y,theMap,plusOrMinusOne):
            theMap[y] = (theMap[y][:x]+" "+theMap[y][(x+1):])
            if xORy == "y":
                theMap[y+plusOrMinusOne] = (theMap[y+plusOrMinusOne][:x]+"O"+theMap[y+plusOrMinusOne][(x+1):])
            elif xORy == "x":
                theMap[y] = (theMap[y][:(x+plusOrMinusOne)]+"O"+theMap[y][(x+1+plusOrMinusOne):])
            else:
                print("-----------\nCheck the code. The xORy variable is wrong.\n=======")
        while True:
            direction = input("Input the keys w,a,s,d, or input the word exit: ")
            if direction == "exit":
                break
            elif direction == "w":
                if y == 0 or mapName[y-1][x] == "#":
                    print("That direction goes nowhere.")
                else:
                    repeatedCodeLol("y",x,y,mapName,-1)
                    y = y-1
            elif direction == "s":
                if y == 7 or mapName[y+1][x] == "#":
                    print("That direction goes nowhere.")
                else:
                    repeatedCodeLol("y",x,y,mapName,1)
                    y = y + 1
            elif direction == "a":
                if x == 0 or mapName[y][x-1] == "#":
                    print("That direction goes nowhere.")
                else:
                    repeatedCodeLol("x",x,y,mapName,-1)
                    x = x - 1
            elif direction == "d":
                if x == 8 or mapName[y][x+1] == "#":
                    print("That direction goes nowhere.")
                else:
                    repeatedCodeLol("x",x,y,mapName,1)
                    x = x + 1
            else:
                print("wrong syntax lol")
            printMap(mapName)
    else:
        print("That space is filled.")
    return mapName
map = move(playerX,playerY,map)
