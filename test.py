import random
h=int(input("Enter the health of your choice: "))


travel=input("Which direction would you like to go? Left, right, up, down?: ").lower()
#randomize enemy spawn depending on what direction is chosen
while h > 0:    
    if travel==travel:
        fight=[1,2,3,4,5,6,7,8]
        steps=random.randint(1,10)
    if steps in fight:
        print("Enemy present")
        #import the opponent class
    else:
        print("Item found")