#\n represents new line
print("this will be \nstart of a new line")

# \t is for a tabular space
print("\tOnce upon a time")

# if there are quotes within string that can negated by backslash
print("\"To be, or not to be\" - said Hamlet")
print('\'To be, or not to be\' - said Hamlet')

# similarly if there is a \ within the string then it can negated by another \
print("what a \\wonderful world")

# if want python  to read a string a raw i.e as it is avoid the special character parsing
# the for raw add r in front of text as show below
text = r"c:\news\travel"
print(text)


#if there is a large string which needs to be splitted across multiple lines
#then it can be easily done using \ as shown below 
someRandomNumber = 5
someObscureNumber = 10
someAdditionalNumber = 20
myvar = someRandomNumber + \
        someObscureNumber + \
        someAdditionalNumber
print(myvar)

