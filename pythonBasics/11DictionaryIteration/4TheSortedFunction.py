numbers = [ 4, 7, 2, 9]
print(sorted(numbers)) #op: [2, 4, 7, 9]
print(numbers) #op: [4, 7, 2, 9]
#note that the sorted function doesnt actually rearrage the items. it just returns a sorted view.
# to rearrege the items we have to 
numbers = sorted(numbers)
print(numbers) #op: [2, 4, 7, 9]

#the sorted() function sorts the elements as per their natural ordering
#i.e. for strings it will get sorted in the lexicographical order

salaries = {
    "executiveAssistant": 20,
    "ceo": 100
}


print(sorted(salaries)) #op: ['ceo', 'executiveAssistant'] 
#i.e the above line just returns a sorted view of the keys in dictionary

#to sort on the basis of values
print(sorted(salaries.values())) #op: [20, 100]





