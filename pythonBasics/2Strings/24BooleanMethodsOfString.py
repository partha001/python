#islower() :: returns true if all alphabetic characters are in lower case
print("winter".islower()) #op: True
print("winter 123_".islower()) #op: True
print("winter 123_A".islower()) #op: False


#similarly there is isupper()


#isalpha()  :: returns true if all characters are strictly alphabets
print("abc".isalpha()) #op: True
print("abc ".isalpha()) #op: False  since there is a space character

#isnumeric() :: return true if all characters are numbers
print("123".isnumeric()) #op: True
print("123a".isnumeric()) #op: False  since there is an alphabet

#isspace()
print(" ".isspace()) #op: True
print("      ".isspace()) #op: True
print("  1    ".isspace()) #op: False
