breakfasts = ["eggs","cereal","banana"]
lunches = ["sushi","chicken kabab","soup"]
dinners = ["steak","meatballs","pasta"]

print(zip(breakfasts,lunches, dinners)) #<zip object at 0x0000021935B4E300>

#thus the zip functions combines the lists and builts a zip object
print(type(zip(breakfasts,lunches, dinners))) #<class 'zip'>

#zip object is iterable . now lets look at the internal structure of the zip object
print(list(zip(breakfasts,lunches, dinners)))
#op:   [('eggs', 'sushi', 'steak'), ('cereal', 'chicken kabab', 'meatballs'), ('banana', 'soup', 'pasta')]
#thus we can see that zip object has combined the list into touples


#now lets see how to iterate the zip
for a, b, c in zip(breakfasts,lunches, dinners):
    print(f"my meal today was {a} and {b} and {c}")
#op:
# my meal today was eggs and sushi and steak
# my meal today was cereal and chicken kabab and meatballs
# my meal today was banana and soup and pasta




