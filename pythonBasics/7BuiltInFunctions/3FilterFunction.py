animals = ["elephant","horse","cat","giraffe","cheetah","dig"]

#problemStatement: want to filter out those animals length is >=5

#solution1: using list comprehension
print([animal for animal in animals if len(animal)>=5])
#op: ['elephant', 'horse', 'giraffe', 'cheetah']

#solution2: lets do the same using filter
def myFilter(item):
    return len(item)>=5

print(list(filter(myFilter,animals)))
#op: ['elephant', 'horse', 'giraffe', 'cheetah']