number = 0.123456789

print(format(number,"f")) #op: 0.123457    .ie.formats the number to string
print(type(format(number,"f"))) #op: <class 'str'>

#if we want to consider only 2 descimal points
print(format(number,".2f")) #0.12

print(format(0.5,"f")) #op: 0.500000
print(format(0.5,"%")) #op: 50.000000%
print(format(0.5,".2%")) #op: 50.00%


print(format(12345,",")) #op: 12,345


#refer to python documentation for more on formatting techniques and symbols 
