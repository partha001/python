madLibs = "{} laughed at the {} {}"

#now there are 3ways in which we can pass the parameters to the format method
# 1.by relative position 2.by numeric position  3.by keyword arguments

# when passed by relative position
print(madLibs.format("Bobby","green","alien")) #op: Bobby laughed at the green alien

#however if we dont pass the same number of argument it will throw Index error as for the below line
#print(madLibs.format("Bobby","green"))

#however if we pass more arguments then we will not run into error
print(madLibs.format("Bobby","green","alien","sometext")) #op: Bobby laughed at the green alien



### passing argument by numeric position
sentence = "{0} laughed at the {1} {2}"
print(sentence.format("Bobby","green","alien")) #op:Bobby laughed at the green alien

sentence = "{2} laughed at the {1} {0}"
print(sentence.format("Bobby","green","alien")) #op: alien laughed at the green Bobby

# it is also to note that below lines will throw index error
# sentence = "{4} laughed at the {5} {6}"
# print(sentence.format("Bobby","green","alien"))


### passing vales using keyword parameter
sentence = "{name} laughed at the {adjective} {noun}"
print(sentence.format(name="Bobby",adjective="green", noun="alien")) #Bobby laughed at the green alien
#advantage1: using this technique the advantage is that the order of parameters doesnt matter anymore
#advantage2: the same parameterName can be resused and the same value dosnt need to be passed as shown below 
sentence2 = "{name} is my country and i love my country {name}" #op: India is my country and i love my country India
print(sentence2.format(name="India")) 


#taking input and replacing in string
name = input("enter any name")
adjective = input("enter an adjective")
noun = input("enter a noun")
sentence3 = "{name} laughed at the {adjective} {noun}"
print(sentence3.format(name=name, adjective = adjective , noun=noun)) #op: partha laughed at the good mimi





