## now lets see how to handle the scenario when our higher order function returns a value. if we simply add return within our inner then the problem is that it 
## wont execute the code within inner() that we want to execute after the calling of the passed function . i.e. here print("It is a pleasure to meet you") will not get
## executed
def utilityFunc1(fn):
    def inner(*args,**kwargs):
        print("Nice to meet you")
        print(args)
        print(kwargs)
        return fn(*args, **kwargs)
        print("It is a pleasure to meet you")   
    return inner

@utilityFunc1
def addTwoNumbers1(a,b):
    return a+b

print(addTwoNumbers1(10,20))
# #OP:
# Nice to meet you
# (10, 20)
# {}
# 30




## this can be handled by holding the return value in a variable and then returning it later after our inner function has executed completely as shown below
def utilityFunc2(fn):
    def inner(*args,**kwargs):
        print("Nice to meet you")
        print(args)
        print(kwargs)
        result = fn(*args, **kwargs)
        print("It is a pleasure to meet you")   
        return result
    return inner

@utilityFunc2
def addTwoNumbers2(a,b):
    return a+b

print(addTwoNumbers2(10,20))
##op:
# Nice to meet you
# (10, 20)
# {}
# It is a pleasure to meet you  ##note this line is also invoked which was not happening earlier
# 30
