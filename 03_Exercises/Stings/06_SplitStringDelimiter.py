"""
    split a string on the last occurrence of the delimiter
"""


str_input = input('Enter a String: ')

# create a list from the string
temp_list = list(str_input)

int_input = int(input('Enter a Number of split Characters: '))

print(str(temp_list).rsplit(',', int_input))
