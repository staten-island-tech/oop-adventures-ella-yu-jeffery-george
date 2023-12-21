import random
class picks():
    def drops(self, small,medium,large):
        self.small=small
        self.medium=medium
        self.large=large
        potions={"small": (200), "medium": (500), "large": (800)}
        
        random.choice(potions)
    drops(small, medium, large)