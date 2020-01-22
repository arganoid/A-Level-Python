# https://www.pydanny.com/python-partials-are-fun.html

from functools import partial

def power(base, exponent):
    return base ** exponent

# Now what if we want to have dedicated square and cube functions that
# leverage the power() function? Of course, we can do it thus:

# def square(base):
#     return power(base, 2)
#
# def cube(base):
#     return power(base, 3)
#
# print(square(2))
# print(cube(2))



# This works, but what if we want to create 15 or 20 variations of our power() function? What about 1000 of them?
# Writing that much repetitive code is, needless to say, annoying. This is where partials come into play.
# Let's rewrite our square and cube functions using partials

square = partial(power, exponent=2)
#cube = partial(power, exponent=3)

print(square(2))
#print(cube(2))


power_functions = []
for i in range(0,100):
    power_functions.append( partial(power, exponent=i) )

print(power_functions[99](3))


def get_power_function(exponent):
    return lambda x: x ** exponent

cube = get_power_function(3)
print(cube(7))
