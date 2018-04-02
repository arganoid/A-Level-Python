# Bubble sort is simple but very slow compared to other sorting algorithms
def bubble_sort(list, print_func, swap_animation = None):
    print_func(list, 0)
    steps = 0
    for i1 in range(0,len(list)-1):
        for i2 in range(0, len(list)-1):
            steps = steps + 1
            if list[i2] > list[i2+1]:
                if swap_animation != None:
                    swap_animation(list, i2, i2+1)
                temp = list[i2+1]
                list[i2+1] = list[i2]
                list[i2] = temp
            print_func(list, i2)

    print("Sorted in " + str(steps) + " steps")

# Bubble sort is simple but very slow compared to other sorting algorithms
def bubble_sort_optimised(list, print_func, swap_animation = None):
    print_func(list, 0)
    steps = 0
    anySwapsMade = True
    while anySwapsMade:
        anySwapsMade = False
        for i in range(0, len(list)-1):
            steps = steps + 1
            if list[i] > list[i+1]:
                if swap_animation != None:
                    swap_animation(list, i, i+1)
                temp = list[i+1]
                list[i+1] = list[i]
                list[i] = temp
                anySwapsMade = True
            print_func(list, i)

    print("Sorted in " + str(steps) + " steps")

# Merge sort is much faster than bubble sort (except maybe for very short lists) but uses more memory
def merge_sort(data_list, start, end, print_func):

    # we define a function within a function, the merge function can only be called within merge_sort
    # this can only be done in some languages. don't do it in pseudocode.
    def merge(data_list, start, middle, end, print_func):
        temp_list = list(data_list) # not efficient, we copy the entire list every time this function runs!
        i_data_list = start
        i_left = start
        i_right = middle + 1

        while i_left <= middle and i_right <= end:
            if temp_list[i_left] < temp_list[i_right]:
                data_list[i_data_list] = temp_list[i_left]
                i_left += 1
            else:
                data_list[i_data_list] = temp_list[i_right]
                i_right += 1
            i_data_list += 1

        # either the left or the right has run out of items, fill in the rest of the items from the other side
        if i_left <= middle:
            for i in range(i_left,middle+1):
                data_list[i_data_list] = temp_list[i]
                i_data_list += 1
        else:
            for i in range(i_right,end+1):
                data_list[i_data_list] = temp_list[i]
                i_data_list += 1

    if end > start:
        middle = int((start + end) / 2)
        merge_sort(data_list, start, middle, print_func)
        merge_sort(data_list, middle+1, end, print_func)
        merge(data_list, start, middle, end, print_func)
        print_func(data_list, middle)

# Insertion sort is faster than bubble sort (although still very
# poor for large arrays) and uses less memory than merge sort.
# Not required for AQA A-Level.
def insertion_sort(list, print_func, swap_animation = None):
    print_func(list, 0)
    for i1 in range(1,len(list)):
        i2 = i1
        while i2 > 0 and list[i2-1] > list[i2]:
            print_func(list, i2)
            if swap_animation != None:
                swap_animation(list, i2, i2 - 1)
            temp = list[i2 - 1]
            list[i2 - 1] = list[i2]
            list[i2] = temp
            i2 -= 1

def quick_sort(list, start, end, print_func, swap_animation = None):
    if start < end:
        p = quick_sort_partition(list, start, end, swap_animation)
        print_func(list, p)
        quick_sort(list, start, p, print_func)
        quick_sort(list, p + 1, end, print_func)


def quick_sort_partition(list, start, end, swap_animation = None):
    pivot = list[start]
    i = start - 1
    j = end + 1
    while True:
        i += 1
        while list[i] < pivot:
            i += 1

        j -= 1
        while list[j] > pivot:
            j -= 1

        if i >= j:
            return j

        if swap_animation != None:
            swap_animation(list, i, j)
        temp = list[i]
        list[i] = list[j]
        list[j] = temp

if __name__ == "__main__":
    #my_list = [5,1,2,9,8,1,4,3,5,0,7,3,1]
    my_list = [5,1,2,9]

    #bubble_sort(my_list, print)
    #merge_sort(my_list,0,len(my_list)-1, print)
    insertion_sort(my_list, print)
    #quick_sort(my_list,0,len(my_list)-1, print)

