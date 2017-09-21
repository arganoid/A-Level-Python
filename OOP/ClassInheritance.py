class Animal:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def make_noise(self):
        print("?")

    def print_age(self):
        print(self.age)


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def make_noise(self):
        print("woof")


class Cat(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def make_noise(self):
        print("meow")


my_dog = Dog("Fido", 3)
my_cat = Cat("Felix", 5)

if False:

    print(my_dog.name)
    my_dog.make_noise()
    my_dog.print_age()

    my_cat.make_noise()

    dogs = [my_dog]

    cats = [my_cat]
    cats.append( Cat("Mr Miaowington", 10) )


animals = [my_dog, my_cat]
animals.append( Dog("Rover", 1) )

for animal in animals:
    animal.make_noise()
