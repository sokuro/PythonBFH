class Person:
    """
        no attributes
    """
    pass


def main():
    bob = Person()
    # print(bob.name)             # >> ERROR: no attribute name

    eve = Person()
    eve.name = 'Eve'
    print(eve.name)


# Execute the main function
main()