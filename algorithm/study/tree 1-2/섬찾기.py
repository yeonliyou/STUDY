import sys
sys.stdin = open('input.txt')

# 행, 열 크기
N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, list(input()))))


# 방문 여부 체크 배열 만들기
visited = []
for _ in range(N):
    visited.append([0 for _ in range(M)])

# 상, 하, 좌, 우, 왼대각위, 오대각위, 왼대각아래, 오대각아래
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

# 섬의 개수 초기화
anw = 0

def dfs(r, c):
    global anw, visited, arr

    # 8가지 방향 체크
    for idx in range(8):
        n_r = r + dx[idx]
        n_c = c + dy[idx]

        # 배열 내 존재 좌표이고 and 방문한 적 없고 and 배열 요소가 1일때
        if (0 <= n_r < N and 0 <= n_c < M and visited[n_r][n_c] == 0
            and arr[n_r][n_c] == 1):
            visited[n_r][n_c] = 1
            dfs(n_r, n_c)


for r in range(N):
    for c in range(M):

        # 첫 출발 지점이 1인데 방문한적 없는 경우에만 체크 시작
        if arr[r][c] == 1 and visited[r][c] == 0:
            # 섬의 개수
            anw += 1
            visited[r][c] = 1
            dfs(r, c)

print(anw)


