import sushi
import math

## accessing docString of module
print(sushi.__doc__)
## output
# A module related to the joy of sushi.
# No fishy code found here!


## accessing docstring of a function declared within the module
print(sushi.fish.__doc__)
## output
    # Determines if fish is a good mean choice.
    # Always returns True, because it always is.

## accessing the docstring of a class written inside in the module
print(sushi.Salmon.__doc__)
## output
    # Blueprint for a Salmon object

## accessing the docstring of an instance method
print(sushi.Salmon.bake.__doc__)
## output
        # Bake the fish in an oven

## accessing the docstring of inbuilt modules and methods
print(math.__doc__)
## output
# This module provides access to the mathematical functions 
# defined by the C standard.

print(math.sqrt.__doc__)
## output
# Return the square root of x.

## another way accessing the docstring is by using the help function.
## however if we use the help() to access the docstring then we dont need to use print
## a print is called internally by the help()
help(sushi)
##output
# Help on module sushi:

# NAME
#     sushi

# DESCRIPTION
#     A module related to the joy of sushi.
#     No fishy code found here!

# CLASSES
#     builtins.object
#         Salmon

#     class Salmon(builtins.object)
#      |  Blueprint for a Salmon object
#      |
#      |  Methods defined here:
#      |
#      |  __init__(self)
#      |      Initialize self.  See help(type(self)) for accurate signature.
#      |
#      |  bake(self)
#      |      Bake the fish in an oven.
#      |
#      |  ----------------------------------------------------------------------
#      |  Data descriptors defined here:
#      |
#      |  __dict__
#      |      dictionary for instance variables (if defined)
#      |
#      |  __weakref__
#      |      list of weak references to the object (if defined)       

# FUNCTIONS
#     fish()
#         Determines if fish is a good meal choice.
#         Always return True, because it always is.

# FILE
#     c:\parthafiles\git\python\pythonbasics\18classesmagicmethods\5docstrings\sushi.py

## note: thus the help() prints the docstring in a more readable way
