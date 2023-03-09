languages = ["python","javascript","ruby"]

lengths = {language:len(language) for language in languages}
print(lengths) #op: {'python': 6, 'javascript': 10, 'ruby': 4}


word = "supercalifragilelistticexpialaidocious"
letterCount = { letter: word.count(letter) for letter in word}
print(letterCount)
#op:
#{'s': 3, 'u': 2, 'p': 2, 'e': 3, 'r': 2, 'c': 3, 'a': 4, 'l': 4, 'i': 7, 'f': 1, 'g': 1, 't': 2, 'x': 1, 'd': 1, 'o': 2}


#lets say we want to get count of only those letters which appear after j
# then this can be done using a filter with comprehension as shown below 
letterCount = { letter: word.count(letter) for letter in word if letter >"j"}
print(letterCount) #{'s': 3, 'u': 2, 'p': 2, 'r': 2, 'l': 4, 't': 2, 'x': 1, 'o': 2}  


