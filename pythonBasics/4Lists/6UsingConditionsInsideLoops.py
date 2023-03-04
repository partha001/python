values =[3,6,9,12,15,18,21,24]
otherValue =[5,10,15,20,25,30]

def oddSum(numbers):
    total =0
    for number in numbers:
        if number % 2==1:
            total += number
    return total

print(oddSum(values)) #op: 48
print(oddSum(otherValue)) #op: 45