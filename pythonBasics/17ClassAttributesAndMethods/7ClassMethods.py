## classmethods are invoked on the class itself and not on the instances

class SushiPlatter():
    def __init__(self,salmon,tuna, shrimp, squid):
        self.salmon = salmon ##defining the attributes now
        self.tuna = tuna
        self.shrimp = shrimp
        self.squid = squid

    @classmethod
    def lunchSpecialA(cls):
        #return SushiPlatter() #this is also possible
        return cls(salmon=2, tuna=2, shrimp=2, squid=0)
    

    @classmethod
    def tunaLover(cls):
        return cls(salmon=0, tuna=10, shrimp=0, squid=1)

boris = SushiPlatter(salmon=8, tuna=4, shrimp=5, squid=10)
print(boris.salmon) #op: 8 

lunchEater = SushiPlatter.lunchSpecialA()
print(lunchEater.salmon) #op 2
print(lunchEater.squid) #op 0

tunaFan = SushiPlatter.tunaLover()
print(tunaFan.tuna) #op: 10



