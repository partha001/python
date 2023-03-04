def sumOfPositiveNumbers(values):
    total =0
    for value in values:
        if value>0:
            total += value
    return total

#doing the same using continue keyword
def sumOfPositiveNumbersWithContinue(values):
    total =0
    for value in values:
        if value <0:
            continue
        total += value
    return total

print(sumOfPositiveNumbers([1,2,-3,4])) #op: 7 since only -3 is not included in the sum
print(sumOfPositiveNumbersWithContinue([1,2,-3,4])) #op:7 here while iterating for -3 seeing the continue keyword the loop goes to the next element iteration