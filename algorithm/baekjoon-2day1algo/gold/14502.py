## 아 ; 문제 잘못읽음

import sys
sys.stdin = open('input.txt')

# 행, 열 크기
N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 안전구역 개수의 최댓값 초기화
max_value = 0

# 한 배열의 안전구역 확인 함수 (바이러스를 찾고 )
def check_safe_area(arr, N, M):  # 배열, 행크기, 열크기
    # 탐색을 위한 델타 만들기
    # 하, 상, 우, 좌
    dx = [1, -1, 0, 0]
    dy = [0 , 0, 1, -1]

    # 안전구역 수 초기화
    total_safe_cnt = 0

    # 한칸씩 돌면서 안전구역 체크
    for row in range(N):
        for col in range(M):
            # 요소가 0일때만 체크
            if arr[row][col] == 0:
                # 상하좌우 4번 체크하기
                for idx in range(4):
                    # 바이러스를 만났는지 여부를 체크할 flag
                    flag = False

                    # 전진하는 반복문
                    for multi in range(1, max(M,N)):
                        n_row = row + dx[idx] * multi
                        n_col = col + dy[idx] * multi


                        # 배열 내에 존재하는 좌표일 때만
                        if 0 <= n_row < N and 0 <= n_col < M:
                            # 만약 빈칸이라면
                            if arr[n_row][n_col] == 0:  # 계속 체크
                                continue
                            # 벽이라면
                            elif arr[n_row][n_col] == 1:  # 체크 중지
                                break
                            # 바이러스라면
                            elif arr[n_row][n_col] == 2:  # 체크 중지
                                flag = True
                                break

                    # 상하좌우 방향 체크하다가 한번이라도 바이러스를 만나면
                    # 검사 중지하고 검사 기준 칸 이동하기
                    if flag == True:
                        break
                # 바이러스 만난적 없으면 세이프 구역 +1
                if flag == False:
                    total_safe_cnt += 1

            # 요소가 1이거나 2면 패스
            else:
                continue

    return total_safe_cnt

# 벽을 새로 세울 구역을 뽑는 함수
def pick_new_building_area():
    # 2의 좌표 저장소
    two_loc_set = []

    # 2가 있는 위치를 탐색하기
    for row in range(N):
        for col in range(M):
            # 요소가 2일 체크
            if arr[row][col] == 2:
                two_loc_set.append([row, col])

    # 2의 상하좌우 중에 벽 세우기
    for curr_two in two_loc_set:


