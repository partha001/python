#in is to check if a value exists in list or not
meals = ["breakfast", "lunch", "dinner"]
print("lunch" in meals) #op: True

testScores = [99.0, 35.0, 23.0]
print(99 in testScores) #op: True . note that it intelligently checks for the value and not type
print("99" in testScores) #op: False 
#the not-in is the inverse of in
print(1000 not in testScores) #op: True
print(23 not in testScores) #op: False
