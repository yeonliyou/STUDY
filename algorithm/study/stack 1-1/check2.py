# make stack
stack = []

# input str
check_str = input()

# par pair list
par_list = ['(', ')']

# repeat check
for str in check_str:
    # if left par
    if len(stack) == 0 or str == par_list[0]:
        stack.append(str)
    # if right par
    elif par_list[0] == stack[-1]:  # if stack's last ele = left par
        stack.pop()

# answer
if len(stack) == 0:
    print('Pass')
else:
    print('Fail')


