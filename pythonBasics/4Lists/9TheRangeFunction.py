#passing only the end
for element in range(10):
    print(element) #this will print from 0 to 9. ie. endExclusive

#passing both start and end
for number in range(0,10):
    print(number) #this print from 0 to 9 . i.e. startInclusive and endExclusive


#passing 3 argument . the 3rd argument is the interval
for number in range(0,10,2):
    print(number) #this will print 0 2 4 6 8 

for number in range(10,1,-2):
    print(number) #this will print 10 8 6 4 2
