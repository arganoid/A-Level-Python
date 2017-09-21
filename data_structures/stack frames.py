def isEven(n):
    if n == 0:
        return True
    elif n == 1:
        return  False
    else:
        return  isEven(n-2)

print(isEven(50))





def test(y):
    x = 5
    print(y)

def test2():
    print("Hello")
    test(10)
    return "something"

def test3():
    mystring = test2()
    print(mystring)
    x = 100 * 100
    print(x)


test3()
