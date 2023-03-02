# optionally we can mention the type of params as shown below
#example1: function with no return
def multiply(word:str, times:int) -> str:
    return word*times


print(multiply("***",2))

#note that this doesnt do type checking.i.e. we can still continue to pass any type
#thus this is mostly for documentation purposes
print(multiply(10,2))