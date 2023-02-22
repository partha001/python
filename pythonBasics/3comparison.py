print(5==5) #op: true

#mismatched datatypes are treated as false
print(True== 'True') #op: False
print(5 == 5.0) #op:true howerver first type promotion happens and then comparison
print(5=="5") #op:false

print(10 == 10.0) #op: true
print(10 == "10.0") #op: false


print(5<8) #op: true
print(5<8<10) #op: true . these comparisons are and associated
print(5<8>10) #op: false . resturns false since these conditions are 'AND' associated

