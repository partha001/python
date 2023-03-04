text = "what a lovely day"
print(text.startswith("what")) #prints True
#overriden forms allow us to pass a start index from where we want to search
print(text.startswith("what",1)) #prints False
#another overridden form is to pass both startIndex and endIndex
print(text.startswith("day",5,12)) #prints false


#simiarly the endswith() method works 