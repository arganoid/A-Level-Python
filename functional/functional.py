import functools

# lambda function - shorthand for defining a simple function in one line
square = lambda x: x * x
cube = lambda x: x ** 3

# same as:
#def square(x):
#    return  x * x

print(square(3))

##############

myList = [76,7,1,4,5]

myList2 = list(map(cube, myList))
print(myList2)

##############

add = lambda x,y: x + y
total = functools.reduce( add, myList, 0 )
print(total)

##############

myFilteredList = list(filter( lambda x: x > 50, myList))
print(myFilteredList)

##############

# higher order function - takes a function as a parameter
do_something = lambda func, x: func(x)

# same as:
#def do_something(func, x):
#    return func(x)

print(do_something(square, 3))

##############

# In Python functions are first-class objects, which means you can assign them to a variable,
# pass them to a function and even return them from a function
def make_function():
    return lambda x: x * 100

my_function = make_function()
print(my_function(3))
