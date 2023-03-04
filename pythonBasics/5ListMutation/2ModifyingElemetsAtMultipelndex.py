coworkers = ["mimi","mishti","saikat","suvosree","sovan"]
print(coworkers[2:4])  #op: ['saikat', 'suvosree']

#changing values at multiple indices
coworkers[2:4] = ["subrata", "shibani"]
print(coworkers)  #op: ['mimi', 'mishti', 'subrata', 'shibani', 'sovan']

#now say we try n replace 2 values with 3 then all the values passed will be added
coworkers[2:4] = ["aniket", "soumya","tausif"]
print(coworkers) #op: ['mimi', 'mishti', 'aniket', 'soumya', 'tausif', 'sovan']
#note that though the slice size is 2 but we have passed 3 value to the length changes

#similarly passing less values comparing to slice size will reduce the length of the list
coworkers[2:4] = ["rahul"] 
print(coworkers) #op: ['mimi', 'mishti', 'rahul', 'tausif', 'sovan']

