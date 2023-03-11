def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20
    
    inner()
    return x

print(outer()) #op: 20