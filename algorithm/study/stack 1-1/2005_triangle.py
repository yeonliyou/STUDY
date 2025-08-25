import sys
#sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = []

    # row number = row's number counts
    for row in range(N):
        # first number is always 1
        sample_list = [1]

        if row >= 1:
            # fill numbers between 1
            for col in range(1, row):
                # before row's two element sum
                sample_list.append(arr[row-1][col-1] + arr[row-1][col])

            # last number is always 1 too
            sample_list.append(1)

        arr.append(sample_list)

    print(f"#{t}")
    # print each line
    for anw in arr:
        print(*anw)