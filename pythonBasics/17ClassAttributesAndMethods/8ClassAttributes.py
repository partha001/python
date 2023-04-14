#class level attributes are used to information that we want to store at the class level.
#as for example a counter to keep track of how many instances have been created out of a class.
class Counter():
    count =0

    def __init__(self):
        Counter.count +=1  # note that we havent done count++ this wont work . since count is a class level attribute

    ##again to manipulate the class level attribute we can make use of class methods as below 
    @classmethod
    def createTwo(cls):
        twoCounters = [cls(), cls()] #creating two objects
        print(f"new number of counter objects created: {cls.count}")
        return twoCounters


print(Counter.count) #op: 0
c1 = Counter()
print(Counter.count) #op: 1

c2, c3 = Counter.createTwo()
print(Counter.count) #op: 3

## unlike java the class level attributes are shared accross instances
print(c1.count) #op: 3
print(c2.count) #op: 3
print(c3.count) #op: 3