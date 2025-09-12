import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 원하는 방향으로 오목 체크하는 함수
def check_concave(arr, row, col, di):   # 인자: 배열 / 현재 기준 행,열 좌표 / 체크할 방향 / 함수 돌리지 안돌릴지

    # di => 우(0), 하(1), 왼대각 아래(2), 오른대각 아래(3) delta 초기화
    dx = [0, -1, 1, 1]
    dy = [1, 0, -1, 1]

    # 전진 횟수 누적
    cnt = 0

    # 최대 5번까지 전진
    for up in range(5):
        # 새로운 행,열 좌표 갱신
        n_row = row + dx[di] * up
        n_col = col + dy[di] * up

        if 0 <= n_row < N and 0 <= n_col < N:
            check = arr[n_row][n_col]
            if check == 'o':
                cnt += 1
            else:
                break
        else:
            break

    # 오목이 될때만 함수값 yes 반환
    if cnt == 5:
        return 'YES'
    else:
        return 'NO'

for t in range(1, T + 1):

    # 배열의 크기
    N = int(input())

    # 배열 생성
    arr = []
    for _ in range(N):
        arr.append(list(input()))

    # result 초기화
    result = 'NO'

    # 행 먼저
    for row in range(N):
        for col in range(N):
            # 오른쪽으로 체크
            if result != 'YES':
                result = check_concave(arr, row, col, 0)
            # 아래쪽으로 체크
            if result != 'YES':  # 위에서 오목 못찾았을 때만 수행
                result = check_concave(arr, row, col, 1)
            # 왼쪽 대각선으로 체크
            if result != 'YES':
                result = check_concave(arr, row, col, 2)
            # 오른쪽 대각선으로 체크
            if result != 'YES':
                result = check_concave(arr, row, col, 3)

        # 찾았을 때 for 문 중지
        if result == 'YES':
            break
        else:
            continue

    print(f"#{t}", result)
