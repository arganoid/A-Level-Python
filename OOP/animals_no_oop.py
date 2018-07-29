animal_names = []
animal_types = []
animal_ages = []

# Add George, who is an dog and is 3 years old
animal_names.append("George")
animal_types.append("Dog")
animal_ages.append(3)

# Add Susan, who is a cat and is 5 years old
animal_names.append("Susan")
animal_types.append("Cat")
animal_ages.append(3)

def animal_make_noise(animal_id):
    if animal_types[animal_id] == "Dog":
        print("Woof")
    elif animal_types[animal_id] == "Cat":
        print("Meow")

animal_make_noise(0)
animal_make_noise(1)
