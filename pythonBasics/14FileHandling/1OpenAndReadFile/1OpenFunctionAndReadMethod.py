#here we arg1=file location  and secondArg= mode in which we want to open the file . 
#here passing arg2="r" since we want to open the file in read mode
myFile = open("sample.txt","r")
myFile.close()


#now this is not the recommened way of opening a file . since the while opening and parsing of the file
#if anything goes wrong then the file will continue to remain open and the close() is never called. this 
#might corrup the file


#the recommened way is using the with clause as shown below 
with open("sample.txt","r") as myfile2:
    print("file accesssible now")
    #ie.. any file related open will go inside this block
    #and then the control moves out of this block it will automatically close the file
    content = myfile2.read()
    print(content)



## we can also take the file name as input from user as shown below
#
# filename = input("please enter the filename with path that u want to read")
# with open(filename,"r") as myfile2:
#     content = myfile2.read()
#     print(content)
