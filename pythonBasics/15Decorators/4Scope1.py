age = 28

def fancyFunction():
    age = 100 #note this this is a completely separate variable with the 
    #same name and its scope is restricted to the method
    print(age)

fancyFunction()
print(age)

TAX_RATE = 0.06

def calculateTax(price):
    return round(price * TAX_RATE , 2)

def calculateTip(price):
    return round(price * (TAX_RATE*3),2)

print(calculateTax(10)) #op: 0.6
print(calculateTip(10)) #op: 1.8