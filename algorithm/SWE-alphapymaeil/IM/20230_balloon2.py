import sys
sys.stdin = open('sample_in.txt')

T = int(input())

# make delta
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, T + 1):
    # arr size
    N = int(input())
    arr = []

    sum_list =[]

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # start from criteria location
    for row in range(N):
        for col in range(N):
            curr_sum = arr[row][col]
            # possible max dx, dy
            for re in range(1, N):
                # new delta
                n_dx = [re * i for i in dx]
                n_dy = [re * i for i in dy]
                # all direction (4)
                for idx in range(4):
                    n_row = row + n_dx[idx]
                    n_col = col + n_dy[idx]

                    # when be in possible range
                    if 0 <= n_row < N and 0 <= n_col < N:
                        curr_sum += arr[n_row][n_col]

            sum_list.append(curr_sum)

    print(f"#{t}", max(sum_list))



T = int(input())

# make delta
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, T + 1):
    # arr size
    N = int(input())
    arr = []

    sum_list =[]

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # start from criteria location
    for row in range(N):
        for col in range(N):
            curr_sum = arr[row][col]
            # possible max dx, dy
            for re in range(1, N):
                # new delta
                n_dx = [re * i for i in dx]
                n_dy = [re * i for i in dy]
                # all direction (4)
                for idx in range(4):
                    n_row = row + n_dx[idx]
                    n_col = col + n_dy[idx]

                    # when be in possible range
                    if 0 <= n_row < N and 0 <= n_col < N:
                        curr_sum += arr[n_row][n_col]

            sum_list.append(curr_sum)

    print(f"#{t}", max(sum_list))


