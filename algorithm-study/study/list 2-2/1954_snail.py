T = int(input())


# 네개의 꼭짓점에서 회전해서 겉 껍질 채우는 함수
def fill_num_side(arr, length, initial_row, initial_col):  # 배열, 껍질 가로 혹은 세로 길이, 초기 행좌표, 열좌표
    global cnt, snail_nums

    # 껍질에서의 출발점
    row = initial_row
    col = initial_col

    if cnt <= snail_nums:
        # 좌측 상단 꼭짓점에서 오른쪽으로 갈때
        for _ in range(length - 1):
            arr[row][col] = cnt
            col += 1
            cnt += 1  # 숫자 채운 횟수 증가

        # 우측 상단 꼭짓점에서 아래쪽으로 갈때
        for _ in range(length - 1):
            arr[row][col] = cnt
            row += 1
            cnt += 1  # 숫자 채운 횟수 증가

        # 우측 하단 꼭짓점에서 왼쪽으로 갈때
        for _ in range(length - 1):
            arr[row][col] = cnt
            col -= 1
            cnt += 1  # 숫자 채운 횟수 증가

        # 좌측 하단 꼭짓점에서 위쪽으로 갈때
        for _ in range(length - 2):
            arr[row][col] = cnt
            row -= 1
            cnt += 1  # 숫자 채운 횟수 증가

        # 초기 행,열 좌표 바로 밑 좌표 채워주기
        arr[row][col] = cnt
        row -= 1
        cnt += 1  # 숫자 채운 횟수 증가

        # 출발 좌표 1씩 증가 (대각선으로 한칸 내려가게)
        initial_col += 1
        initial_row += 1
        # 둘레 껍데기는 가로폭 2 감소
        length -= 2

        return fill_num_side(arr, length, initial_row, initial_col)

    else:
        return arr


for t in range(1, T + 1):
    N = int(input())
    snail_nums = N * N

    # 0으로 이루어진 NxN 2차원 리스트 만들기
    snail_arr = [[0] * N for _ in range(N)]

    # 리스트 인덱싱 0,0 에서 출발
    row, col = 0, 0
    # 넣는 숫자
    cnt = 1

    # N*N까지 채울때까지 재귀함수 돌기
    result = fill_num_side(snail_arr, N, row, col)

    # 답 출력
    print(f"#{t}")
    for i in range(N):
        print(*result[i])  # 리스트 제거해서 출력 - unpacking
