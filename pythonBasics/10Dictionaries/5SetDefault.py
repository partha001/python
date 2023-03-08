#setDefault() method is used to write key value to a dictionary if the key
# if the key doesnt already exist in the dictionary

filmDirectors = {
    "theGodfather": "francisFordCoppola",
    "theRock": "michaelBay",
    "goodfellas": "martinScorsese"
}

print(filmDirectors.get("goodFellas")) #op: None
print(filmDirectors.get("badBoys","michaelBay")) #op: michaelBay   
#i.e. returns the default value without making any change to the dictionary
#this can be confirmed as below 
print(filmDirectors)
#op: {'theGodfather': 'francisFordCoppola', 'theRock': 'michaelBay', 'goodfellas': 'martinScorsese'}

#now lets explore the setDefault()
filmDirectors.setdefault("badBoys","michaelBay")
print(filmDirectors)
#op {'theGodfather': 'francisFordCoppola', 'theRock': 'michaelBay', 'goodfellas': 'martinScorsese', 'badBoys': 'michaelBay'}


filmDirectors.setdefault("badBoys","a good director")
print(filmDirectors)
#op: {'theGodfather': 'francisFordCoppola', 'theRock': 'michaelBay', 'goodfellas': 'martinScorsese', 'badBoys': 'michaelBay'}
#it is to be noted that badBoys still has michaelBay because the setDefault() works only if the key doesnt exist


#it is also to be noted that if we call the setDefault() without passing the second value arugment
#then the key will get pushed with a value None
filmDirectors.setdefault("batman")
print(filmDirectors)
#op: {'theGodfather': 'francisFordCoppola', 'theRock': 'michaelBay', 'goodfellas': 'martinScorsese', 'badBoys': 'michaelBay', 'batman': None}
 


