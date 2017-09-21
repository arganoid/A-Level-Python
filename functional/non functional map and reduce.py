def map_nonfunctional(func, list):
    newlist = []
    for item in list:
        newvalue = func(item)
        newlist.append(newvalue)
    return newlist

def square(n):
    return n * n


print(map_nonfunctional(square, [1,2,3,4,5]))


def reduce_nonfunctional(func, list, value):
    for item in list:
        value = func(value, item)
    return  value


myList = [76,7,1,4,5]

total = reduce_nonfunctional( lambda x,y: x + y, myList, 0 )
print(total)
