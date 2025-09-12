# 시간초과로 큐 알고리즘 적용
import sys
from collections import deque

# 입력 받기
N, K = map(int, sys.stdin.readline().split())
arr = []
initial_viruses = []

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if row[j] != 0:
            # 초기 바이러스 정보 저장 (바이러스 번호, 행, 열)
            initial_viruses.append((row[j], i, j))
    arr.append(row)

S, X, Y = map(int, sys.stdin.readline().split())

# delta - 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 오름차순 정렬
initial_viruses.sort()

# 큐에 초기 바이러스 정보 넣기: (바이러스 번호, 시간, 행, 열)
queue = deque()
for virus, r, c in initial_viruses:
    queue.append((virus, 0, r, c))

while queue:
    # 가장 왼쪽 팝하기
    virus, t, r, c = queue.popleft()

    # 목표 시간 S초가 되면 종료
    if t == S:
        break

    # 4방향으로 전파
    for i in range(4):
        n_row = r + dx[i]
        n_col = c + dy[i]

        # 범위 내에 있고 빈 칸인 경우
        if 0 <= n_row < N and 0 <= n_col < N:
            if arr[n_row][n_col] == 0:
                arr[n_row][n_col] = virus
                queue.append((virus, t+1, n_row, n_col))

if arr[X-1][Y-1] == 0:
    print(0)
else:
    print(arr[X-1][Y-1])