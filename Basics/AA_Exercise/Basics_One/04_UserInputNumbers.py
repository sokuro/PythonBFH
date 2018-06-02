"""
    Input: Comma separated Numbers
    Output: List and Tuple
"""


""" 
    List:
    > mutable
    > Size can be changed during Execution 
"""

numbersInput = input('Input some Values separated by Space: ')

list = numbersInput.split(" ")

print('List: ', list)


"""
    Tuple:
    > immutable
    > Size can not be changed during Execution
"""
tuple = tuple(list)

print('Tuple: ', tuple)
