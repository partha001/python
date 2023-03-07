heroes = ["batman","superman","spiderman"]

del heroes[1]
print(heroes) #'batman', 'spiderman']

#note that this can be done using the pop() also but the delete keyword provides an 
# advantange of deleting multiple elements using slicing techniques
del heroes[:]
print(heroes) #op:[]
