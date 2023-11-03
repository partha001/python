## defining the parent class
class Store():
    def __init__(self) -> None:
        self.owner = "Boris"

    def exclaim(self):
        return "lots of stuff to buy, come inside!"
    

##defining the subclass now
class CoffeeShop(Store):
    pass


starbucks = CoffeeShop()
## since its an object of the subclass to it automatically gets all properties and methods of the parent class
print(starbucks.owner) #op: Boris
print(starbucks.exclaim()) #op: lots of stuff to buy, come inside!

## now there can be multilevel inhertence . in such a case whenever we call a property or method
## python starts going from leaf to root starting with the child class and fetches the property of method of nearest parent
