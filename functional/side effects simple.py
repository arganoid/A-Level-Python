global_variable = 0

def do_calculation(x):
    return x * 3 + global_variable

print(do_calculation(10))   # returns 30

global_variable = 5

print(do_calculation(10))   # returns 35 - same function call with same parameter gave a different result.
                            # If we were working under the functional programming paradigm, this kind of thing
                            # should not be able to happen.
