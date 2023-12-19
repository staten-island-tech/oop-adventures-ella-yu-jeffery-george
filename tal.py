class talents():

    def __init__(self,title):
        self.title= title
    def gain(self,effect, turns):
        self.title.append(effect)
        self.title.append(turns)
        print(f"You have chosen the following talent: {effect}. It will be active after every {turns} turns.")

