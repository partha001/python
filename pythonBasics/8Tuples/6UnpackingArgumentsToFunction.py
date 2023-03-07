def product(a,b):
    return a*b

print(product(3,5)) #op: 15

numbers1 = [3,5]
numbers2 = (3,5)

#the below lines will give the errors mentioned aside since the function takes 2 arguments however we are passing only one
# print(product(numbers1)) #op: TypeError: product() missing 1 required positional argument: 'b'
# print(product(numbers2)) #op: TypeError: product() missing 1 required positional argument: 'b'


#however it is possible to invoke the function as mentioned below 
print(product(*numbers1))
print(product(*numbers2))



