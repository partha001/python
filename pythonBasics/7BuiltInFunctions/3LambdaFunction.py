metals = ["gold","silver","iron","platinum","palladium"]

#filter all metals having name-length >=5
#prevously we have done this as
def myFilter(item):
    return len(item)>=5
print(list(filter(myFilter, metals)))
#op: ['silver', 'platinum', 'palladium']



#now lets do this using lambda. since lambdas are anonymous inline implementation
#so here we will pass a lambda to the filter method instead of passing a defined function the previous
print(list(filter(lambda i: len(i)>=5, metals)))
#op: ['silver', 'platinum', 'palladium']



#one more usecase: lets filter all metals that have starts with p using lambda
print(list(filter(lambda a: a.startswith("p"), metals )))
#op: ['platinum', 'palladium']