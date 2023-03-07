employee = ("Bob","Jhonson","Manager",50)

#now we can either unpack it as follows
# firstname = employee[0]
# lastname = employee[1]
# position = employee[2]
# age = employee[3]

#or a still better way of unpacking will be as follows
firstname, lastname, position, age = employee
print(firstname,lastname,position,age) #Bob Jhonson Manager 50


#this same way unpacking data can be applied to lists as well
# subject, verb, adjective = ["python","is","fun"]
# print(subject,verb,adjective)


## however if we are unpacking this way then we have to pass the same number of variable
# hence the below line will fail
#firstname , lastname , age = employee 
#op: ValueError: too many values to unpack (expected 3)


a = 5
b = 10
b, a = a,b
print(a,b) #10 5
# as we know to create tuple () is not necessary. and only a comma is enough 
# a,b is tuple  whose values are assigned to b,a which is again a tuple
# here again the immutable tuple is made up of variable which are mutable . hence we are able to change their values
