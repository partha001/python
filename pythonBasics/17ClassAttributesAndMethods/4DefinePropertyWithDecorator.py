class Currency():
    def __init__(self,dollars):
        self._cents = dollars * 100 #thus internally an storing dollars by defining an attribute cents

    
    @property
    def dollars(self): #note that here we defining an attribute dollars using the decorator @property
        return self._cents/100
    
    @dollars.setter
    def dollars(self,dollars): #this is the setter method
        if dollars >=0:
            self._cents = dollars * 100


backAccount = Currency(5000)
print(backAccount.dollars) #op: 5000


backAccount.dollars = 10000
print(backAccount.dollars) #op: 10000

backAccount.dollars = -2000
print(backAccount.dollars) #op: 10000
