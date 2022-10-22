class ExampleClass:
    """"Define Example class to demo class variable"""

    counter = 0

    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


obj1 = ExampleClass()
obj2 = ExampleClass(2)
obj3 = ExampleClass(4)

print(obj1.__dict__, obj1.counter)
print(obj2.__dict__, obj2.counter)
print(obj3.__dict__, obj3.counter)