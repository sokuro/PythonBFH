class Pet:

    def __init__(self, name):

        self.name = name


class Dog(Pet):

    def get_noise(self):

        return 'woof!'


class LapDog(Dog):

    def get_noise(self):

        return 'yip!'


class LoudLapDog(LapDog):

    def get_noise(self):

        noise = super().get_noise().upper()

        return noise * 3


def main():

    x = Dog("Rex")

    print(x.name)           # >> Rex
    print(x.get_noise())    # >> woof!

    y = LapDog("Kato")

    print(y.name)           # >> Kato
    print(y.get_noise())    # >> yip!

    z = LoudLapDog("Arta")

    print(z.name)           # >> Arta
    print(z.get_noise())    # >> YIP!YIP!YIP!


main()
