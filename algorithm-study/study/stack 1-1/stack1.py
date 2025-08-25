# make a stack
stack = []

# add data
stack.append("A")
stack.append("B")
stack.append("C")

for _ in range(3):
    print(stack[-1])
    stack.pop()


