def divide_5_by_number(n):
    try:
        calculation = 5 / n
    except (ZeroDivisionError, TypeError) as e:
        return f"Something went wrong. The error was {e}"
    return calculation

# if we were to handle different exceptions differently then it should be written as 
    # except ZeroDivisionError:
    #     return "Something went wrong. The error was"
    # except TypeError as e:
    #     return f"Something went wrong. The error was {e}"


print(divide_5_by_number(10))
print(divide_5_by_number(0))
print(divide_5_by_number("nonsense"))


# program output:
# 0.5
# Something went wrong. The error was division by zero
# Something went wrong. The error was unsupported operand type(s) for /: 'int' and 'str'