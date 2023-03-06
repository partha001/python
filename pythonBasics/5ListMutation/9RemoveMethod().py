heroes = ["superman", "batman", "spiderman", "superman"]
heroes.remove("superman")
print(heroes) #['batman', 'spiderman', 'superman']


#however if try to delete a value that doesnt exist 
# in the list then it will throw ValueError
#heroes.remove("wonderWoman") #op: ValueError: list.remove(x): x not in list

#this can be handled as below 
if "wonderWoman" in heroes:   #this will make it failSafe
    heroes.remove("wonderWoman")