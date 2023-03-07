plays = ["hamlet", "macbeth", "kingLear"]
plays.insert(1,"juliusCeaser")
print(plays) #op: ['hamlet', 'juliusCeaser', 'macbeth', 'kingLear']


plays.insert(0,"romeoAndJuliet")
print(plays) #['romeoAndJuliet', 'hamlet', 'juliusCeaser', 'macbeth', 'kingLear']

#note that this will not throw error though there are not 100 elements
#rather python will silently add this to the end of the list
plays.insert(100,"aMidsummerNightsDream")
print(plays) #['romeoAndJuliet', 'hamlet', 'juliusCeaser', 'macbeth', 'kingLear', 'aMidsummerNightsDream']