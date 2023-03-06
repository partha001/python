heroes = ["superman","batman","superman"]
moreHeroes = heroes.copy() 
#thus here a new list is created from the values of the intial list
#hence changing one will not affect the other

print(moreHeroes) #op: ['superman', 'batman', 'superman']
moreHeroes.remove("superman")
print(moreHeroes) #op: ['batman', 'superman']
print(heroes)  #op: ['superman', 'batman', 'superman']


print()


#however as discussed earlier we can also copy a list by using slicing
moreHeroes = heroes[:]
moreHeroes.remove("superman")
print(moreHeroes) #op: ['batman', 'superman']
print(heroes)  #op: ['superman', 'batman', 'superman']
