import sys

sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    # 배열 크기
    N = int(input())
    arr = []

    # 배열 생성
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 방향키 delta : 왼쪽위 대각선, 오른쪽 위 대각선, 왼쪽 아래 대각선, 오른쪽 아래 대각선
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    # 방향 짝꿍 만들기
    # idx = 0, 1, 2, 3
    pair = [3, 2, 1, 0]

    # 답 초기화
    anw = -1

    # 모든 좌표 돌기
    for row in range(N):
        for col in range(N):

            # 먹은 디저트 종류 기록하는 용도
            eaten = []

            # 사용한 방향 기록
            used_direc = [0, 0, 0, 0]

            def dfs(row, col):
                global eaten, used_direc

                # 네가지 방향 체크
                for idx in range(4):
                    n_row = row + dx[idx]
                    n_col = col + dy[idx]

                    # 만약 배열 내에 존재하는 좌표일 때 진행
                    if 0 <= n_row < N and 0 <= n_col:
                        # 1. 이미 먹은 디저트 종류라면 함수 종료
                        if arr[n_row][n_col] in eaten:
                            return
                        # 2. 아직 아무 방향도 사용 안했다면
                        elif used_direc.count(0) == 4:
                            used_direc[idx] += 1
                            dfs(n_row, n_col)
                        # 3. 사용한 방향이 1개라면
                        elif used_direc.count(0) == 3:
                            # 짝꿍 pair가 아닐때 탐색 지속
                            if used_direc[pair[idx]] == 0:
                                used_direc[idx] += 1
                                dfs(n_row)(n_col)
                            # 되돌아 가는 방향일 때는 함수 종료
                            else:
                                return
                        # 4. 사용한 방향이 3개라면
                        elif used_direc.count(0) == 1:

                    # 배열 내에 존재하는 좌표가 아니라면 함수 종료
                    else:
                        return

            dfs(row, col)



    print(f"#{t}")
