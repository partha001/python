#creating empty list using square brackets
emptyList1 = []
print(type(emptyList1)) #op: <class 'list'>

#creating list using list function . this is useful in convertin other datastructures to list
emptyList2 = list() 
print(type(emptyList2)) #op: <class 'list'>


#creating list from values
sodas = ["coke","pepsi","dr.pepper"]
print(len(sodas)) #op: 3


#however while creating list using list() we need to pass an iterable hence the below doesnt work
#fastFoods = list("potatoChips","coke")

#but the below works
fastFoods = list(["potatoChips","coke"])
print(len(fastFoods)) #p: 2



