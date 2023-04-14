## this program shows what happens when str is called but no __str__ implementation is present but __repr__ implementation is present
class Card():
    def __init__(self,rank, suit) :
        self.rank = rank
        self.suit = suit

    # def __str__(self):
    #     return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f'Card("{self.rank}","{self.suit}")'


c = Card("Ace","Spades")
#print(str(c)) #op: Ace of Spades  #initial output with __str__ uncommented
print(str(c)) #op: Card("Ace","Spades")  
##note since we have commented out the __str__ so internally makes call to __repr__ method since that is the one available
