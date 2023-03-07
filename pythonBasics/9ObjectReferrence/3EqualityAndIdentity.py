#equality checks if two objects are equal ie. whether they have same value or not
#whereas identity checks if two names in the program point to the same object or not in the computer memory
    #identity is checked using the 'is' keyword


students = ["bob","sally","sue"]
atheletes = students
nerds = ["bob","sally","sue"]

## checking for equality
print(students == atheletes) #op:  True
print(students == nerds) #op: True


## checking for identity
print(students is atheletes) #op: True
print(students is nerds) #op: False
