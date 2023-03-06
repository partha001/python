#this will give all the methods that are available on the list object
#print(dir([]))
## op:
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
##

#the methods names with double_underscore are called dunder-methods
#these methods are like system methods which are used by python compliler
#and the method which doesnt have _ are exposed to us. 
#so wheneven we call any method that is exposed to us it underlyingly calls
#a dunder method

#print(dir("pasta"))
print(len("pasta")) #op: 5
#this len is a function and it under the hood calls the below method on the object
print("pasta".__len__()) #op: 5