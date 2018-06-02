# Handling Substrings
str = "Lorem ipsum dolor sit amet."

print(str)
print(str[1])
print(str[3:8])
print(str[3:])
print((str + '\n') * 3)     # concatenation


""" 
    split String 
    sep= separate by Char
    maxsplit= List with maxsplit+1 Elements
"""
stringSplit = str.rsplit(sep='m', maxsplit=3)
print(stringSplit)
