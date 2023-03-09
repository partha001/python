disneyCharacters = {"mickyMouse","miniMouse","elsa"}

#adding element to the set
disneyCharacters.add("ariel")

#note that there is no guarantee of order
print(disneyCharacters) #op: {'miniMouse', 'elsa', 'ariel', 'mickyMouse'}


#if we try to add duplicates then it will not get added
disneyCharacters.add("mickyMouse") 
print(disneyCharacters) #op: {'mickyMouse', 'miniMouse', 'elsa', 'ariel'}


#the update method is used to add multiple values to the set 
disneyCharacters.update(["donaldDuck","miniMouse","goofy"])
print(disneyCharacters) #op: {'ariel', 'donaldDuck', 'miniMouse', 'elsa', 'goofy', 'mickyMouse'} 
#note that again duplicate character elements are automatically avoided

disneyCharacters.update(("simba","pluto"))
print(disneyCharacters) #op: {'donaldDuck', 'pluto', 'goofy', 'miniMouse', 'simba', 'elsa', 'ariel', 'mickyMouse'}

#just like set() function we can pass any iterable to the update() method i.e. a list , set, dictionary
#if we pass a dictionary then the keys will be added to the set