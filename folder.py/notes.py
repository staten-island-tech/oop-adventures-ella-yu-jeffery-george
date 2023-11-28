class Merchant:
    def __init__(self,name, products):
        self.name=name
        self.products=products
    def sell(self,item):
        self.products.remove(item)
        print(f'Purchased {item}')
        print(self.products)
        return item
    @staticmethod
    def greeting():
        print("Welcome")  
