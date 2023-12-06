from notes import Merchant
from hero import Hero
#Creates new instance of merchant, instansiation?
#all sle frefers to a specific instance ex Bob
Bob= Merchant("Bob", ["shells", "Sweater", "Jarvis", "Soul"])
Ann=Hero("Ann", 10, ["Burger"])
item=Bob.sell("Soul")
Ann.buy(item)
#Merchant.greeting()
#A staticmethod lets you do whatever without needing another class

