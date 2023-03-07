employee = ("Bob","Jhonson","Manager",50)

##as we have seen earlier the below line will fail since there are 4 vaules and we have supplied 3
#firstname , lastname , age = employee 
#op: ValueError: too many values to unpack (expected 3)

## this is where the asterix comes to rescue
firstname , lastname, *details = employee
print(firstname) #op: Bob
print(lastname) #op: Jhonson
print(details)  #op: ['Manager', 50]    #note that this is a list
print(type(details)) #op: <class 'list'>


## note how the last two variables are mapped and rest from left is loaded into the name list
*name , pos, age = employee
print(name) #op: ['Bob', 'Jhonson']
print(type(details)) #op: <class 'list'>
print(pos) #op: Manager
print(age)  #op: 50


## putting asterix in the middle
fname, *var, newAge = employee
print(name) #op: ['Bob', 'Jhonson']
print(type(details)) #op: <class 'list'>
print(pos) #op: Manager
print(age)  #op: 50



