names = {"partha","saikat","mimi","suvosree"}

print(names) #op: {'suvosree', 'saikat', 'partha', 'mimi'}
names.remove("suvosree")
print(names) #op: {'saikat', 'partha', 'mimi'}


#however if we pass a key that doesnt exist in the set then the remove will fail
#names.remove("aniket") #op: KeyError: 'aniket'


#this is where the discard() method comes handy. it also removes an element from set.
#  Howerver the discard() doesnt fail if the element is not found
names.discard("sayan")
print(names) #op: {'saikat', 'partha', 'mimi'}

