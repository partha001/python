## usecase1:
x = 10
def changeStuff():
    x=15

print(x) #op: 10
changeStuff()
print(x) #op: 10
#here the x within the function is a different variable from the x declared 
# globally and its scope is restricted only within the function. that is why 
# the setting its values does have any effect on the x which is declared locally . 


#usecase2:
#however if there is a requirement to refer to the x which is available at the global
#level from within the function then that is achived using the global keyword
#as shown below 
a = 20
def changeStuff2():
    global a
    a=25

print(a) #op: 20
changeStuff2()
print(a) #op: 25
#note that here we are accessing the global variable from within the function 
#and also modifiying it. this is the use of the global keyword


#use case3
#one can also not declare the global variable at the global scope at all rather create it 
#within the function but this is highly discouraged
def changeStuff3():
    global m
    m= 30
#print(m)
changeStuff3()
print(m) #op: 30
##howeever this block of code will fail if we uncomment the print before the changeStuff3() call 
#give nameError. because the m is created and registed at the global scope only after the call of changeStuff3()


##thus is a nutshell overwriting or creating a global variable within some local scope of some function is highly discouraged

