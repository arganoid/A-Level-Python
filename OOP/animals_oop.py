# Dog, Cat and Elephant classes - not using inheritance

class Dog():
    def __init__(self, name, age, breed):
        self.__name = name          # __ = private
        self.__age = age
        self.__breed = breed

    def make_noise(self):
        print("woof")

    def print_age(self):
        print(self.__age)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

class Cat():
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    def make_noise(self):
        print("meow")

    def print_age(self):
        print(self.__age)

class Elephant():
    def __init__(self, name, age, trunk_length):
        self.__age = age
        self.__name = name
        self.trunk_length = trunk_length

    def make_noise(self):
        print("elephant noise")

    def print_age(self):
        print(self.__age)


# Instantiate (i.e. create) a dog object, store a reference to it in my_dog
# Objects are also sometimes called instances
my_dog = Dog("Fido", 3, "Terrier")

print(my_dog.name)
dog_age = my_dog.get_age()
my_dog.breed = "Labrador"

my_dog.make_noise()
my_dog.print_age()

my_dog.set_age(10)


# Instantiate (i.e. create) a cat object, store a reference to it in my_cat
my_cat = Cat("Felix", 5)
my_cat.make_noise()

# Instantiate (i.e. create) an elephant object, store a reference to it in my_elephant
my_elephant = Elephant("Jumbo", 20, 3)
my_elephant.make_noise()
