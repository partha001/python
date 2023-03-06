def add(a,b):
    print("sum of ",a," and ",b," is :", a+b)

add(10,20) 
#these are called positional parameters
#here a=10 and b=20


#however we can choose to mention the parameter names explicitly
#if we mention the names explicity then order doesnt matter
add(b=20 , a=10)


#if we mention the parameter names partially then python applies position rules
#to the other arguments to which we have not mentioned names as below
add(10, b=20)

#but is has to be passed in the same the sequence 
#i.e. while the above works the below will not work
#therefore the below will throw syntax error
#add(b=20,10)
