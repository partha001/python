## this program shows that happens when we call str or repr without defining __str__ or __repr__
class Card():
    def __init__(self,rank, suit) :
        self.rank = rank
        self.suit = suit

    # def __str__(self):
    #     return f"{self.rank} of {self.suit}"
    
    # def __repr__(self):
    #     return f'Card("{self.rank}","{self.suit}")'


c = Card("Ace","Spades")
print(str(c)) #op: <__main__.Card object at 0x00000223296DEAD0>
print(repr(c)) #op: <__main__.Card object at 0x00000223296DEAD0>
