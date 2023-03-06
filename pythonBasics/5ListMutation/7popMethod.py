heros = ["superman","batman","spiderman"]
print(heros.pop()) #op: spiderman
print(heros) #op: ['superman', 'batman']

#we can also pass an index parameter to the pop() and remove item from a particular position
print(heros.pop(1)) #batman
print(heros) #['superman']

#however passing an index that doesnt exist will give IndexError
#print(heros.pop(100)) #op: IndexError

cities =[]
print(cities.pop())


