countries = ["india","usa","canada"]
print(countries) #op: ['india', 'usa', 'canada']
print(len(countries)) #op: 3

countries.append("france")
print(countries) #op: ['india', 'usa', 'canada', 'france']
print(len(countries)) #op: 4


#also note that the append method does return anything i.e 
#it has a return type of None . thus we write 
countries = countries.append("brazil")
print(countries)