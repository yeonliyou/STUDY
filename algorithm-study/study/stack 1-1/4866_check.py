import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T + 1):
    check_str = input()

    # make stack
    stack = []

    # default
    result = 1

    # par pair dict
    par_dict = {')': '(', '}': '{'}

    # repeat check
    for str in check_str:
        # if str == '(' or '{'
        if str in par_dict.values():  # left par
            stack.append(str)  # add new element

        # if str == ')' or '}'
        elif str in par_dict.keys():  # right par
            # no element stack or no pair

            ###############################################
            ####### writing order very important^^ #########
            ##########   'A or B' => A, B order   ##########
            ###############################################
            if len(stack) == 0 or stack[-1] != par_dict[str]:
                result = 0
                break

            # when stack's last element == lef par
            else:
                stack.pop()  # remove last element


    # if there are elements
    if stack:
        result = 0

    # answer
    print(f"#{t}", result)