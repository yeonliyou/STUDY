import sys
from collections import deque

sys.stdin = open("test.txt")

T = int(input())

for t in range(1, T+1):
    # 배열 크기
    N = int(input())
    arr = []

    # 배열 생성
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 방향키 delta : 오른쪽 위 대각선, 오른쪽 아래 대각선, ,  왼쪽 아래 대각선, 왼쪽위 대각선
    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1]

    # 답 초기화
    anw = -1

    # 모든 좌표 돌기
    for row in range(N):
        for col in range(N):

            # 먹은 디저트 종류 기록 초기화 (시작점 먹고 출발)
            eaten = [arr[row][col]]

            # 시계방향 꺾음 확인 변수
            turn = 0

            # 방향 조작하는 용도의 stack 초기화
            stack = []

            # 현재 체크하는 행, 열, 직전 방향, 턴 누적 횟수
            def dfs(n_row, n_col, pre_dir, turn):

                # 만약 배열 내에 존재하는 좌표가 아니면
                if not (0 <= n_row < N and 0 <= n_col < N):
                    return

                # 이미 먹은 디저트 종류면
                if arr[n_row][n_col] in eaten:
                    return

                # 1. 사용한 방향이 1개라면 (아직 꺾은 적이 없다면)
                if turn == 0:
                    # 이전 방향, turn 방향 두개만 가능
                    for idx in [pre_dir, (pre_dir+1) % 4]:
                        if idx != pre_dir:
                            turn += 1
                        eaten.append(arr[n_row][n_col])
                        dfs(n_row, n_col, idx, turn)
                        # 백트래킹
                        eaten.pop()

                # 2. 사용한 방향이 2개라면
                elif turn == 1:
                    # 첫번째로 가던 방향이랑 pair 방향 같을때 or 직전 방향이랑 같을 때만 진행
                    if stack[-1] == idx or stack[0] == pair[idx]:
                        eaten.append(arr[n_row][n_col])
                        dfs(n_row, n_col, idx)
                        # 백트래킹
                        eaten.pop()

                # 4. 사용한 방향이 3개 이상이라면 (pair를 맞춰서 돌아가야 하는 경우임)
                elif used_direc.count(0) <= 1:
                    # pair를 다 맞추었다면 (스택이 비어있다면)
                    if not stack:
                        if len(eaten) > anw:
                            anw = len(eaten)
                            return
                    # 첫번째로 가던 방향이랑 현재 가는 방향이랑 갯수가 일치할때까지 (pair) 개수 맞추기
                    elif stack[-1] == pair[idx]:
                        # 더이상 짝꿍을 못 맞출때까지
                        while stack[-1] != pair[idx]:
                            used_direc[idx] += 1
                            eaten.append(arr[n_row][n_col])
                            stack.pop(0)
                            stack.pop(-1)

                        dfs(n_row, n_col, idx)
                        # 짝꿍 맞춘 만큼 백트래킹
                        for _ in range(used_direc[idx]-1):
                            eaten.pop()

                    # 만약 pair를 못 맞추면 함수 종료
                    else:
                        return

            # 기준 점으로부터 네가지 방향 체크 (각 방향에서 시계방향으로만 진행)
            for idx in range(4):
                n_row = row + dx[idx]
                n_col = col + dy[idx]

                # 함수 시작
                dfs(n_row, n_col, idx, 0)

    print(f"#{t}", anw)
