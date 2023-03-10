superheroes1 = {"superman" , "batman" , "spiderman"}
superheroes2 = {"thor", "batman"}

#now finding the union
print(superheroes1.union(superheroes2)) #op: {'spiderman', 'superman', 'batman', 'thor'}

#there is anther way of finding intersection and this is by using the the | operator
print(superheroes1 | superheroes2) #op: {'superman', 'thor', 'spiderman', 'batman'}



##lets see one more example with numbers
numbers = {1,2,3,4}
moreNumbers = {3.0, 4, 5}
print(numbers.union(moreNumbers)) #op: {1, 2, 3, 4, 5}
print(numbers | moreNumbers) #op: {1, 2, 3, 4, 5}