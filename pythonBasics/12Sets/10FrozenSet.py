superheroes1 = frozenset({"superman" , "batman" , "spiderman"})

print(superheroes1)

#however if try to add or modify it will give error
#superheroes1.add("thor") #AttributeError: 'frozenset' object has no attribute 'add'


#just like set we can pass any iterable to the frozenset() function. ie. set, list, dictionary or another frozenset