import random
import queue

class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class ArrayPriorityQueueOld:
    def __init__(self, capacity):
        self.__array = []
        for i in range(0,capacity):
            self.__array.append(0)
        self.__capacity = capacity
        self.__rear = -1

    def push(self, value, priority):
        self.__rear += 1
        self.__array[self.__rear] = [value, priority]

    def pop(self):
        value = self.__array[0][0]
        if self.__rear <= -1:
            raise IndexError
        for i in range(0, self.__rear):
            self.__array[i] = self.__array[i+1]
        self.__rear -= 1
        return value

    def get_array(self):
        return self.__array

class ArrayPriorityQueue1:
    def __init__(self, capacity):
        self.__array = []
        for i in range(0,capacity):
            self.__array.append(0)
        self.__capacity = capacity
        self.__rear = -1

    def push(self, value, priority):
        slot = 0
        if not self.is_empty():
            # Find last item with same or higher (lower in numerical terms) priority
            last_same_or_lower = -1
            for i in range(0, self.__rear+1):
                if self.__array[i][1] <= priority:
                    last_same_or_lower = i
            slot = last_same_or_lower + 1
            # shift everything after that to the right by one
            for i in range(self.__rear, last_same_or_lower, -1):
                self.__array[i+1] = self.__array[i]
        self.__rear += 1
        self.__array[slot] = [value, priority]

    def pop(self):
        value = self.__array[0][0]
        if self.is_empty():
            raise EmptyError
        for i in range(0, self.__rear):
            self.__array[i] = self.__array[i+1]
        self.__rear -= 1
        return value

    def is_empty(self):
        return self.__rear == -1

    def is_full(self):
        return self.__rear >= self.__capacity - 1

    def get_array(self):
        return self.__array

class ArrayPriorityQueue2:
    def __init__(self, capacity):
        self.__array = []
        for i in range(0,capacity):
            self.__array.append(0)
        self.__capacity = capacity
        self.__rear = -1

    def push(self, value, priority):
        self.__rear += 1
        self.__array[self.__rear] = [value, priority]

    def pop(self):
        if self.is_empty():
            raise EmptyError

        # Find first highest priority item and store its index
        highest_priority = -1
        highest_priority_index = -1
        for i in range(0, self.__rear+1):
            if highest_priority == -1 or self.__array[i][1] < highest_priority:
                highest_priority = self.__array[i][1]
                highest_priority_index = i

        value = self.__array[highest_priority_index][0]

        for i in range(highest_priority_index, self.__rear):
            self.__array[i] = self.__array[i+1]

        self.__rear -= 1
        return value

    def is_empty(self):
        return self.__rear == -1

    def is_full(self):
        return self.__rear >= self.__capacity - 1

    def get_array(self):
        return self.__array

numbers = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
numberCounts = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
size = 50
myQueue = ArrayPriorityQueue2(size)

for i in range(0,size):
    n = random.randint(0,9)
    numberCounts[n] += 1
    myQueue.push(numbers[n] + str(numberCounts[n]), n)

for i in range(0,size):
    print(myQueue.pop())
