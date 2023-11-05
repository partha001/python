def divideFiveByNumber(n):
    try:
        print("before action")
        calculation = 5/n
        print("after action")
    except:
        calculation = 5
    return calculation

print(divideFiveByNumber(0)) #op: 5
print(divideFiveByNumber(10)) #op: 0.5
print(divideFiveByNumber("nonsense")) #op: 5



# thus the try block is executed if there are no errors
# however if there are any errors they the block inside except is execute. 
# its like a catch block

# a try cant exist in isolation , an except is mandatory . however if we dont have any
# action to perform on exception then we can declare except as below 
# except:
#    pass



