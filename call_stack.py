# Intended to be run in a debugger so the student can see how the call stack changes as we enter and leave
# these functions. I typically teach this before recursion as it makes it easier to understand how the call stack works

def func1(x):
    x *= 10
    print("Func1: " + str(x))
    x = func2(x)
    print("Func1: " + str(x))
    return x

def func2(y):
    y *= 3
    print("Func2: " + str(y))
    y += func3(y)
    print("Func2: " + str(y))
    return y

def func3(z):
    z += 8
    print("Func3: " + str(z))
    return z


print(func1(1))
