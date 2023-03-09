superheroes1 = {"superman" , "batman" , "spiderman"}
superheroes2 = {"thor", "batman"}

#now finding the intersection
print(superheroes1.intersection(superheroes2)) #op: {'batman'}

#there is anther way of finding intersection and this is by using the the & operator
print(superheroes1 & superheroes2) #op: {'batman'}



##lets see one more example with numbers
numbers = {1,2,3,4}
moreNumbers = {3.0, 4, 5}
print(numbers.intersection(moreNumbers)) #op: {3.0, 4}
print(numbers & moreNumbers) #op: {3.0, 4}
