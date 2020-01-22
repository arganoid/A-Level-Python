import math
x = ((2*3) + ((5**200) / (3.5 ** 50.2)) - 3) + (math.sqrt(8**200) + math.sqrt(math.sin(5**10)))
print(x)

# Imagine running this code on a computer which has an extremely slow CPU, but the CPU has four cores.
# Let's say that each power calculation (e.g. 5 ** 200) takes 10 seconds. Because each of the power calculations
# is independent of the others, they could theoretically be run concurrently (i.e. at the same time).
