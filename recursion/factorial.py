# Iterative and recursive implementations of factorial
# Need help understanding computer science and programming?
# Arganoid Tuition - https://tutor.arganoid.com/

import sys

# Allow very large results, in case you want to try calculating factorials of very large numbers!
sys.set_int_max_str_digits(6000000)

# Calculate factorial (eg 5! = 5 * 4 * 3 * 2 * 1) using a loop
def factorial_iterative(x):
    result = 1
    for i in range(2, x+1):     # 2nd range parameter not inclusive
        result *= i
    return result


# Here's another way of thinking of how to calculate factorials:
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1

# The following function qualifies as both recursive (because it calls itself)
# and functional (as there are no side effects)
def factorial_recursive(x):
    if x <= 1:
        # base case
        return x
    else:
        return x * factorial_recursive(x - 1)

print(factorial_iterative(5))
print(factorial_recursive(5))

