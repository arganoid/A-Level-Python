import random

# Bubble sort is simple but very slow compared to other sorting algorithms
def bubble_sort(l, print_func, swap_animation = None):
    print_func(l, 0)
    steps = 0
    for i in range(0, len(l) - 1):
        for j in range(0, len(l) - 1):
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
        for i in range(0, len(l) - 1):
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
def merge_sort(l, start, end, print_func):

    # Here we define a function within a function. The merge function can only be called within merge_sort, and
    # it can access variables from the outer function - this makes it what's known as a 'closure' - although we
    # don't make use of outer variables in this case. This is an advanced topic not covered in the AQA A-level.
    def merge(left, right):
        merged = []
        i_left = 0
        i_right = 0

        while i_left < len(left) and i_right < len(right):
            if left[i_left] < right[i_right]:
                merged.append(left[i_left])
                i_left += 1
            else:
                merged.append(right[i_right])
                i_right += 1

        # Either the left or the right has run out of items, fill in the rest of the items from the other side
        if i_left < len(left):
            for i in range(i_left,len(left)):
                merged.append(left[i])
        else:
            for i in range(i_right,len(right)):
                merged.append(right[i])

        return merged

    if end > start:
        middle = (start + end) // 2
        left = merge_sort(l, start, middle, print_func)
        right = merge_sort(l, middle + 1, end, print_func)
        result = merge(left, right)
        print_func(result, middle)
        return result
    else:
        return [start]

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
    my_list = [5,1,2,9,8,1,4,3,5,0,7,3,1]
    #my_list = [5,1,2,9]
    #my_list = [n for n in range(100)]
    #random.shuffle(my_list)

    # In-place algorithms
    #bubble_sort(my_list, print)
    #insertion_sort(my_list, print)
    #insertion_sort_optimised(my_list, print)
    #quick_sort(my_list,0,len(my_list)-1, print)

    # Non in-place algorithms
    result = merge_sort(my_list,0,len(my_list)-1, print)

