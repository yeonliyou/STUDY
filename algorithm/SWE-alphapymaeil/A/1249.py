import sys
from collections import deque
sys.stdin = open("1249_input.txt")

T = int(input())

# delta => 사람들 풀이 코멘트 보니까 '상하좌우' delta 설정보다 '하우좌상'이 더 빠름
# 실제로 제출했을때
# 상하좌우 : 메모리 63,232kb / 실행시간 165ms
# 하우좌상 : 메모리 64,128kb / 실행시간 154ms
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    # 큐 생성
    que = deque()
    # 시작점 추가
    que.append((0, 0))

    # 큐의 요소가 존재하는 동안 반복
    while que:
        # 큐의 왼쪽 좌표부터 빼오기
        r, c = que.popleft()

        # 현재 좌표로부터 4방향 탐색
        for direc in range(4):
            n_r = r + dx[direc]
            n_c = c + dy[direc]

            # 배열 내에 존재하는 좌표일 때
            if 0 <= n_r < N and 0 <= n_c < N:
                # 새로운 시간 = 그 전까지의 누적 공사시간(기록해놨던) + 새로 갱신된 좌표 공사시간
                new_time = dist[r][c] + arr[n_r][n_c]
                # 만약 새로 갱신된 공사 시간이 기존 갱신된 좌표의 원래 최소시간보다 작으면
                if new_time < dist[n_r][n_c]:
                    # 해당 자리까지의 최소 누적 공사시간 갱신해주기
                    dist[n_r][n_c] = new_time
                    # 새로 탐색할 좌표로 큐에 추가
                    que.append((n_r, n_c))

    # 행좌표 N-1, 열좌표 N-1까지의 최소 공사누적시간 반환
    return dist[N-1][N-1]

for C in range(1, T+1):
    N = int(input())

    # 배열 만들기
    arr = [list(map(int, input().strip())) for _ in range(N)]

    # 가중치 거리를 나타내는 배열 초기화
    dist = [[float('inf')]* N for _ in range(N)]
    dist[0][0] = arr[0][0]

    anw = bfs()

    print(f"#{C}", anw)
