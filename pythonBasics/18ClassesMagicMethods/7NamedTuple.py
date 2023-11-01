import collections

## declaring namedTuple
# collections.namedtuple("Book", ["title", "author"])
##another way of writing a namedTuple is as shown below where the properties are space separated strings
# collections.namedtuple("Book","title author")

Book = collections.namedtuple("Book", ["title", "author"])
## henceforth book can be assumed as a class with the attributes title and author

animal_farm = Book("Animal Farm", "George Orwell")
## additionally we can also pass keyword arguments as shown below 
gatsby = Book(title="The great gatsby", author="F.Scott Fitzgerald")
## advantange of keyword arguments is that the order of the arguments dont matter if we use keyword arguments

## tuple like behavior . i.e. accessing data using index
print(animal_farm[0])
## op: Animal Farm
print(gatsby[1])
## op: F.Scott Fitzgerald

## class like behavior . i.e accessing data using property names
print(animal_farm.title)
## op: Animal Farm
print(gatsby.author)
## op: F.Scott Fitzgerald



