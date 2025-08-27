import sys

sys.stdin = open("2105_input.txt")

T = int(input())

for t in range(1, T+1):
    # 배열 크기
    N = int(input())
    arr = []

    # 배열 생성
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # delta : 오른쪽 아래 대각선(0), 왼쪽 아래 대각선(1), 왼쪽 위 대각선(2), 오른쪽 위 대각선(3)
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    # 답
    anw = -1

    # 배열 순회
    # 출발 지점
    for row in range(N):
        for col in range(N):
            # 시작 지점 저장
            start_row, start_col = row, col

            # 시계방향 회전 순서 (회전횟수)
            turn = 0

            # 전진횟수 = 먹은 디저트 수 - 1
            go = 0

            # 먹은 디저트 종류 (처음꺼 먹고 시작) - 방문 여부 체크 가능
            eaten = [arr[row][col]]

            def dfs(row, col, turn, go):
                global anw

                # 만약 회전을 3번보다 적게 했다면 이제 갈 수 있는 경우의 수 => 2가지(직전에 가던 방향, 오른쪽 회전 방향)
                if turn < 3:
                    # 갈 수 있는 방향 만큼 탐색
                    for idx in [turn, (turn + 1) % 4]:
                        n_row = row + dx[idx]
                        n_col = col + dy[idx]

                        # 배열 내 존재하는 좌표이고 and 먹지 않은 디저트여야 함
                        if (0 <= n_row < N and 0 <= n_col < N) and arr[n_row][n_col] not in eaten:
                            eaten.append(arr[n_row][n_col])
                            dfs(n_row, n_col, idx , go + 1)
                            # 백트래킹
                            eaten.pop()

                        else:
                            continue

                # 만약 회전을 3번 했다면 (돌아가야 가능한 것임)
                elif turn == 3:
                    n_row = row + dx[turn]
                    n_col = col + dy[turn]

                    # 만약 처음 지점으로 돌아오고 and go가 1 이상이라면
                    if n_row == start_row and n_col == start_col:
                        # 만약 먹은 디저트 수가 기존 값보다 크다면
                        if go + 1 > anw:
                            anw = go + 1

                    # 배열 내 존재하는 좌표이고 and 먹지 않은 디저트여야 함
                    if (0 <= n_row < N and 0 <= n_col < N) and arr[n_row][n_col] not in eaten:
                        eaten.append(arr[n_row][n_col])
                        dfs(n_row, n_col, turn , go + 1)
                        # 백트래킹
                        eaten.pop()

                    else:
                        return


            dfs(row, col, turn, go)

    print(f"#{t}",anw)






