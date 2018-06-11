"""
    lowercase first n characters in a string
"""


str_input = input('Enter a String: ')

int_input = int(input('Enter the Number of Characters: '))

print(str_input[0:int_input].lower() + str_input[int_input:])
