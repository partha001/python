superheroes1 = {"superman" , "batman" , "spiderman"}
superheroes2 = {"thor", "batman"}

#now finding the difference
print(superheroes1.symmetric_difference(superheroes2)) #op: {'superman', 'thor', 'spiderman'}

#there is anther way of finding symmetric difference and this is by using the the ^ operator
print(superheroes1 ^ superheroes2) #op: {'superman', 'spiderman', 'thor'}
