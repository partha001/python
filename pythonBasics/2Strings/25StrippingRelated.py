empty_space = "     some content     "
print("initial length", len(empty_space)) #op: initial length 22

#using the rstrip() we can remove space from the right side of the string
print(empty_space.rstrip())  #op:     some content
print(len(empty_space.rstrip()))  #op: 17   this is just to prove that spaces are indeed removed

#similarly we can use lstrip() to remove space from the left
print(empty_space.lstrip()) #op: some content     
print(len(empty_space.lstrip())) #17

#using the strip() will remove spaces from both sides
print(empty_space.strip()) #op: some content
print(len(empty_space.strip())) #op: 12


#the strip methods can also be used to remove characters from the start or end or both depending upon
#which strip method we are using
website = "www.python.org"
print(website.lstrip("w")) #op: .python.org
print(website.rstrip("org")) #op: www.python.

#note how it behaves for below . it will look for the characters that we want to strip from start or end. 
#1.it will not remove characters if they appear in the middle of the string
#2. also it checks for character or combination for if they appear in start or end . note '.' is not taken into accout in below case since match is not found
print(website.strip("worg.")) #op: python