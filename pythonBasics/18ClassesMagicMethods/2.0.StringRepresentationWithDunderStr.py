## this is similar to toString() method in java


class Card():
    def __init__(self,rank, suit) :
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


c = Card("Ace","Spades")
#print(c) #op: <__main__.Card object at 0x0000027967F4EB50>    #without the __str__ custom implementation this will  be the output
## however if we choose to implement our own string re
print(c) #op: Ace of Spades
#another way of getting the same output is by calling the str() as this will internally call our custom defined __str__() magic method internally 
print(str(c)) #op: Ace of Spades




