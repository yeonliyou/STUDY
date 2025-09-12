import sys
from collections import deque
sys.stdin = open("1953_input.txt")

T = int(input())

# 상(0), 하(1), 좌(2), 우(3)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 배수구 모양별 가능한 통로 모음
direc_info = [0, [0,1,2,3], [0,1], [2,3], [0,3], [1,3], [1,2], [0,2]]

# 배수구가 서로 이어질 수 있는지를 체크하기 위한 페어쌍
pair_dict = {0:1, 1:0, 2:3, 3:2}

for t in range(1, T+1):
    # 행,열 크기 / 맨홀 뚜껑 행, 열 좌표 / 소요시간
    N, M, R, C, L= map(int, input().split())

    # 배수구 정보 배열
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))

    # 답 초기화
    anw = 1  # 맨홀 뚜껑 위치부터 포함

    # 큐 생성
    queue = deque()
    queue.append((R, C, 1))

    # 방문 여부 파악 배열
    visited_arr = []
    for _ in range(N):
        visited_arr.append([0 for _ in range(M)])

    # 맨홀 위치는 이미 방문함
    visited_arr[R][C] = 1

    # 큐가 비어있지 않는 동안 반복
    while queue:
        # 새로운 갱신 값
        R, C, time = queue.popleft()

        # 시간이 다 됐으면 종료
        if time == L:
            break

        # 해당 배수구관 모양에 따른 이동 가능 방향 저장
        possible_direc = direc_info[arr[R][C]]

        for idx in possible_direc:
            n_r = R + dx[idx]
            n_c = C + dy[idx]

            # 1. 존재하는 좌표여야 하고
            # 2. 배수구관이 있는 좌표여야 하고
            # 3. 서로 이어지는 방향이어야 하고
            # 4. 방문한적 없는 곳이어야함
            if ((0 <= n_r < N) and (0 <= n_c < M) and
                (arr[n_r][n_c] != 0 ) and
                (pair_dict[idx] in direc_info[arr[n_r][n_c]]) and
                (visited_arr[n_r][n_c] == 0)):

                anw += 1
                visited_arr[n_r][n_c] = 1
                queue.append((n_r, n_c, time + 1))

    print(f"#{t}", anw)











