# Calculate factorial (eg 5! = 5 * 4 * 3 * 2 * 1) using a loop
def factorialIterative(x):
    result = 1
    for i in range(2, x+1):     # 2nd range parameter not inclusive
        result *= i
    return result


# Here's another way of thinking of how to calculate factorials:
# 5!
# 5 * 4!
# 4 * 3!
# 3 * 2!
# 2 * 1!
# 1! = 1

# The following function qualifies as both recursive and functional
def factorialRecursive(x):
    if x <= 1:
        return x
    else:
       return x * factorialRecursive(x-1)

print(factorialIterative(5))
print(factorialRecursive(5))
