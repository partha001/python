numbers = [1,2,3,4]

#now lets say we can to create a list of square of above numbers
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares) #op [1, 4, 9, 16]


#now lets see how it be done using list comprehension
squares = [a  ** 2 for a in numbers]
print(squares) #op: [1, 4, 9, 16]
#note how the list comprehension take care of the requirement in one line


#finding length of each item using list-comprehension in single line
rivers = ["amazon","nile","ganges"] 
print([len(river) for river in rivers]) #op: [6, 4, 6]

expressions = ["lol", "rofl", "lmao"]
print([expression.upper() for expression in expressions])
#op: ['LOL', 'ROFL', 'LMAO']


decimals = [4.95, 3.28, 1.08]
print([int(decimal) for decimal in decimals]) #op: [4, 3, 1]