print(all([True]))  #op: True
print(all([True,True])) #op: True
print(all([])) #op: True
print(all([True,False])) #op: False


print(any([True]))  #op: True
print(any([True,True])) #op: True
print(any([])) #op: False
print(any([True,False])) #op: True

#it doesnt necessarily be a list of boolean elements . 
#in case of other list item values it will depend on the truthiness of falsiness of the value

print(all([1,2])) #op: True
print(all([1,0])) #op: False

print(any([" ",""])) #op: True
print(any([""])) #op: False



