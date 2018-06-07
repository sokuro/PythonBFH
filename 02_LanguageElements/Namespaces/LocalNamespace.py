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
