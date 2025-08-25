T = int(input())

for t in range(1, T + 1):
    # i can't use Korean now ..

    # receive str1, 2
    str1 = list(input())
    str2 = list(input())

    # init max
    max_value = 0

    # check count
    for check in str1:
        curr_cnt = str2.count(check)
        if max_value < curr_cnt:
            max_value = curr_cnt

    print(f"#{t}", max_value)