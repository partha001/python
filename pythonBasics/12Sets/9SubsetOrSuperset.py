numbers1 = {1,2,3,4}
numbers2 = {3.0, 4}

print(numbers2.issubset(numbers1)) #op: True
#another way checkig this is a below 
print(numbers2 < numbers1)  #op: True
print(numbers2 <= numbers1)  #op: True
#we can choose to use < or <= both works fine

#conversly we can check for superset
print( numbers1.issuperset(numbers2)) #op: True
print( numbers1 >= numbers2) #op: True




