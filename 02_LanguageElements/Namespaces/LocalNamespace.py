"""
    a local Variable hides the global One
"""


my_var = 10


def local_var():
    # print(my_var)       # Error: global Variable will be masked by the local
    my_var = 20
    print(my_var)


local_var()             # >> 20
print(my_var)           # >> 10

print('\n')

"""
    by defining the Variable global inside the function
"""


def local_var_2():
    global my_var
    print(my_var)       # global Variable: >> 10
    my_var = 20
    print(my_var)


local_var_2()           # >> 20
print(my_var)           # >> 20
