import sys
from collections import deque
sys.stdin = open("1868_input.txt")

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

# 주변 지뢰 개수 세기
def count_mines(arr, r, c, N):
    cnt = 0
    for i in range(8):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '*':
            cnt += 1
    return cnt

# BFS로 0 구역 확장
def bfs(arr, visited, r, c, N):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        cr, cc = q.popleft()
        mine_cnt = count_mines(arr, cr, cc, N)

        # 주변 지뢰가 없으면 → 인접칸 열어줌
        if mine_cnt == 0:
            for i in range(8):
                nr, nc = cr + dx[i], cc + dy[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if not visited[nr][nc] and arr[nr][nc] == '.':
                        visited[nr][nc] = True
                        q.append((nr, nc))
        # 지뢰가 있으면 그냥 숫자 표시만 (visited만 True면 충분)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    clicks = 0

    # 1단계: 0인 칸 BFS (연쇄적으로 열림)
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '.' and not visited[r][c]:
                if count_mines(arr, r, c, N) == 0:
                    bfs(arr, visited, r, c, N)
                    clicks += 1

    # 2단계: 남은 '.' (숫자칸)은 각각 클릭
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                clicks += 1

    print(f"#{tc} {clicks}")
