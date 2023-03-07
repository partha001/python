colors1 = "red" , "blue" , "green", "yellow"
colors2 = ("red" , "blue" , "green", "yellow")

print(type(colors1)) #op: <class 'tuple'>
print(type(colors2)) #op: <class 'tuple'>


#declaring empty tuple
empty = ()
print(type(empty)) #op: <class 'tuple'>

#it is also to be noted that its the presence of a comma that tells python its a tuple
#thus if there is only one element and we declare it as below . then its an integer
variable1 = (1) 
print(type(variable1)) #op: <class 'int'>
#to tell python its a tuple we have to declare it like 
variable2 = 1, 
print(type(variable2)) #op: <class 'tuple'>

#as mentioned earlier for declaring a tuple parenthesis is not necessary. but comma is . so if we have 
#only 1 element in our tuple then by best practice we should declare it as
variable3= (1,)
print(type(variable3)) #op: <class 'tuple'>


#we can also convert a list to a tuple as shown below 
print(tuple(["red" , "blue" , "green", "yellow"])) #op: ('red', 'blue', 'green', 'yellow')
#note we see the parenthesis in the above output which tells us its a tuple

#also to note that if we pass a single string argument to the tuple 
#then the elements elements in tuple will the the characters present in the string
print(tuple("abc")) #op: ('a', 'b', 'c')


