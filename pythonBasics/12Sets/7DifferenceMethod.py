superheroes1 = {"superman" , "batman" , "spiderman"}
superheroes2 = {"thor", "batman"}

#now finding the difference
print(superheroes1.difference(superheroes2)) #op: {'spiderman', 'superman'}

#there is anther way of finding difference and this is by using the the | operator
print(superheroes1 - superheroes2) #op: {'spiderman', 'superman'}



##lets see one more example with numbers
numbers = {1,2,3,4}
moreNumbers = {3.0, 4, 5}
print(numbers.difference(moreNumbers)) #op: {1, 2}
print(numbers - moreNumbers) #op: {1, 2}