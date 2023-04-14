import functools

#we know have help() function available to which we can pass any function or method and it will return the 
#documentation for the function.lets see how to define our own docstram

def addTwoNumbers1(a,b):
    "adds to numbers together and then returns the value"
    return a+b

help(addTwoNumbers1)
##op:
# addTwoNumbers1(a, b)
#     adds to numbers together and then returns the value   


## now in case of if the function is a higher order function then this docstram gets lost
def utilityFunc2(fn):
    def inner(*args,**kwargs):
        print("Nice to meet you")
        result = fn(*args, **kwargs)
        print("It is a pleasure to meet you")  
        return result 
    return inner

@utilityFunc2
def addTwoNumbers2(a,b):
    "adds to numbers together and then returns the value"
    return a+b
help(addTwoNumbers2)
##op:
#inner(*args, **kwargs)

### this is because now the addTwoNumbers2 is not executed alone rather from with the inner decorator function




## this losing of docStream of a higher order function can be dealt using the FuncTools which needs to be imported and used
def utilityFunc3(fn):
    @functools.wraps(fn) ##this is the line that does the magic
    def inner(*args,**kwargs):
        print("Nice to meet you")
        result = fn(*args, **kwargs)
        print("It is a pleasure to meet you")  
        return result 
    return inner

@utilityFunc3
def addTwoNumbers3(a,b):
    "adds to numbers together and then returns the value"
    return a+b
help(addTwoNumbers3)
#op
# Help on function addTwoNumbers3 in module __main__:      

# addTwoNumbers3(a, b)
#     adds to numbers together and then returns the value 