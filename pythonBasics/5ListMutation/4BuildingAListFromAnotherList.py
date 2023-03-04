numbers = [1,2,3,4,5]
#example1
def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number**2)
    return squares

print(squares(numbers)) #op: [1, 4, 9, 16, 25]



#exampl2
def converToFloat(numbers):
    floats = []
    for number in numbers:
        floats.append(float(number))
    return floats

print(converToFloat(numbers)) #op: [1.0, 2.0, 3.0, 4.0, 5.0]


#exampl3
def evenOdd(numbers):
    result = []
    for number in numbers:
        if number%2==0:
            result.append("even")
        else:
            result.append("odd")
    return result

print(evenOdd(numbers)) #op: ['odd', 'even', 'odd', 'even', 'odd']