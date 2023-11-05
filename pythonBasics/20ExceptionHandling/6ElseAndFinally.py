x = 10

try:
    print(x + 5)
except NameError:
    print("Some variable is not defined!")
else:
    print("This will print if there is no error in the try.")
finally:
    print("This will print with or without exception") 
    print("Closing file...")


# #program output
# 15
# This will print if there is no error in the try.
# This will print with or without exception
# Closing file...