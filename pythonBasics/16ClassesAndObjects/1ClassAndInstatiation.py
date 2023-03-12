#creating an empty class. now since python compiler complains if we have an empty block so we can make use of the 'pass' keyword to deal with this
class Person():
    pass

#creating an object of the class now
person1 = Person()

print(person1) #op: <__main__.Person object at 0x0000025FBC06E690>
# the above line will print the memory location at which the object is stored. something much similar to hashCode in java