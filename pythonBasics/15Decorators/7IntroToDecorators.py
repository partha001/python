def beNice(fn):
    def inner():
        print("Nice to meet you")
        fn()
        print("It is a pleasure to meet you")
    
    return inner

def complexBusinessLogic():
    print("something complex")

#note that in the below line we are passing a function as input and getting a function as output
result = beNice(complexBusinessLogic)
result()
##op:
# Nice to meet you
# something complex
# It is a pleasure to meet you


print()

#another way of calling this is by directly calling it without capturing the return 
beNice(complexBusinessLogic)()
##op:
# Nice to meet you
# something complex
# It is a pleasure to meet you

print()

## however there is a special synax for this kind of scenario
#@beNice
def complexBusinessLogic2():
    print("something complex")

complexBusinessLogic2()
##op:
# Nice to meet you
# something complex
# It is a pleasure to meet you

#note if we comment out the annotated line then the output will be 
##op:
#something complex




