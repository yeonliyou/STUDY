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
    # 방향 바꿔주기
    di += 1

    # 오목이 될때만 함수값 yes 반환
    if cnt == 5:
        return 'YES'
    # 오목 못 찾았는데 이미 모든 방향 탐색했다면
    elif di > 3:
        return 'NO'
    # 오목 못 찾았는데 아직 탐색 가능하다면
    else:
        return check_concave(arr, row, col, di)

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
            # 우, 하, 대각(왼쪽, 오른쪽) 체크
            if result == 'NO':
                result = check_concave(arr, row, col, 0)

        # 찾았을 때 for 문 중지
        if result == 'YES':
            break
        else:
            continue

    print(f"#{t}", result)
