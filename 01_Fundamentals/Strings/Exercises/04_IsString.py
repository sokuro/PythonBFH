"""
    get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
"""


def IsString(str):
    if len(str) >= 2 and str[:2] == 'Is':
        return str
    else:
        return 'Is' + str


print(IsString("Testing"))
print(IsString("IsTesting"))
