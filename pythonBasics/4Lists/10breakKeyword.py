print(2 in [1,2,3]) #op: prints true


def contains(values, target):
    found = False

    for value in values:
        print(value)
        if(value==target):
            found=True
            break
    
    return found

print(contains([1,2,3] ,2)) #op: True