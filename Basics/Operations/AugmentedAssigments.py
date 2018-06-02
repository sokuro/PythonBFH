"""
* Augmented Assignment is m-place updates with an augmented operator
"""


class SuperInt:
    def __init__(self, v):
        self.value = v

    def __add__(self, other):
        print('__add__')
        return SuperInt(self.value + other.value)

    def __iadd__(self, other):              # special method
        print('__iadd__')
        self.value += other.value
        return self


si1 = SuperInt(1)
si2 = SuperInt(10)

si1 = si1 + si2
print(si1)                              # >> __add__
print(si1.value)                        # >> 11

# invoking the special method __iadd__
si1 += si2
print(si1)                              # >> __iadd__
print(si1.value)                        # >> 21