numbers = [1,2,3,4]

#now lets say we want a list of cubes of these elements

#solution1 : naive way
result1 = []
for number in numbers:
    result1.append(number **3)
print(result1) #[1, 8, 27, 64]

#solution2: using list comprehension
print([number ** 3 for number in numbers]) #op: [1, 8, 27, 64]


#solution3: using map. a map takes 2 arguments 
# i. function that will be applied to each element
# ii an iterable on whose elements the function will be applied.
# this works as below 

def getCube(item):
    return item**3
print(list(map(getCube, numbers)))#op: [1, 8, 27, 64]
#it is to be noted that a map return a map object . so we have list() above
print(map(getCube, numbers)) #op: <map object at 0x000001D03618B9D0>
print(type(map(getCube, numbers))) #op: <class 'map'>


#we can also pass any built in function to the map function as shown below
animals = ["tiger","lion","elephant"]
print(list(map(len, animals))) #[5, 4, 8]






