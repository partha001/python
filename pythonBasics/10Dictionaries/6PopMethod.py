## we have already seen the pop method w.r.t list . it works very similary for dictionary with some differences

years = [1991, 1995, 2000, 2007]
years.pop(1)
print(years) #op: [1991, 2000, 2007]


#if we invoke pop() on dictionary it will return the keyValue pair and also removes it from the dictionary at the same time
releaseDates = {
    "python": 1991,
    "Ruby":1995,
    "Java":1995,
    "Go":2007
}

year = releaseDates.pop("Java")
print(releaseDates) #op: {'python': 1991, 'Ruby': 1995, 'Go': 2007}   so java is removed


# however if the key that we are trying to pop() doesnt exist in the dictionary then will get a keyError exception
#year = releaseDates.pop("Rust") #op KeyError: 'Rust'

#one way to avoid this is by doing 
if "Rust" in releaseDates:
    releaseDates.pop("Rust")

#another way of dealing with this is by passing a second default fallback argument to the pop() method
#as shown below 
print(releaseDates.pop("Rust","2000")) #op: 2000
print(releaseDates) #op: {'python': 1991, 'Ruby': 1995, 'Go': 2007}