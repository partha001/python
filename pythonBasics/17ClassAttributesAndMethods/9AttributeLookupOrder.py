class Example():
    data = "classAttribute!"

e1 = Example()
e2 = Example()
print(e1.data) #op: classAttribute!

e1.data = "InstanceAttribute!"
print(e1.data) #op: InstanceAttribute!
print(e2.data) #op: classAttribute!

#now removing the instance attribute
del e1.data
print(e1.data) #op: classAttribute!
#note that after removal of the instance attribute its starts printing the class attribute since python reads attributes in that priority
## i.e whenever an attribute is referenced by an object 
##	Python will look for an instance attribute first 
##  If its not able to find the attribute at the instance level then it will look for a class attribute

## however the below line will give the below error since the attribute nonsense exists neither at the instanceLevel nor at the class level
#print(e1.nonsense) #AttributeError: 'Example' object has no attribute 'nonsense'