#earlier we have seen ulitiy function like list(), dict(), int(), str() to create 
# corresponding objects. similary there is a set() function to create a set

print(set()) #op: set()
print(type(set())) #op: <class 'set'>


#creating set using values  from a list. note that it also takes care of the duplicates
print(set([1,2,3,3]))  #op: {1, 2, 3}


#creating a set from another set
print(set({1,2,3})) #op: {1, 2, 3}


#passing a dictionary to the set() function creates a set of keys of the dictionary elements
myDictionary = {"key1":100, "key2":200}
print(set(myDictionary)) #op: {'key2', 'key1'}