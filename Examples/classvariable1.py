class ExampleClass:
    """"Define Example class with one class variable"""

    varia = 1

    def __init__(self, val):
        ExampleClass.varia = val
        self.varia = val
        varia = val


print(ExampleClass.__dict__)

obj = ExampleClass(2)

print(ExampleClass.__dict__)
print(obj.__dict__)