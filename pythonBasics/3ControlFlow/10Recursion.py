def countDownFrom(number):
    if number>=0:
        print(number)
        countDownFrom(number-1)


number = 5
countDownFrom(number)

