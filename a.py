import random
global x
class start():
    def begin():
        go=input("Are you ready to start? ").capitalize()
        if go=='No':
            print("Do you wanna restart?")
        else:
            print("You may now begin. Your code will be printed below")
            za=['the fast monkey', 'the fat dog jumped', 'the lazy man sneezed', 'the dog meowed', 'no test too hard, no grade too low', 'no such thing as a bad quote']
            x=print(random.choice(za))
            g=input("").lower()
            
        if x==g:
            print("Congrats!")
        else:
            print("Try again.")  
    begin()