class Animal:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    def make_noise(self):
        print("?")

    def print_age(self):
        print(self.__age)

# Dog inherits from Animal
# Dog is the inherited class, Animal is the class we're inheriting from
# Dog is the derived class, Animal is the base class
# Dog is the child class, Animal is the parent class
# Dog is the subclass, Animal is the super class
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed

    def make_noise(self):
        print("woof")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_noise(self):
        print("meow")


my_dog = Dog("Fido", 3, "Terrier")     # Instantiate (ie create) a dog object, store a reference to it in my_dog
my_cat = Cat("Felix", 5)

my_dog.make_noise()
my_dog.print_age()

my_cat.make_noise()

cats = [my_cat]
cats.append( Cat("Mr Miaowington", 10) )


animals = [my_dog, my_cat]
animals.append( Dog("Rover", 1, "Alsatian") )

for animal in animals:
    animal.make_noise()
