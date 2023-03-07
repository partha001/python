a = 3
b= a
a = 5
print(a) #op: 5
print(b) #op: 3
#this is because numbers are immutable

#however this is not the case for immutable types
a = [1,2,3]
b = a
a.append(4)
print(a)   #op: [1, 2, 3, 4]
print(b)    #op: [1, 2, 3, 4]
#this is because list is of types mutable. so the append done using
# a is also reflected in when we print b. since a and b point to the 
#same object


