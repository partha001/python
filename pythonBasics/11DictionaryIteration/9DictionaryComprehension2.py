#creating one dictionary to another 
capitals = {
    "NewYor":"Albany",
    "California":"Sacramento",
    "Texas":"Austin"
}

#now lets say i want to invert this dictionary ie. value will be keys and keys will be values
#lets see how to do this using dictionary comprehension
inverted = {capital:state for state,capital in  capitals.items()}
print(inverted) #{'Albany': 'NewYor', 'Sacramento': 'California', 'Austin': 'Texas'}


#lets add a filter on top of this i.e. invert only for those state where length>5
inverted2 = {capital:state for state,capital in  capitals.items() if len(state)>5}
print(inverted2) #{'Albany': 'NewYor', 'Sacramento': 'California'}