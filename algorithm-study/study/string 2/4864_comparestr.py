T = int(input())

for t in range(1, T + 1):
    # i can't use Korean now ..
    str1 = input()
    str2 = input()

    flag = 0

    # repeat for finding str1
    str1_length = len(str1)

    # until possible length
    for idx in range(len(str2) - str1_length + 1):
        # as long as str len
        if str2[idx : idx+str1_length] == str1:
            flag = 1
        else:
            continue

    print(f"#{t}", flag)