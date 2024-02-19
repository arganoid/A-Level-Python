# Sorting algorithms taught in AQA A-level Computer Science:
# Bubble sort
# Merge sort
# Plus insertion sort and quick sort (not part of the AQA A-level syllabus)

# Need help understanding computer science and programming?
# Arganoid Tuition - https://tutor.arganoid.com/

import random
import time

# Bubble sort is simple but very slow compared to other sorting algorithms
def bubble_sort(l, print_func, swap_animation = None):
    print_func(l, 0)
    steps = 0
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            steps = steps + 1
            if l[j] > l[j + 1]:
                if swap_animation != None:
                    swap_animation(l, j, j + 1)

                # Swap items using a temporary variable
                # See bubble_sort_optimised below for an alternative way of doing this in Python
                temp = l[j + 1]
                l[j + 1] = l[j]
                l[j] = temp
            print_func(l, j)

    print("Sorted in " + str(steps) + " steps")

# Bubble sort is simple but very slow compared to other sorting algorithms
def bubble_sort_optimised(l, print_func, swap_animation = None):
    print_func(l, 0)
    steps = 0
    anySwapsMade = True
    while anySwapsMade:
        anySwapsMade = False
        for i in range(len(l) - 1):
            steps = steps + 1
            if l[i] > l[i + 1]:
                if swap_animation != None:
                    swap_animation(l, i, i + 1)

                # Swap elements - unlike most languages Python allows this kind of double assignment which removes
                # the need for a temporary variable.
                l[i + 1], l[i] = l[i], l[i + 1]

                anySwapsMade = True
            print_func(l, i)

    print("Sorted in " + str(steps) + " steps")

# Merge sort is much faster than bubble sort (except maybe for very short lists) but uses more memory
# Unlike the other algorithms in this file, this implementation of merge sort does not sort the list
# 'in-place' - i.e. the original list is not changed, instead it returns a new list
def merge_sort(sort_list):
    if len(sort_list) > 1:
        middle = len(sort_list) // 2

        # These lines use Python list slicing which lets you generate a new list by writing stuff like list_name[1:4]
        # to get all elements from indices 1 to 3
        left_elements = sort_list[:middle]  # gets all elements up to but not including middle
        right_elements = sort_list[middle:]  # gets all elements from middle onwards

        left_sorted = merge_sort(left_elements)
        right_sorted = merge_sort(right_elements)

        # Merge left and right lists into result list
        result_list = []
        pointer_left = 0
        pointer_right = 0
        # Keep going until both lists have been exhausted
        while pointer_left < len(left_sorted) or pointer_right < len(right_sorted):
            # If left list has been exhausted, take from right
            if pointer_left >= len(left_sorted):
                result_list.append(right_sorted[pointer_right])
                pointer_right += 1
            # Same but for if right list has been exhausted
            elif pointer_right >= len(right_sorted):
                result_list.append(left_sorted[pointer_left])
                pointer_left += 1
            # If both lists still have remaining elements, choose whichever element has the lowest value
            elif left_sorted[pointer_left] < right_sorted[pointer_right]:
                result_list.append(left_sorted[pointer_left])
                pointer_left += 1
            else:
                result_list.append(right_sorted[pointer_right])
                pointer_right += 1
        return result_list
    else:
        # List only contains 1 or 0 items, just return the list as it can be considered sorted
        return sort_list

# Insertion sort is faster than bubble sort (although still very
# poor for large arrays) and uses less memory than merge sort.
# Not required for AQA A-Level.
def insertion_sort(l, print_func, swap_animation = None):
    print_func(l, 0)
    for i in range(1, len(l)):
        j = i
        print_func(l, j)
        while j > 0 and l[j - 1] > l[j]:
            # Shift current item down until it reaches its correct position
            print_func(l, j)
            if swap_animation != None:
                swap_animation(l, j, j - 1)

            # Swap elements - Python allows this kind of double assignment which removes the need for a temporary variable
            l[j - 1], l[j] = l[j], l[j - 1]

            print_func(l, j)
            j -= 1

# This version is slightly faster as it reduces the number of assignments.
# No swap_animation parameter as won't work with visualisation as it currently stands
def insertion_sort_optimised(l, print_func):
    print_func(l, 0)
    for i in range(1, len(l)):
        j = i
        if l[j - 1] > l[j]:
            current = l[j]
            while j > 0 and l[j - 1] > current:
                # Shift current item down until it reaches its correct position
                print_func(l, i)
                l[j] = l[j - 1]
                j -= 1
            l[j] = current

# Not required for AQA A-level
def quick_sort(l, start, end, print_func, swap_animation = None):
    if start < end:
        pivot_index = quick_sort_partition(l, start, end, swap_animation)
        print_func(l, pivot_index)
        quick_sort(l, start, pivot_index, print_func)
        quick_sort(l, pivot_index + 1, end, print_func)

def quick_sort_partition(l, start, end, swap_animation = None):
    # Sort items in the given range to be either on the left or right side of a chosen pivot value. The index of
    # the pivot value may move during this function. The final index of the pivot is returned.
    # Choose middle element as partition. Any index can be chosen for the pivot but choosing the left-most index
    # leads to worst-case performance on already-sorted lists. For large lists, choosing the median of the start, pivot
    # and end values gives the best performance.
    pivot_value = l[(end + start) // 2]

    left = start
    right = end

    while True:
        while l[left] < pivot_value:
            left += 1

        while l[right] > pivot_value:
            right -= 1

        if left >= right:
            # Lower/higher values have now been partitioned either side of the pivot (which may itself have moved)
            return right

        if swap_animation != None:
            swap_animation(l, left, right)

        # Python swap shorthand, most other languages require a temporary variable
        l[left], l[right] = l[right], l[left]

        left += 1
        right -= 1


if __name__ == "__main__":
    #my_list = [5,1,2,9,8,1,4,3,5,0,7,3,1]
    #my_list = [5,1,2,9]

    # Create list of number from 0 to 9999 and shuffle them randomly
    my_list = [n for n in range(10000)]
    random.shuffle(my_list)

    # Begin timer
    start_time = time.perf_counter()

    # Change to True to use standard Python print as the print function for the sorting algorithms,
    # otherwise provide a print function that does nothing
    if False:
        print_func = print
    else:
        def print_func(*args):
            pass

    # In-place algorithms
    #bubble_sort(my_list, print_func)
    #bubble_sort_optimised(my_list, print_func)
    #insertion_sort(my_list, print_func)
    #insertion_sort_optimised(my_list, print_func)
    #quick_sort(my_list,0,len(my_list)-1, print_func)

    # Non in-place algorithms
    result = merge_sort(my_list)

    print(f"Finished in {time.perf_counter() - start_time} seconds")