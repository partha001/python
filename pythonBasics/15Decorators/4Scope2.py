#LEGB
def outer():
    x = 10

    def inner():
        x=5
        return x
    
    return inner()

print(outer()) #op 5  . LEGB rule . ie. python will always use the values that is nearest to current scope.
#however if comment line5 then the above line will print 10 .
#ie. the prirority order is LEGB: i.e. Local > Enclosing > Global > BuiltIn
# this is the order in which python tries to resolve the varible values that we use in our program  