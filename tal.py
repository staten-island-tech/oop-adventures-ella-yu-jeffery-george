class talents():
    import random
    turns=random.randint(3,5)
    
    def __init__(self,title,effect):
        self.title= title
        self.effect= effect
    def gain(self,turns):
        self.title.add(turns)
        print(f"You have chosen the following talent: {effect}.It will be active after every {turns} turns.")

