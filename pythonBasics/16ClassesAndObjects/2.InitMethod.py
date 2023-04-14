## the __init__ method is used whereever we instantiate a class
## this method corresponds to a constructor in java
# the __init__ doesnt have any return type. and should have atleast one argument i.e. self

class Guitar():
    def __init__(self):
        pass  #using the 'pass' keyword since python complains on having empty block


class Animal():
     def __init__(self):
         print("creating an object of animal class")


print(Animal())
##op: 
# creating an object of animal class
# <__main__.Animal object at 0x000001F9F678ED90>

## note how the init method is called automatically while the object creation