#in python we dont need to declare datatypes for variable
#it intelligently know the datatype from the value
#thus the datatype of the variable can change during the course of program

value = "partha"
print(type(value)) #op: <class 'str'>
value = 10
print(type(value) ) #op: <class 'int'>




#multi-variable assignment
#naive way 
a = 5
b = 5
#in multi-variable assignment can be done as 
a = b = 5  
#i.e. here a is not pointing to b. rather a and b are two separate variables
b = 10
print(a) #op: 5  #i.e. a and b are not tied to each other


#another way of multi-variable assignment is 
a,b = 5,6  #i.e. here is a= 5 and b=6