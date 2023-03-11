#the previous program is good while dealing with small files
#however if we are dealing with a large file then loading the content
#into a single in-memory variable can make the program crash with out of memory
#so the recommended approach is to read the file line by line

with open("sample.txt") as myFile:
    for line in myFile:
        #print(line) ## note the print function adds one more line break after each line. 
        
        #if we dont want this then we can do this 
        print(line.strip())