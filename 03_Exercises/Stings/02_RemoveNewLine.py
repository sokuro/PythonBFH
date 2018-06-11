"""
    remove a newline
"""

# print the default string
string = 'remove a newline\n remove a newline'

print(string)


# remove '\n'
remove_newline = string.split("\n")

print(remove_newline)


# create a string with 'join'
temp = ""

bind_string = temp.join(remove_newline)

print(bind_string)
