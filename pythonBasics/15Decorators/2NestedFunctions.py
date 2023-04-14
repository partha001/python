#gallons to cups
    #1 gallon = 4 cups
    #1 quart =2 pints
    #1 pint = 2 cups

def convertGallonsToCups(gallons):

    def gallonsToQuars(gallons):
        print(f"converting {gallons} gallons to quarts")
        return gallons*4
    
    def quartsToPrints(quarts):
        print(f"converting {quarts} quarts to pints")
        return quarts*2
    
    def pintsToCups(pints):
        print(f"converting {pints} quarts to cups")
        return pints*2
    
    quarts = gallonsToQuars(gallons)
    pints = quartsToPrints(quarts)
    cups = pintsToCups(pints)
    return cups

print(convertGallonsToCups(1)) #op: 15
print(convertGallonsToCups(3)) #op: 48

#however we cant call a nested function directly . then we will get the below error
#print(pintsToCups(3)) #op: NameError: name 'pintsToCups' is not defined
    


## overall program output:
# converting 1 gallons to quarts
# converting 4 quarts to pints
# converting 8 quarts to cups
# 16
# converting 3 gallons to quarts
# converting 12 quarts to pints
# converting 24 quarts to cups
# 48
