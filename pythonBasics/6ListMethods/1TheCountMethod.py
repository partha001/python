heroes = ["superman","batman","superman"]
print(heroes.count("superman")) #op: 2
print(heroes.count("wonderwoman")) #op: 0
#also does a case-sentisitive search and count
print(heroes.count("Superman")) #op: 0


#however in case of numbers it intelligently searches the value
hoursOfSleep = [7.0 , 7.0, 8 , 9]
print(hoursOfSleep.count(7.0)) #op: 2
print(hoursOfSleep.count(7)) #op: 2
print(hoursOfSleep.count(10))  #op: 0


