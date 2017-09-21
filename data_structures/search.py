import data_structures.profiler as profiler
import random

my_list = []
for i in range(0, 10000000):
    my_list.append(random.randint(-2000000000, 200000000))

my_list.sort()

# Returns index of item, if not present returns -1
def linear_search(list, item):
    for i in range(0,len(list)):
        if list[i] == item:
            return i

    # Not found
    return -1

# Returns index of item, if not present returns -1. List must be sorted.
def binary_search(list, item):
    steps = 0
    start = 0
    end = len(list) - 1
    i = (end + start) // 2
    while list[i] != item and end > start:  # AQA book is wrong! it effectively says end != start - that won't work for lists with odd number of items (TODO CONFIRM)
        i = (end + start) // 2
        if list[i] < item:
            start = i + 1
        elif list[i] > item:
            end = i - 1
        steps += 1

    print(steps)

    if list[i] == item:
        return i
    else:
        return -1

p = profiler.Profiler()
print(binary_search(my_list,1))
print(p.get_seconds())
