"""
    Variables, Function's Parameters, Attributes reside in Namespaces
"""

# global Scope
my_var = 10


def global_var():
    print(my_var)   # global Variable is accessible


global_var()      # >> 10
print(my_var)       # >> 10
