class ExampleClass:
    """"Example to demo instance variable"""

    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


obj1 = ExampleClass()
obj2 = ExampleClass(2)

obj2.set_second(3)

obj3 = ExampleClass(4)
obj3.third = 5

print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
