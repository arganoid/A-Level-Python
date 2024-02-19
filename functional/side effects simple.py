global_variable = 0

def do_calculation(x):
    global global_variable
    global_variable += 1
    return x * 3 + global_variable

print(do_calculation(10))   # returns 31

print(do_calculation(10))   # returns 32 - same function call with same parameter gave a different result.
                            # If we were working under the functional programming paradigm, this kind of thing
                            # should not be able to happen.
