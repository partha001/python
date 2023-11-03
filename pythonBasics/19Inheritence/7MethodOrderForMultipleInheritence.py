class FrozenFood():
    def thaw(self, minutes):
        print(f"Thawing for {minutes} minutes")

    def store(self):
        print("Putting in the freezer!")

class Dessert():
    def add_weight(self):
        print("Putting on the pounds!")

    def store(self):
        print("Putting in the refrigerator!")

class IceCream(Dessert, FrozenFood):
    pass

ic = IceCream()
ic.add_weight()
ic.thaw(5)
ic.store() 
#op: Putting in the refrigerator!
# this is because while definining inheritence Dessert comes before FrozenFood .
# thus in a nutshell the order is preferrence is the order in which the inherited classes are declared

#mro stands for method resolution order
print(IceCream.mro())   #op: [<class '__main__.IceCream'>, <class '__main__.Dessert'>, <class '__main__.FrozenFood'>, <class 'object'>]