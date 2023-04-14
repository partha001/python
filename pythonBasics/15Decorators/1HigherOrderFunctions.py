#higher order function i.e function as argument
def one():
    return 1

print(type(one)) #op: <class 'function'>  
#note that the function itself is an object of the function class

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

#here calculate is higher order function
def calculate(func,a,b):
    return func(a,b)

print(calculate(add,2,3)) #op: 5
print(calculate(subtract,10,4)) #op: 6

