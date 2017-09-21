import math
import itertools

# A set is an unordered collection of values in which each value occurs at most once.
# Several languages support set construction. In Python, for example, use of curly braces constructs a set: {1, 2, 3}

# From Python docs:
# Python also includes a data type for sets. A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical
# operations like union, intersection, difference, and symmetric difference.
# Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(),
# not {}; the latter creates an empty dictionary

emptySet = set()  # empty set - don't use {} - that creates an empty dictionary
mySet = { 1, 2, 3 }
mySet2 = set( [1,2,3] )     # same as above but uses a list to initialise the set

# Set comprehension (mathematical form):
# A = {x | x ∈ ℕ ∧ x ≥ 1}
# where A is the set consisting of those objects x such that x ∈ ℕ and x ≥ 1 is true.
# | means such that.
# x ∈ ℕ means that x is a member of the set ℕ consisting of the natural numbers, ie {0, 1, 2, 3, 4, …}.

# In Python, set comprehension can be done like this:
mySet3 = { x * 2 for x in { 1, 2, 3 } }   # This is said to be a set comprehension over the set {1, 2, 3 }
mySet4 = { x * 2 for x in range(0,10) }   # This is said to be a set comprehension over the set {0, 2, 4, 6, 8, ..., 18 }
mySet5 = { x for x in range(0,10) if x > 3 }   # { 4,5,6,7,8,9 }
mySet6 = set()  # empty set - don't use {}

# how to make an infinite set? (probably a bad idea)
#mySet7 = { x for x in range(0,int(math.inf))}
#mySet7 = { x for x in itertools.count(0,1) }

print(mySet)
print(mySet2)
print(mySet3)
print(mySet4)
print(mySet5)
print(mySet6)

mySet5.add(100)
print(mySet5)

mySet5.remove(7)
print(mySet5)

print(2 in mySet)   # how to tell if something is in a set
print (2 in mySet5)

