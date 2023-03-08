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


