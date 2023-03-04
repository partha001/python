#the not keyword is used either in front of a boolean expression or a boolean to negate

print(not True) #OP: Ralse
print(not False) #op: True

if "Hi" in "Hello":
    print("this does not get printed")

#now using not
if "z" not in "Hello":
    print("this gets printed as not makes the condition true")

