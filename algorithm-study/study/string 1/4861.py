#전치 행렬 만드는 함수
def find_trans_arr(arr, N):  #인자 : 행렬, 행렬 크기

    # 대각선 기준 오른쪽만 돌면서
    for row in range(N):
        for col in range(row + 1, N):
            # 자리 바꿔주기
            arr[row][col], arr[col][row] = arr[col][row], arr[row][col]

    return arr

# 가로 회문 체크하는 함수
# 인자 : 배열, 배열 크기, 회문 길이
def check_reverse_true(arr, N, M):
    flag = False
    anw = 0

    # 회문 찾을 때까지 반복
    while flag == False:
        # 배열 크기만큼 row를 돌기
        for row in range(N):
            # 주어진 배열에서 가능한 회문 범위만 돌기
            for col in range(N - M + 1):
                curr_str = ''.join(arr[row][col:(col + M)])  # 현재 문자열
                reversed_str = curr_str[::-1]  # 현재 문자열을 뒤집은 버전

                # 위의 두 문자열이 같은지 비교 : 같으면 flag ture로 변경
                if curr_str == reversed_str:
                    anw = curr_str  # 정답 저장
                    flag = True
                    break
                else:
                    continue

        return anw

import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for t in range(1, T+1):
    # 배열 크기, 회문 길이
    N, M = map(int, input().split())

    # 배열 받기
    arr = [[input().split()] for _ in range(N)]

    # 가로 회문 존재여부부터 탐색
    anw = check_reverse_true(arr, N, M)

    # 전치 행렬로 바꾸기기
    arr = find_trans_arr(arr, N)

    # 만약 가로 회문을 못 찾았으면 세로 회문 탐색
    if anw == 0:
        anw = check_reverse_true(arr, N, M)

    print(f"#{t}", anw)