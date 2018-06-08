"""
    global: binds a Variable to the global Scope
    nonlocal: binds a Variable to the enclosing Function Scope
    Assignments to Names ALWAYS go into the innermost Scope
"""


def scope_test():

    def do_local():
        spam = "local spam"

    def do_non_local():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"

    do_local()
    print('After local Assignment: ', spam)     # >> test spam

    do_non_local()
    print('After nonlocal Assignment: ', spam)  # >> nonlocal spam

    do_global()
    print('After global Assignment: ', spam)    # >> nonlocal spam


def main():
    scope_test()
    print('In global Scope: ', spam)            # >> global spam


main()
