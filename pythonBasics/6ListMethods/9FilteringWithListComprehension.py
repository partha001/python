#problem statement : lets say i have a word 'donut' and i want the indexes of 
#each character in my word with respect the english-letters
alphabets = "abcdefghijklmnopqrstuvwxyz"
print([alphabets.index(char) for char in "donut"])
#op: [3, 14, 13, 20, 19]


#exampl2: problemStatement i want to see the half of every integer till 5
print([number/2 for number in range(6)])
#[0.0, 0.5, 1.0, 1.5, 2.0, 2.5]

#now lets see how to filetering works with list-comprehension
donuts = ["boston cream",
          "jelly",
          "vanilla cream",
          "glazed",
          "chocolate cream"]
#now lets say we want to filter those items having 'cream' in its name

#naive solution
creamyDonuts = []
for donut in donuts:
    if "cream" in donut:
        creamyDonuts.append(donut)
print(creamyDonuts)
#['boston cream', 'vanilla cream', 'chocolate cream']


#now lets see how this can be done using filtering with list-comprehension
print([item for item in donuts if "cream" in item])
#['boston cream', 'vanilla cream', 'chocolate cream']


#now lets say i want length of all item where the word 'cream' appears
print([len(element) for element in donuts if 'cream' in element])
#[12, 13, 15]

#thus grammer is :  [ <operation>  <for-loop> <filter-condition> ]


