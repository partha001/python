heroes = ["superman","batman","superman"]
#using in clause we can check if the value is present or not
print("superman" in heroes) #op: True

#however if i want to get hold of the index where the value occurs then
print(heroes.index("superman")) #op: 0

#however if the value doesnt exist then it will return value error
#print(heroes.index("catwoman")) #op: ValueError: 'catwoman' is not in list

#thus to make the above code fail safe we can do 
if "catwoman" in heroes:
    print(heroes.index("catwoman"))


#we can optionally pass a second parameter to the index() i.e. the startPosition of the search
#this returns the index value relative to the start
print(heroes.index("superman",1)) #op: 2

#optionally we can also pass a thind parameter i.e the endIndex of the search .
# however it is start inclusive and end exclusive
print(heroes.index("superman",1,10)) #op: 2

#however here again if we do then we will get ValueError since its end exclusive and hence
#it will not find the value that we are looking for and hence throw valueError
print(heroes.index("superman",1,2)) #op: 2


