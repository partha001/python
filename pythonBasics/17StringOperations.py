#finding length of a string
print(len("partha"))

#reading a particular character
param = "partha"
print(param[0])
#if we pass -ve values then it will read from the end
print(param[-1])

#string slicing. ie. equivalent of substring in java
sentence="India is my country.I love my country."
print(sentence[0:5])
print(sentence[-18:-1])
#print(sentence[-1:-18]) however this is incorrect and will not print anything

#optionally we can pass only one paramter 
print(sentence[:19]) 
# if we dont mention any start it will print from start
# thus its essentially same as print(sentence[0:19]) 

print(sentence[20:]) #similarly if we dont mention any end then it will print till the end

print(sentence[:]) #this returns a copy of the initial string . ie. a new string object

