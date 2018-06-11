"""
    Inheritance Diamond Problem
"""


class A:
    def m(self):
        return 'm of A called'


class B(A):
    def m(self):
        return 'm of B called'


class C(A):
    def m(self):
        return 'm of C called'


class D(B, C):
    pass


def main():

    d = D()

    print(d.m())


main()              # >> 'm of B called
