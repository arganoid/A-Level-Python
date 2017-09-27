import math

def mean(list):
    total = 0
    for n in list:
        total += n
    return total / len(list)

def median(list):
    if len(list) % 2 == 1:
        middle = (len(list)-1) // 2
        return list[middle]
    else:
        middle = (len(list) - 1) / 2
        return (list[math.floor(middle)] + list[math.ceil(middle)]) / 2

def mode(list):
    counts = {}
    for n in list:
        if not n in counts:
            counts[n] = 1
        else:
            counts[n] += 1

    highestN = -1
    highestAmount = -1

    for n in counts.keys():
        if counts[n] > highestAmount:
            highestAmount = counts[n]
            highestN = n

    return highestN