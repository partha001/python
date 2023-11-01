import collections

Book = collections.namedtuple("Book", ["title", "author"])
animal_farm = Book("Animal Farm", "George Orwell")
gatsby = Book(title = "The Great Gatsby", author = "F. Scott Fitzgerald")

# word = "dynasty"
# print(len(word))
# print(word.__len__())


## __len__ returns the length by default . however we if want to have our own implementation of 
## len then that can be done as below

## giving __len__ our own implementation 
## ie. whether to return number of books or number of librarians.
## here we have implemented __len__ to return the number of books
class Library():

    ##also note that since we have used *books so it can take any number of books
    def __init__(self, *books):
        self.books = books
        self.librarians = []

    def __len__(self):
        return len(self.books)

l1 = Library(animal_farm)
l2 = Library(animal_farm, gatsby)
print(len(l1)) ##op: 1
print(len(l2)) ##op: 2