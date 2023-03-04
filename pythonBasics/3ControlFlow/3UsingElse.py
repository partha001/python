#using the else clause
value = int(input("enter some number"))
if value:
    print("entered value is truthy")
else:
    print("entered value is falsy")


#using else if
value = int(input("enter some number"))
if value>0:
    print("the entered number is greater than zero")
elif value==0:
    print("the entered value is equal to zero")
else:
    print("the entered number is negative")
