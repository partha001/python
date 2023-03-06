mountains = ["mountEverest", "K2"]
print(mountains) #op: ['mountEverest', 'K2']

#the extend methods add the list passed a parameter to the list on which we are calling the method
#the list elements are added to the end of initial list 
mountains.extend(["Kanchenjunga","Makalu"])
print(mountains)  #['mountEverest', 'K2', 'Kanchenjunga', 'Makalu']


#however if we want a thid new list by added two lists they it can be done as shown below
cities = ["paris","kolkata"]
moreCities = ["mumbai","bangalore"]
totalCities = cities + moreCities
print(totalCities) #op: ['paris', 'kolkata', 'mumbai', 'bangalore']

#if we dont want a new list but add second list to the firstList then it 
#can be done as below without using append
cities = cities + moreCities
print(cities) #op: ['paris', 'kolkata', 'mumbai', 'bangalore']