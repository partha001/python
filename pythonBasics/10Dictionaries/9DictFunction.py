# the dict() function is used to create dictionaries

#we have already seen similar functions earlier for list and string
print(list("abc")) #op: ['a', 'b', 'c']
print(str(9)) #op:  9
#similarly we can create a new disctionary using the dict()
print(dict()) #op: {}


#calling the dict function with values
employeeTitle = [
    ["mary","seniorVicePresident"],
    ["brian","vicePresident"],
    ["julie","assistantVicePresident"]
]
print(dict(employeeTitle))
#op: {'mary': 'seniorVicePresident', 'brian': 'vicePresident', 'julie': 'assistantVicePresident'}
#note we can pass any dictionary compatible structure to the dict function and python will try and convert this to a dictionary for us

