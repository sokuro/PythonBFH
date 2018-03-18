"""
* Refusing to create a specific item's value
"""

class Person():
    def __setattr__(self, key, value):
        if key == 'value':
            raise AttributeError('No values of the Persons')
        super().__setattr__(key, value)


def main():
    eve = Person()
    eve.name = 'Eve'
    print(eve.name)
    eve.value = 42


main()