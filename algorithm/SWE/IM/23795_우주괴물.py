#import sys
#sys.stdin = open('sample_in.txt')

T = int(input())

# delta 만들기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, T + 1):
    # 배열 크기
    N = int(input())

    # 배열 만들기
    arr = []
    # 배열 만들면서 벽이 없는 빈칸(0)의 개수 바로 구하기
    total_empty = 0
    for curr_row in range(N):
        sample = list(map(int, input().split()))
        total_empty += sample.count(0)  # 0의 개수 더하기
        arr.append(sample)

        # 괴물이 있는 위치 갱신
        if 2 in sample:
            row = curr_row
            col = sample.index(2)
    
    # 현재 좌표를 기준으로 빈칸 개수 초기화
    meet_line = 0

    # 상, 하, 좌, 우 방향 반복
    for idx in range(4):

        # 어디까지 직진할 건지
        for go in range(1, N):
            # 새로운 델타 갱신
            n_dx = [i * go for i in dx]
            n_dy = [i * go for i in dy]

            # 체크할 행, 열 좌표 갱신
            n_row = row + n_dx[idx]
            n_col = col + n_dy[idx]

            # 새로 갱신한 좌표가 배열 내의 좌표면서, 벽이 아닐때
            if (0 <= n_row < N) and (0 <= n_col < N) and arr[n_row][n_col] != 1:
                meet_line += 1  # 광선 닿은 빈칸 +1
            else:
                break

    print(f"#{t}", total_empty - meet_line)  # 총 빈칸 - 광선이 닿은 빈칸






