#sort uses natural order sorting 
# i.e. it list items are letters then it will be sorted in lexicographical order
# if listElements are numbers then they will be sorted in ascending order



numbers = [10.1 , 2, 200 , 1]
numbers.sort()
print(numbers) #op: [1, 2, 10.1, 200]

#to sort in descending
numbers = [10.1 , 2, 200 , 1]
numbers.sort()
numbers.reverse() 
print(numbers) #[200, 10.1, 2, 1]

#also to be noted that this is a case-sensitive sort i.e first all the uppercase are sorted and then the lowerCase
letters = ["Lz","l", "aA", "x"]
letters.sort()
print(letters) #op: ['Lz', 'aA', 'l', 'x']
