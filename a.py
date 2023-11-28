class character:
    def __init__(self,name):
        self.name= name
    def stats(self, base):
        print("Choose from the following stats:") 
    print("Choose one of the following base stats")
    print("""
        Stat A:
        health= 1000
        attack= 150

        Stat B:
        health= 2000
        attack= 50
        
        Stat C:
        health= 900
        attack= 300
        
        Stat  D:
        health= 1500
        attack= 120
        
        Stat E:
        health= 1800
        attack= 100
        """)
    choice=input("Enter here: ")
