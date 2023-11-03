class Nonsense():
    def __init__(self):
        self.__some_attribute = "Hello"

    def __some_method(self):
        print("This is coming from some_method!")

class SpecialNonsense(Nonsense):
    pass

n = Nonsense()
sn = SpecialNonsense()

## the below will not work
# print(n.__some_attribute)
# print(n.some_attribute)
# print(sn.__some_attribute)
# print(sn.some_attribute)
# n.__some_method()
# sn.__some_method()


## the double underscore attributes and method names are mangled in a special way 
# and can be accessed in the below way. i.e. <object>._<ClassName>__<attribute/methodName>
print(n._Nonsense__some_attribute)
print(sn._Nonsense__some_attribute)
n._Nonsense__some_method()
sn._Nonsense__some_method()