#note how using the string literal we can format strings without using the format() 
#this is more modern way of writing code which results in less code
name ="Bobby"
adjective = "green"
noun = "alient"
madLibs = f"{name} laughed at the {adjective} {noun}" #Bobby laughed at the green alient
print(madLibs)


#using f-literal and {} makes python treat {}  as an expression and evaluate/replace vaules in it
sentence = f"2 + 2 is {2+2}" #2 + 2 is 4
print(sentence)


