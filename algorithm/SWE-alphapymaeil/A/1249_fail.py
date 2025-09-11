import sys
sys.stdin = open("1249_input.txt")

T = int(input())

# delta : 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# dfs 함수
def dfs(r, c, curr_time, visited):
    global anw, arr

    # 만약 기존의 최소 공사 시간보다 지금 탐색 시간의 합이 더 크면 조기 종료
    # * 근데 이 논리구조를 다시 생각해보면 그 전 기록보다 큰 경우 멈추는게 더 합리적임
    # * 100000이라는 초기 값을 넘기는 쉽지 않기 때문에 사실 조기종료 역할을 제대로 못함
    if curr_time > anw:
        return

    # G에 도착했다면
    if r == N-1 and c == N-1:
        anw = curr_time
        return

    # 상하좌우 방향 탐색
    for direc in range(4):
        n_r = r + dx[direc]
        n_c = c + dy[direc]

        # 배열 내 존재좌표이고
        if 0 <= n_r < N and 0 <= n_c < N:
            # 방문한적이 없다면
            if visited[n_r][n_c] == 0:

                # 방문 처리 해주기
                visited[n_r][n_c] = 1

                dfs(n_r, n_c, curr_time + arr[n_r][n_c], visited)

                # 백트래킹
                visited[n_r][n_c] = 0

for C in range(1, T+1):
    # 지도의 크기 nxn
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip())))

    # 답 초기화
    anw = 100000

    # 방문 확인 여부
    visited = []
    for _ in range(N):
        visited.append([0 for _ in range(N)])

    dfs(0, 0, 0, visited)

    print(f"#{C}", anw)