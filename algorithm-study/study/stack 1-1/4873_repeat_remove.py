import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T + 1):
    check_list = list(input())

    flag = True
    while flag == True:
        # flag init
        flag = False

        # remove repeated str
        for idx in range(0, len(check_list)-1):

            # if sequence str
            if check_list[idx] == check_list[idx + 1]:
                flag = True
                # remove them
                check_list.pop(idx)
                check_list.pop(idx)  # because index counts -1
                break  # after removing, break ! (important)
            else:
                continue


    print(f"#{t}", len(check_list))




