#closure : A programming pattern in which a scope retain access to an enclosing 
#scope's names

def outer():
    candy = "snickers"

    def inner():
        return candy
    
    #return candy
    return inner

theFunc = outer()
print(theFunc())
