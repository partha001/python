#for number 0=falsiness and any other value including -ve has truthiness 
if 3:
    print("this will be printed")

if 0:
    print("this will not be printed")


#for strings : empty strings has falisness while string having any character has truthiness
if "":
    print("this will not be printed. hence has faliness")

if " ":
    print("this will be printed. since there is a blank character has truthiness")


#we can also find the truthiness or falsines of value by passing it to the bool function
print(bool(1)) #this prints true
print(bool(0)) #this prints false
print(bool(0.0)) #this printes false