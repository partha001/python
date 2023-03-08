footballTeams = {
    "barcelona" : ["messi", "suarez", "neyman"],
    "realMadrid" : ["ronaldo", "zidane", "benzema"]
}

print(footballTeams["barcelona"]) #op: ['messi', 'suarez', 'neyman']

## adding new key to the dictionary
footballTeams["brazil"] = ["kaka","rivado","kafu"]
print(footballTeams)  
#op: {'barcelona': ['messi', 'suarez', 'neyman'], 'realMadrid': ['ronaldo', 'zidane', 'benzema'], 'brazil': ['kaka', 'rivado', 'kafu']}

## using the same syntax we can update value for a key
footballTeams["brazil"] = ["ronaldinho"]
print(footballTeams)
#op: {'barcelona': ['messi', 'suarez', 'neyman'], 'realMadrid': ['ronaldo', 'zidane', 'benzema'], 'brazil': ['ronaldinho']}


#example1: lets say we have a list of words and we want to get a 
# dictionary with the count of each work as value and the word itself as the key
animals = ["cats","dogs","lions", "dogs","cats", "cats"]

def countWords(words):
    wordCount = {}
    for word in words:
        wordCount[word] = wordCount.get(word,0) +1
    return wordCount

print(countWords(animals)) #{'cats': 3, 'dogs': 2, 'lions': 1}

