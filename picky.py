import random
class picks():
    def drops(self, small,medium,large):
        self.small=small
        self.medium=medium
        self.large=large
        potions={"small": 200, "medium": 500, "large": 800}
        
        picked= random.choice(list(potions.keys()))
        return f"Item found: {picked} potion. Replenishes {potions[picked]} health when used."