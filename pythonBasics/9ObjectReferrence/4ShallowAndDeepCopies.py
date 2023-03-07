import copy

################## shallow copy ########################
# 1. a shallow copy creates a new list and then insert referrence of the objects present 
#   in the original , in the newly created list
# 2. a shallow copy is a good choice when the nested objects are immutable
#   like a list of numbers, Strings , booleans
# 3. there are three ways of creating shallow copy


a = [1,2,3]
#FirstWay:  creating a shallow copy
b = a[:]
print(a == b) #op: True
print(a is b) #op: False


#secondWay: is by using the copy() method available on the object
c = a.copy()
print(a == c) #op: True
print(a is c) #op: False

#thirdWay: is by using the copy module. for this we need to do import copy
d = copy.copy(a)
print(a == d) #op: True
print(a is d) #op: False

#thus in the above case b,c and d is a new list object however the elements within them refer to the same elements that are in a 
#this can also be verified as below 
numbers = [2,3,4]
a = [1, numbers, 5]
#now if we do any of the three
b = a[:]
b = a.copy()
b = copy.copy(a)
print( a==b) #True
print(a is b) #False
print(a[1] is b[1]) #True

a[1].append(100)
print(b)

#thus shallow-only copies the object referrence 

##########################  deep copy #####################
#however deep copy uses recursion to explore as many internal lists [or list within lists are present ] and copies the
#  values to create the new close and not just object element referrences

numbers = [2,3,4]
a = [1, numbers, 5]
#now making a deep copy 
b = copy.deepcopy(a)
print(a==b) #op: True   since == does value comparison
print(a is b) #op: False   since they are both different objects
print(a[1] is b[1]) #op: False

#also making change in a will not affect b .since we have made deep copy of a to b
a[1].append(100)
print(a) #op: [1, [2, 3, 4, 100], 5]
print(b) #op: [1, [2, 3, 4], 5]

#similarly if we make any changes to b list it will not reflected in a
b[1].append(200)
print(b) #op: [1, [2, 3, 4, 200], 5]
print(a) #op: [1, [2, 3, 4, 100], 5]







