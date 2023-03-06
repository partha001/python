#the help functin is useful to see documentation and usage of any function or method
#we can either directly pass the functionName as parameter or we can pass it as string
help(len)
help(print)
help("len")
help("print")


help(str)
help(int)
help(list)


#we can also pass method-names to it. 
# however method are always called on top of an object
# so method names are passed as below
help("hello".replace)


help([1].extend)