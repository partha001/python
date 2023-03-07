flightPrices = {
    "kolkata" : 200,
    "delhi" : 300,
    "mumbai": 400
}


print(flightPrices["kolkata"]) #op: 200
#however if try to fetch value for a key that doesnt exist in the dictionary
#then it will give error 
#print(flightPrices["patna"]) #op: KeyError: 'patna'

#this can be handled as below by using the get method with a default value
# i.e if the key is not found then the get() will return the default value that we pass
print(flightPrices.get("patna",0)) #op: 0
print(flightPrices.get("patna"))   #op: None   ie none will be returned if we dont pass the default
print(flightPrices.get("kolkata")) 

## thus we can access the values either by using [] or by using get()
# we can choose from either depending upon how script we want our program to be 
# i.e whether to fail or not fail if the key is found or not 
# using [] will make the program fail if the key is not found while 
# using get() will make the program fail safe


