# A number is a value type - the variable's memory location holds that number.
# When you pass a value type as a parameter to a function, the function receives
# a copy of that value. Changing the parameter inside the function only changes
# the function's copy, not the original variable.
def test_value_type(parameter):
    parameter = 10

x = 5
print(x)
test_value_type(x)
print(x)


# A list is a reference type. The variable's memory location holds a reference (similar
# to a pointer) to another location in memory which holds the actual data. When you pass
# a reference type as a parameter to a function, the function receives a copy of that
# reference, which points to to the same point in memory, so the function can access
# the original data.

def test_reference_type(parameter):
    parameter.push(10)    # make an addition to the supplied list

my_list = [5]
print(my_list)
test_reference_type(my_list)
print(my_list)



# However, the copied reference can be reassigned to a new source of data without
# affecting the original reference. (This varies depending on which language is used)

def test_reference_type_2(parameter):
    parameter = [1,2,3] # create new list, the old one is left intacy

my_list_2 = [5]
print(my_list_2)
test_reference_type_2(my_list_2)
print(my_list_2)


# Objects instantiated from classes are also reference types
class my_class:
    def __init__(self):
        self.x = 100

def test_reference_type_3(parameter):
    parameter.x = 200

my_object = my_class()
print(my_object.x)
test_reference_type_3(my_object)
print(my_object.x)
