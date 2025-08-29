import sys

sys.stdin = open("1949_input.txt")

T = int(input())

for t in range(1, T+1):
    # 배열 크기, 공사 가능 최대 높이
    N, K = map(int, input().split())

    # 배열
    arr = []
    # 방문 여부 체크하는 배열
    visited = []

    for _ in range(N):
        arr.append(list(map(int,input().split())))
        visited.append([0 for _ in range(N)])

    # delta - 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 1. 가장 높은 높이 찾기
    most_high = 0
    for i in arr:
        if max(i) > most_high:
            most_high = max(i)

    # 2. 가장 높은 곳들 좌표 저장
    high_loc =  []
    for row in range(N):
        for col in range(N):
            if arr[row][col] == most_high:
                high_loc.append((row,col))
    # 답 초기화
    anw = 0

    # 3. 높은 곳들 하나씩 검사 시작
    for coor in high_loc:
        # 출발 지점
        row, col = coor

        # 방문 여부 체크하는 배열 초기화
        visited = []

        for _ in range(N):
            visited.append([0 for _ in range(N)])

        # 첫 출발점 방문 무조건 함
        visited[row][col] = 1

        # 등산로의 길이
        go = 1

        # 산을 깎았는지 여부 확인
        flag = False

        def dfs(row, col, visited, arr, go, flag):
            global anw

            # 현위치에서 네가지 방향 체크
            for idx in range(4):
                n_row = row + dx[idx]
                n_col = col + dy[idx]

                # 배열 내에 존재하는 좌표이면서 and 방문한 적이 없는 곳일 때
                if (0 <= n_row < N and 0 <= n_col < N) and visited[n_row][n_col] == 0:
                    # 1) 현 위치보다 낮은 지형이라면
                    if arr[row][col] > arr[n_row][n_col]:
                        # 방문하기
                        visited[n_row][n_col] = 1
                        dfs(n_row, n_col, visited, arr, go + 1, flag)
                        # 백트래킹
                        visited[n_row][n_col] = 0

                    # 2) 현 위치보다 높은 or 같은 지형이라면
                    else:
                        curr_height = arr[row][col]
                        next_height = arr[n_row][n_col]
                        # 이미 깎은 적 있거나 or 깎을 개수가 부족한 경우
                        if flag == True or (next_height - curr_height>= K):
                            if go > anw:
                                anw = go

                        # 깎을 수 있다면
                        else:
                            # 무조건 최소로 깎음 => 왜냐면 어차피 한번 깎으면 다른데는 못깎고 무조건 낮은 지형으로만 이동해야하기 때문에 최소로 깎아야함
                            arr[n_row][n_col] -= (next_height - curr_height + 1)
                            visited[n_row][n_col] = 1
                            dfs(n_row, n_col, visited, arr, go + 1, True)
                            # 백트래킹
                            visited[n_row][n_col] = 0
                            arr[n_row][n_col] = next_height


        dfs(row, col, visited, arr, go, flag)

    print(f"#{t}", anw)