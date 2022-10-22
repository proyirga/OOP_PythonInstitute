class Stack:
    """"Define a class called stack"""

    def __init__(self):
        """"Constructor function definition"""
        self.__stack_list = []

    def push(self, val):  # a method to push element to a stack
        self.__stack_list.append(val)

    def pop(self):  # a method to pop an element from a stack
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    """"Define a subclass of Stack with additional properties
    of adding values in a stack
    we want the push method not only to push the value onto the stack but also
    to add the value to the sum variable;
    we want the pop function not only to pop the value off the stack but also
    to subtract the value from the sum variable.
    """

    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):  # Adds a value to sum
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum


class CountStack(AddingStack):
    """"Define a subclass of stack with additional properties
    to count number of elements of the stack
    """

    def __init__(self):
        AddingStack.__init__(self)
        self.__counter = 0

    def push(self, val):
        AddingStack.push(self, val)
        self.__counter += 1

    def pop(self):
        AddingStack.pop(self)
        self.__counter -= 1

    def get_counter(self):
        return self.__counter


obj = CountStack()
obj.push(10)
print("Number of elements in the stack {}".format(obj.get_counter()))
print("SUM: {}".format(obj.get_sum()))
obj.push(10)
print("Number of elements in the stack {}".format(obj.get_counter()))
print("SUM: {}".format(obj.get_sum()))
obj.push(10)
print("Number of elements in the stack {}".format(obj.get_counter()))
print("SUM: {}".format(obj.get_sum()))

obj.pop()
print("Number of elements in the stack {}".format(obj.get_counter()))
print("SUM: {}".format(obj.get_sum()))
obj.pop()
print("Number of elements in the stack {}".format(obj.get_counter()))
print("SUM: {}".format(obj.get_sum()))