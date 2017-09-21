import data_structures.profiler as profiler

# File named queuex to avoid clashing with built-in Python queue module

# Queue - can only add items to end and get/remove items from start

# From book:
# A queue is called a FIFO (first in first out) structure. A queue in a computer acts just like people queuing for a
# bus – the first person in the queue is going to be the first person to get on the bus and the first item of data to
# be put into the queue in a computer will be the first to be taken out.
# Reeves, Bob. AQA A level Computer Science (Kindle Locations 1807-1810). Hodder Education. Kindle Edition.

# In Python you can use a list as if it were a queue, eg:
#myList = []
#myList.append(1)
#myList.append(2)
#myList.append(3)
#print(myList.pop(0))    # myList.pop(0) returns and then deletes first item in list
#print(myList.pop(0))
#print(myList.pop(0))
# however, this is not efficient, as removing an item from the start of a list means Python will shift each item by one to the left


class EmptyError(Exception):
    pass

class FullError(Exception):
    pass


# This class works just like the code above but is more encapsulated
class Queue():
    def __init__(self):
        self.__list = []

    def push(self, value):
        self.__list.append(value)

    def pop(self):
        value = self.__list[0]
        del self.__list[0]      # still not very efficient, same reason as above
        return value



class ArrayLinearQueue:
    def __init__(self, capacity):
        self.__array = []
        for i in range(0,capacity):
            self.__array.append(0)
        self.capacity = capacity
        self.rear = -1

    def push(self, value):
        self.rear += 1
        self.__array[self.rear] = value

    def pop(self):
        value = self.__array[0]
        if self.rear <= -1:
            raise EmptyError
        for i in range(0,self.rear):
            self.__array[i] = self.__array[i+1]
        self.rear -= 1
        return value

class ArrayCircularQueue:
    def __init__(self, capacity):
        self.__array = []
        for i in range(0,capacity):
            self.__array.append(0)
        self.__capacity = capacity
        self.__front = 0
        self.__rear = -1
        self.__count = 0

    def push(self, value):
        if self.is_full():
            raise FullError
        self.__count += 1
        self.__rear += 1
        if self.__rear >= self.__capacity:
            self.__rear = 0
        self.__array[self.__rear] = value

    def pop(self):
        if self.is_empty():
            raise EmptyError
        value = self.__array[self.__front]
        self.__front += 1
        if self.__front >= self.__capacity:
            self.__front = 0
        self.__count -= 1
        return value

    def is_empty(self):
        return self.__count == 0

    def is_full(self):
        return self.__count >= self.__capacity

# Alternative way of checking empty/full
class ArrayCircularQueue2:
    def __init__(self, capacity):
        capacity += 1   # there will be one empty slot even in full queue
        self.__array = []
        for i in range(0,capacity):
            self.__array.append(0)
        self.__capacity = capacity
        self.__front = 0
        self.__rear = -1

    def push(self, value):
        if self.is_full():
            raise FullError
        self.__rear += 1
        if self.__rear >= self.__capacity:
            self.__rear = 0
        self.__array[self.__rear] = value

    def pop(self):
        if self.is_empty():
            raise EmptyError
        value = self.__array[self.__front]
        self.__front += 1
        if self.__front >= self.__capacity:
            self.__front = 0
        return value

    def is_empty(self):
        return self.__rear == (self.__front - 1) % self.__capacity

    def is_full(self):
        return self.__rear == (self.__front - 2) % self.__capacity

#myQueue = ArrayCircularQueue2(5)
#myQueue.push(1)
#print(myQueue.pop())
#print(myQueue.pop())
#print(myQueue.pop())

myQueue = ArrayCircularQueue2(10000)
p = profiler.Profiler()
for i in range(0,10000):
    myQueue.push(i)
print(p.get_seconds())

p = profiler.Profiler()
for i in range(0,10000):
    myQueue.pop()
print(p.get_seconds())

