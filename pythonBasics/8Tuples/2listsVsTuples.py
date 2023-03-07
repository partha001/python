heroes = ("batman","superman","spiderman","wonderwoman")

#like lists we can select values from tuples using index
print(heroes[0]) #op: batman
print(heroes[-1]) #op: wonderwoman

#howerver since tuples are immutable so we cant add or remove or modify value
#hence the below line will for tuple . but will work perfectly for list
#heroes[0] = "thor"   #op: TypeError: 'tuple' object does not support item assignment

addresses = (
    ["mumbai", "kolkata", "bangalore", "chennai"],
    ["maharashtra", "westbengal","karnataka","tamilnadu"]
)
# #though tuples are immutable . but we can change the values within the nested lists
addresses[0].append("patna")
addresses[1].append("bihar")
print(addresses)
## we can also modify the values in the lists
# addresses[0][0] ="patna"
# addresses[1][0] ="bihar"

#this is because the tuple is still not changing . its still references the same list objects . 
#and we are making changes on top of the list objects

#thus tuples are immutable but if the ojects that it holds are mutable then the state of those
#underlying objects can be changed




