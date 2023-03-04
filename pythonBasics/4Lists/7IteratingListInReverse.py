theSimpons = ["Homer","Marge", "Bart","Lisa","Maggie"]

#while slicing we have already explore how to reverse a list using the last intervalParamter
for element in theSimpons[::-1]:
    print(element)


print("")

#however there is a reversed()  to which we can pass a list get a new list with the elements reversed
for element in reversed(theSimpons):
    print(element)

#also note the return type of the reversed() function 
print(type(reversed(theSimpons))) #op: <class 'list_reverseiterator'>