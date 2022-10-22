class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    """"A function that gets an object of any class,
    scans its contents in order to find all integer
    attributes with names starting with i,
    and increments them by one.
    """
    for name in obj.__dict__.keys(): # loop scans the object
        if name.startswith('i'):  # check if a name starts with i is found
            val = getattr(obj, name)  # passes the attribute name starts with i to val
            if isinstance(val, int):  # checks if the attribute starts with i is an int
                setattr(obj, name, val + 1)  # increment attributes starts with i by 1


print(obj.__dict__)
incIntsI(obj)  # invoke the function to increment attributes starts with i by 1
print(obj.__dict__)