# 시간초과 버전
# 최악의 경우 연산 횟수 -> S * K * N * N
import sys
import copy

# 배열 크기, 바이러스 번호
N, K = map(int, sys.stdin.readline().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 몇 초가 될 때, 원하는 행/열 좌표
S, X, Y = map(int, sys.stdin.readline().split())

# delta
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시간 초기화
t = 0

# 경과 시간이 조건 시간 이하일 동안
while t < S:
    # 시간 1초 증가
    t += 1
    # 경과 시간만큼의 바이러스 번호까지만 활동
    for idx in range(1,K+1):
        temp_arr = copy.deepcopy(arr)
        # 모든 좌표 돌기
        for row in range(N):
            for col in range(N):
                # 첫번째 for문에서 순회하는 바이러스 번호라면
                if temp_arr[row][col] == idx:
                    # 상 하 좌 우 감염
                    for re in range(4):
                        n_row = row + dx[re]
                        n_col = col + dy[re]

                        # 배열 내에 존재하는 좌표일때만
                        if 0 <= n_row < N and 0<= n_col < N:
                            # 만약 빈칸이면 순회 바이러스 번호로 채워주기
                            if temp_arr[n_row][n_col] == 0:
                                arr[n_row][n_col] = idx

if arr[X-1][Y-1] == 0:
    print(0)
else:
    print(arr[X-1][Y-1])