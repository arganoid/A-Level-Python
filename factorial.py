
def factorialRecursive(x):
    if x <= 1:
        return x
    else:
       return x * factorialRecursive(x-1)

def factorialIterative(x):
    result = 1
    for i in range(2, x+1):     # range not inclusive
        result *= i
    return result

print(factorialIterative(50000))
#print(factorialRecursive(3))
