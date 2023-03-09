emptySet = {}
print(type(emptySet)) #op: <class 'dict'>  since its empty

#to create an empty set we have to use the setFunction
print(type(set())) #op  <class 'set'>

stocks = {"microsoft","facebook","ibm","facebook","google"}
print(type(stocks)) #op: <class 'set'>
print(stocks) #op: {'facebook', 'ibm', 'microsoft', 'google'}
##note that though we have mentioned facebook twice but it maintains only one entry
#i.e. doesnt allow duplicates

#again we can next elements in it . i.e. say a list of tuples
lotteryNumbers = {(1,2,3),(4,5,6)}
print(lotteryNumbers) #op: {(1, 2, 3), (4, 5, 6)}


print("google" in stocks) #op: True
print("wallmart" in stocks) #op False

for number in lotteryNumbers:
    print(number)
##
# (1, 2, 3)
# (4, 5, 6)



