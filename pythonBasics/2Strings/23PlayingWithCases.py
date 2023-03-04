mySentence = "once upon a time in india"
#capitalize()  : this method will capitalize the first character only
print(mySentence.capitalize()) #OP: Once upon a time in india

#title() : this method capitalizes the first and every-character that follows a space
print(mySentence.title()) #op: Once Upon A Time In India

#upper() : this method changes everything to capitals
print(mySentence.upper()) 

#lower()
word2 = "HELLO"
print(word2.lower()) #OP: hello

#swapcase() : this method inverses the cases
companyName = "Adobe"
print(companyName.swapcase()) #OP: aDOBE

#method chaining
name = "BENJAMIN FRANKLIN"
print(name.lower().title()) #OP: Benjamin Franklin
#it is to be noted since strings are immutable so every chainging intermediate 
#produces a new string
