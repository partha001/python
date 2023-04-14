##example1
print(3.3 + 4.4) #op: 7.7
## the above line actually internally calls the magic method __add__() as shown below 
print(3.3.__add__(4.4)) #op: 7.7

##example2
print(len([1,2,3])) #op: 3
# the above line actaully call the __len__() magic method behind the scene
print([1,2,3].__len__()) #op: 3


##example3
print("h" in "hello") #op: True
# the above line internally calls the magic method __contains__()
print("hello".__contains__("h")) #op: True

#example4
print(["a","b","c"][2]) #op: c
# the above line internally calls magic method __getitem__
print(["a","b","c"].__getitem__(2)) #op: c
