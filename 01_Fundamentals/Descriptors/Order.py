"""
    Descriptor for non negative Values
"""


class NonNegative:

    # since Python 3.6
    # def __set_name__(self, owner, name):
    #     self.name = name

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]     # Assign the Attribute

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative!')
        instance.__dict__[self.name] = value


class Order:

    # implementing the Descriptor
    price = NonNegative('price')
    quantity = NonNegative('quantity')

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


def main():
    apple_order = Order('apple', 1, 10)
    print(apple_order.total())


main()
