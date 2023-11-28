class talents():
    def __init__(self,title):
        self.title= title
    def more(self,effect,turns):
        self.effect=effect
        self.turns=turns
        print(self.effect, self.turns)
        