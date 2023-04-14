class Pokemon():
    def __init__(self,name,speciality,health=100):
        self.name = name
        self.speciality = speciality
        self.health = health

    def roar(self):
        print("Raaaar!")

    def describe(self):
        print(f"I am {self.name} . I am {self.speciality}  Pokemon!")

    def takeDamage(self,amount):
        self.health = self.health - amount


squirtle = Pokemon("Squirtle","Water")
charmander = Pokemon(name = "Charmander", speciality="Fire", health=110)

squirtle.roar() #op: Raaaar!
charmander.roar() #op: Raaaar!
squirtle.describe() #op: I am Squirtle . I am Water  Pokemon!
charmander.describe() #op: I am Charmander . I am Fire  Pokemon!

## changing some attribute value using object method
print(squirtle.health) #op: 100
squirtle.takeDamage(20)
print(squirtle.health) #op: 80


## we can also change the value of the object attributes directly 
print(charmander.health) #op: 110
charmander.health = 90
print(charmander.health) #op: 90