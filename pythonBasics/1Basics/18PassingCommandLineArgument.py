#the command line arguments are loaded onto a list. 
#however for this we need to import sys

import sys

print(sys.argv)
print(type(sys.argv))

#output: 
# /python.exe e:/git/python/pythonBasics/18PassingCommandLineArgument.py 10 20  
# ['e:/git/python/pythonBasics/18PassingCommandLineArgument.py', '10', '20']
# <class 'list'>

#note: it takes the python filename that we run as the first argument


print("")


wordLength =0
for arg in sys.argv[1:]: #reading from index 1 to skip the filename
    wordLength += len(arg)

print(F"total length of all the parameter passed is {wordLength}")
#ouput: 
# python.exe e:/git/python/pythonBasics/18PassingCommandLineArgument.py 10 20  
#total length of all the parameter passed is 4

