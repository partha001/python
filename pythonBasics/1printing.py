#by default prints are printed in new lines
print("Hello world")
print('This is wonderfu day')

# using the end paramater in print
print("india is my country.",end="") #default end is \n howerver since we have end='' so the next line appears after this line
print("i love my country.")

# passing multiple values to print
print("A","B","C","D"); #note these values are separeted by space
print("A","B","C","D",sep="") #note: no separation works


#note that for named parameters the order in which they are passed doent matter
print("1","2","3","4", sep="#",end="\n"); 
print("1","2","3","4", end="\n",sep="#"); 