# Linear and binary search, as taught in AQA A-level Computer Science

# Need help understanding computer science and programming?
# Arganoid Tuition - https://tutor.arganoid.com/

import profiler
import random

# Returns index of item, if not present returns -1
def linear_search(l, item_searched_for):
    for i in range(0,len(l)):
        if l[i] == item_searched_for:
            return i

    # Not found
    return -1

# List must be sorted. Returns index of item, if not present returns -1. Second return value is number of steps taken.
def binary_search(l, item_searched_for):
    steps = 0
    start = 0
    end = len(l) - 1
    mid = (end + start) // 2
    while l[mid] != item_searched_for and end > start:  # AQA book is wrong! It effectively says end != start - that won't work for lists with odd number of items (TODO CONFIRM)
        mid = (end + start) // 2
        if l[mid] < item_searched_for:
            # Item can't be in the first half of the part of the list we're looking at
            start = mid + 1
        elif l[mid] > item_searched_for:
            # Item can't be in the second half of the part of the list we're looking at
            end = mid - 1
        steps += 1

    if l[mid] == item_searched_for:
        return mid, steps
    else:
        return -1, steps

if __name__ == '__main__':
    my_list = []

    p = profiler.Profiler()
    for i in range(0, 10000000):
        my_list.append(random.randint(-4e9, 4e9))       # 4e9 = 4 * 10^9 i.e. 4 billion
    print("List add time: " + str(p.get_seconds()))

    p = profiler.Profiler()
    my_list.sort()
    print("Sort time: " + str(p.get_seconds()))

    p = profiler.Profiler()
    result = linear_search(my_list, 1)
    print("Linear search time: " + str(p.get_seconds()))
    print("Linear search result: " + str(result))

    p = profiler.Profiler()
    result, steps = binary_search(my_list,1)
    print("Binary search time: " + str(p.get_seconds()))
    print("Binary search result: " + str(result))
    print("Binary search steps: " + str(steps))
