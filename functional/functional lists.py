import functools

def head(l):
    return l[0]

def tail(l):
    return l[1:]

def is_empty(l):
    return len(l) == 0

def length(l):
    return len(l)


mylist = [2,5,3,6,4,8,9]

print(head(mylist))
print(tail(mylist))



def myReduce( func, list, value ):
    if is_empty(list):
        return value
    else:
        return myReduce( func, tail(list), func(value, head(list)) )

total2 = myReduce( lambda x,y: x + y, mylist, 0 )
print(total2)

