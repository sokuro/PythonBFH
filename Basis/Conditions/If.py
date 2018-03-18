"""
* The is NO switch statement in Python!
"""


class DefineIfStatement:
    # def __init__(self, v):
    #     self.value = v

    words1 = ["test1", "test2"]
    words2 = ["other1", "other2"]

    value = input("Enter a word")

    if value in words1:
        print('the value is test1')

    elif value in words2:
        print('the value is test2')

    else:
        print('no value')


# DefineIfStatement('other1')
DefineIfStatement()