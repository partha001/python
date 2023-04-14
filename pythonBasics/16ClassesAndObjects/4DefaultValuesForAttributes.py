class Book():
    def __init__(self,title, author, price = 14.99):
        self.title = title
        self.author = author
        self.price = price


animalFarm = Book("animalfarm","georgeOrwell",19.99)
gatsby = Book("TheGreatGatsby","F.Scott Fitzgerals")

print(animalFarm.price) #op: 19.99
print(gatsby.price) #op: 14.99  
## note that this shows the default price since we havent passed any price ourselves while creating the object