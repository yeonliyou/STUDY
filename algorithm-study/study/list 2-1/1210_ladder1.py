import sys
sys.stdin = open("input.txt")

T = int(input())

# delta (좌, 우, 하)
dx = [0, 0, 1]  # 행
dy = [-1, 1, 0]  # 열

for t in range(1, 11):
    arr = []
    # 100x100 행렬 만들기
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    # 첫 행의 모든 열 출발 검사
    for col in range(100):
        # 첫 출발 row는 0으로 고정
        row = 0
        # 나중에 답 도출하기 위한 출발 col 저장
        curr_col = col

        # 마지막 행에 도착 전까지 반복
        while row < 99:

            # 좌, 우, 하 방향 체크
            for idx in range(3):
                n_row = row + dx[idx]
                n_col = col + dy[idx]

                # 범위 안에 있는 좌표 일때만 체크
                if 0 <= n_row < 100 and 0 <= n_col < 100:
                    # 만약 해당 방향의 element가 1 이라면
                    if arr[n_row][n_col] == 1 and idx == 2:
                        row = n_row
                        col = n_col
                        # 해당 좌표로 이동 (더이상의 방향체크 중지)
                        break
                    elif arr[n_row][n_col] == 1:
                        row = n_row
                        col = n_col
                    # 아니라면 다른 방향 체크
                    else:
                        continue

                # 범위 내 좌표가 아니라면 다음 방향 체크
                else:
                    continue

        # 만약 2라면 찾은 표시와 중지
        if arr[row][col] == 2:
            break

        print(f"#{t}", curr_col)




