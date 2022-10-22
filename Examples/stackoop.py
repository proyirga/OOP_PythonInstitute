class Stack:
    """"Implementing stack with oop"""

    def __init__(self):
        """"Define the constructor function
        it makes sure that each objects have its own instantiation
        """
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_obj = Stack()
stack_obj.push(1)
stack_obj.push(2)

#print(len(stack_obj.__stack_list))

print(stack_obj.pop())
print(stack_obj.pop())