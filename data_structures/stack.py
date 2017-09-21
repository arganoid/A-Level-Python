class EmptyError(Exception):
    pass

class FullError(Exception):
    pass


#myList = []
#myList.append(10)
#myList.append(20)
#myList.append(30)
#print(myList.pop(len(myList)-1))
#print(myList.pop(len(myList)-1))
#print(myList.pop(len(myList)-1))



# This class works just like the code above but is more encapsulated
class Stack():
    def __init__(self):
        self.__list = []

    def push(self, value):
        self.__list.append(value)

    def pop(self):
        value = self.__list[len(self.__list)-1]
        del self.__list[len(self.__list)-1]
        return value

myStack = Stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())




def create_array(capacity):
    array = []
    for i in range(0, capacity):
        array.append(0)
    return array

class ArrayStackDynamic():
    def __init__(self, capacity):
        self.__array = create_array(capacity)
        self.top = -1
        self.capacity = capacity

    def push(self, value):
        if self.top == self.capacity - 1:
            #raise FullError
            newArray = create_array(self.capacity*2)
            for i in range(0,self.capacity):
                newArray[i] = self.__array[i]
            self.__array = newArray
        self.top += 1
        self.__array[self.top] = value

    def pop(self):
        if self.top <= -1:
            raise EmptyError
        value = self.__array[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.top <= -1:
            raise EmptyError
        return self.__array[self.top]

myArrayStack = ArrayStackDynamic(10)
myArrayStack.push(10)
myArrayStack.push(20)
myArrayStack.push(30)
myArrayStack.push(40)
myArrayStack.push(50)
myArrayStack.push(60)
myArrayStack.push(70)
myArrayStack.push(80)
myArrayStack.push(90)
myArrayStack.push(100)
myArrayStack.push(110)
# print(myArrayStack.pop())
# print(myArrayStack.pop())
# print(myArrayStack.pop())
