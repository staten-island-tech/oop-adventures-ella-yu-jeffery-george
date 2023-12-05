class talents():
    import random
    turns=random.randint(3,5)
    
    def __init__(self,title):
        self.title= title
    def gain(self,effect):
        self.title.append(effect)
        print(f"You have chosen the following talent: {effect}.It will be active after every {turns} turns.")

