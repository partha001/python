class Guitar():
    def __init__(self) :
        pass

acoustic = Guitar()
electric = Guitar()

##now we can set attributes manually ourselves
acoustic.wood = "mahogany"
acoustic.strings = 6
acoustic.year = 1990

electric.nickname = "Sound viking 300"
print(acoustic.wood)  ##op: mahogany
print(electric.nickname) ##op: Sound viking 300


## though this works but there is no consistency in the attributes. for having consitency we can 
## add these attributes to the class itself rather than adding them manually on the objects



