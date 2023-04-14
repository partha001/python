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
print(bbq.size) #op: ExtraLarge
print(bbq.ingredients) #op: ['Chicken', 'Onions', 'BBQSauce']
##note how the setattr() functions is used to dynamically create attributes

##similary the get attributed is used to find the values of attibutes.
##it takes 3 params . 1:the object 2.attributename 3.fallback value if the attribute is not found
for attr in ["price","name","diameter","discounted"]:
    print(getattr(bbq,attr, "Unknown"))
#op : 
# 199.99
# BBQChicken
# Unknown
# Unknown