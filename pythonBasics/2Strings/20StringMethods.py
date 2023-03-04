# retuns the index if character is found
browser = "Google Chorme"
print(browser.find("C")) #prints 7
print(browser.find("z")) #prints -1
print(browser.find("Goo")) #prints 0
print(browser.find("Good")) #prints -1
#an overriden form of find where we can mention from which startIndex we want to look
print(browser.find("C",8)) #prints -1
#another overriden from of find is to mention both start and end
print(browser.find("m",1,7)) #prints -1



# index() works the same as find() but its more strict i.e. it will make 
# the program fail if the search string is not found
print(browser.index("C")) #prints 7
print(browser.index("z")) #ValueError: substring not found





