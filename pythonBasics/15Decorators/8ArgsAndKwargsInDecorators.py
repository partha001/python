## scenario1
# def beNice1(fn):
#     def inner():
#         print("Nice to meet you")
#         fn()
#         print("It is a pleasure to meet you")   
#     return inner

# @beNice1
# def complexBusinessLogic1(stakeholder):
#     print("something complex for {stakeholder}")
# complexBusinessLogic1("partha") #op TypeError: beNice1.<locals>.inner() takes 0 positional arguments but 1 was given

## problem statement: the above code gives Error because when it tries to execute the complexBusinessLogic1() via the inner it doesnt have the argument
## available to it. for this we can do 
## def beNice1(fn,stakeholder):
##     def inner(stakeholder):
##         print("Nice to meet you")
##         fn(stakeholder)
## however the decorator function is used to hold cross cutting concerns and thus can used with another function say complexBusinessLogic2 which may have different
## set of arguments. thus we want our inner to be as generic as possible so that it called without issue from any function.
## this is where args and kwargs comes to rescue. using args and kwars we can pass variable number of arguments and keyvalue pairs making our inner generic decorator function



def beNice1(fn):
    def inner(*args,**kwargs):
        print("Nice to meet you")
        print(args)
        print(kwargs)
        #fn(*args,**kwargs)
        print("It is a pleasure to meet you")   
    return inner

@beNice1
def complexBusinessLogic1(stakeholder):
    print("something complex for {stakeholder}")
complexBusinessLogic1(1,2,3,stakeholder="partha",) #op TypeError: beNice1.<locals>.inner() takes 0 positional arguments but 1 was given
# #ouput
# Nice to meet you
# (1, 2, 3)
# {'stakeholder': 'partha'}
# It is a pleasure to meet you



# ## now lets see wat we need to do to make the function call from within inner
def beNice2(fn):
    def inner(*args,**kwargs):
        print("Nice to meet you")
        print(args)
        print(kwargs)
        fn(*args, **kwargs) #here it basically destructures the arguments and passes them to the inner
        print("It is a pleasure to meet you")   
    return inner

@beNice2
def complexBusinessLogic2(stakeholder,position):
    print(f"something complex for {position} {stakeholder}")

## we can now make the calls as any of the below the differenece is how they are loaded into args and kwargs

## the below call works fine and arguments are loaded as  args=('partha', 'ceo') and kwargs = {}
complexBusinessLogic2("partha","ceo")  ##this will be loaded onto the args and passed the nested function call

# # the below call works fine and arguments are loaded as  args=() and kwargs = {'stakeholder': 'partha', 'position': 'ceo'}
complexBusinessLogic2(stakeholder="partha", position="ceo") ##here the argumnet is loaded onto a dictionary and then passed into the nested function call

# #the below call works fine and arguments are loaded as  args=('partha',) and kwargs = {'position': 'ceo'}
complexBusinessLogic2("partha", position="ceo") ##here the argumnet is loaded onto a dictionary and then passed into the nested function call



