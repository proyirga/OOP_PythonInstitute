stack = []

def push(val):
    stack.append(val)

def pop():
    try:
        val = stack[-1]
        del stack[-1]
        return val
    except IndexError:
        print("No element to remove")



push(1)
push(2)
push(3)

print(stack)

print(pop())
print(stack)

print(pop())
print(stack)

print(pop())
print(stack)

print(pop())
print(stack)