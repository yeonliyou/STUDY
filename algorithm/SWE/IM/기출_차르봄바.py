import sys
sys.stdin = open('input.txt')

T = int(input())

# 상, 하, 좌, 우 델타 만들기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, T+1):
    # 격자 크기 (행, 열)
    N, M = map(int, input().split())

    # 배열 만들기
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    max_pang = 0

    # 배열 한 칸씩 돌면서 경비병의 눈을 피할 수 있는 곳 찾기
    for row in range(N):
        for col in range(M):
            # 폭발 수 초기화
            pang_cnt = arr[row][col]

            # 상하좌우 방향 4번 체크
            for idx in range(4):

                # 가능한 범위까지 계속 칸을 전진하면서 벽 or 경비병 여부 체크
                for up in range(1, arr[row][col]+1):
                    # 전진으로 갱신한 행열 좌표
                    n_row = row + dx[idx] * up
                    n_col = col + dy[idx] * up

                    # 갱신한 좌표가 배열 내에 존재하는 좌표라면
                    if 0 <= n_row < N and 0 <= n_col < M:
                        pang_cnt += arr[n_row][n_col]

            if pang_cnt > max_pang:
                max_pang = pang_cnt

    print(f"#{t}", max_pang)