phoneNumber = "555 555 1234"
print(phoneNumber.replace(" ","-")) #op: 555-555-1234
print(phoneNumber.replace("5","9")) #op: 999 999 1234
#note the since is strings are mutable so the initil variable remains same.
#its just that the replace returns a new string object after doing the replacement
print(phoneNumber) #555 555 1234
