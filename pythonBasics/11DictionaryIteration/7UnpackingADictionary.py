def heightToMeters(feet,inches):
    totalInches = (feet*12) + inches
    return totalInches

print(heightToMeters(5,11))


stats = {
    "feet": 5,
    "inches":11
}

#this below line will give error
#print(heightToMeters(stats)) #TypeError: heightToMeters() missing 1 required positional argument: 'inches'

print()
#it is to be noted that the keys and param names need to match exactly for the program to work
print(heightToMeters(**stats)) #op: 71


#now lets say we have a new key value in our dictionary
stats2 = {
    "feet": 5,
    "inches":11,
    "nonsense": True
}
#the below line will also fail since python doesnt see a corresponding parameter w.r.t nonsense
#print(heightToMeters(**stats2))  #op: TypeError: heightToMeters() got an unexpected keyword argument 'nonsense'
