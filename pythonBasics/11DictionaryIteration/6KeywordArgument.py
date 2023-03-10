#passing keyword arguments to functions
def length(word):
    return len(word)

print(length("hello"))
print(length(word="hello"))

#however if we pass mention the argument name explicitly while calling the function
#then we also have to make sure that we are passing the right argumentName else python will throw error
#print(length(something="hello")) #op: TypeError: length() got an unexpected keyword argument 'something'

#also we have to pass the right number of arguments else we will get the below error
#print(length(word="hello", something="goodbye")) #TypeError: length() got an unexpected keyword argument 'something'

##here the double asterix i.e ** is used to tell python to load the arguments into a dictionary
def collectKeywordArgs(**kwargs):
    print(kwargs) #op: {'a': 2, 'b': 3, 'c': 4}
    print(type(kwargs)) #op:  #op: <class 'dict'>
    for key,value in kwargs.items():
        print(f"key is {key} and the value is {value}")
        #op
        # key is a and the value is 2
        # key is b and the value is 3
        # key is c and the value is 4

collectKeywordArgs(a=2,b=3,c=4)



#however using a single asterix will make the arguments load into a tuple as we have seen earlier
def argsAndKeyword(a,b,*args):
    print(args) #op: (3, 4, 5)
    print(type(args)) #op: <class 'tuple'>

argsAndKeyword(1,2,3,4,5)


## it is also to be kept in mind that if we want to pass both 
# i.e kwargs and args i.e a dictionary and a tuples then the 
# tuple should always come before the dictionary
def argsTupleAndDictionary(a,b ,*args,**kwargs):
    print(f"a is {a} and b is {b}")
    print(args)
    print(kwargs)

print()
## in this case python loads the first two into params into variables and 
# the remaining into tuple since we have not passed any name for the params
argsTupleAndDictionary(1,2,3,4,5,6,7)
#op
# a is 1 and b is 2
# (3, 4, 5, 6, 7)
# {}

print()
argsTupleAndDictionary(1,2,3,4, first=100, last=200)
#op
# a is 1 and b is 2
# (3, 4)
# {'first': 100, 'last': 200}





