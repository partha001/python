stats = {
    "name":"BBQChicken",
    "price": 199.99,
    "size":"ExtraLarge",
    "ingredients":["Chicken","Onions","BBQSauce"]
}

class Pizza():
    def __init__(self,stats):
        for key,value in stats.items():
            setattr(self,key,value)


bbq = Pizza(stats)

statsToDelete = ["size","diameter","spiceness","ingredients"]

print(bbq.size)

for stat in statsToDelete:
    if hasattr(bbq,stat):
        delattr(bbq,stat)  #note: calling delete for an attribute that doesnt exist will give error .so we have the check above

## now if we execute the below line the we'l get the below error since the attribute doesnt exist any more
#print(bbq.size)       #op: AttributeError: 'Pizza' object has no attribute 'size'   



