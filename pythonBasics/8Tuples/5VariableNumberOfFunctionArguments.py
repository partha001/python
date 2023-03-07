#defining a function which takes variable number of arguments
#this is done using the asterix. it is also to be noted that 
# it is while defining the args we use the asterix and not while we are using it
#whenever we pass variable arguments like this then they are actually loaded to a tuple as shown below
def acceptStuff(*args):
    print(type(args))
    print(args)


acceptStuff(1) #this creates a tuple with 1 argument
acceptStuff(1,2,3) #this creates a tuple with 2 values
acceptStuff() #this will create an empty tuple when the function is executed



#example2:
def findMax(*numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(findMax(1))
findMax(findMax(1,3))


print()
#example3: it is to be noted that if we pass any additional argument then
#the unpacking happens mentioned in the previous program i.e. 4UnpackingUsingAsterix.py
def findMax2(nonsense, *numbers):
    print(nonsense)
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

#print(findMax2(6)) #in this case nonsense=6, numbers=() and will give index error while reading the firstIndex at line 33
print(findMax(findMax2(1,3)))  #in this case nonsense=1 numbers=(3) and return from function is 3



#it is also to be noted if we are passing variable number of arguments 
#it need not necessarily be a tuple . we can pass a list as well to the above functions