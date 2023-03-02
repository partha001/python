def add(a=0,b=0):
    return a+b

print(add(10,20))

print(add()) #also note that mentioning default values make the parameters optional


print(add(10)) #note that here the 10 will be assigned to a. while b will take default value.