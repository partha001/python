bubbleTeaFlavors = [ ["honeydew","mango","passionFruit"], ["peach","plum","strawberry","taro" ]]


#for the sake of readablity we can also break it into multiple lines
bubbleTeaFlavors = [ 
    ["honeydew","mango","passionFruit"], 
    ["peach","plum","strawberry","taro" ]
]

print(len(bubbleTeaFlavors)) #op: 2
print(len(bubbleTeaFlavors[0])) #op: 3
print(len(bubbleTeaFlavors[1])) #op: 4
print(len(bubbleTeaFlavors[-1])) #op: 4
#we can also make use of slicing to read a particular required range 
#of values with the sublist

#reading an item from the nested list
print(bubbleTeaFlavors[0][2]) #op: passionFruit

#converting bubbleTeaFlavors into a 1-d list
allFlavors = []
for flavorPack in bubbleTeaFlavors:
    for flavor in flavorPack:
        allFlavors.append(flavor)


print(allFlavors)
#op: ['honeydew', 'mango', 'passionFruit', 'peach', 'plum', 'strawberry', 'taro']


