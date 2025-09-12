import sys
sys.stdin = open('input.txt')

T = int(input())

# 상, 하, 좌, 우 델타 만들기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, T + 1):
    # 공간의 넓이 받기
    N = int(input())

    # 안전 공간 개수 초기화
    total_safe = 0

    # 배열 만들기
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))


    # 배열 한 칸씩 돌면서 경비병의 눈을 피할 수 있는 곳 찾기
    for row in range(N):
        for col in range(N):
            
            # 0인 경우에만 검사
            if arr[row][col] != 0:
                continue
                
            # 기준 좌표에서 경비병 만났는지를 확인하는 flag 초기화
            police_meet = False
            
            # 상하좌우 방향 4번 체크
            for idx in range(4):

                # 가능한 범위까지 계속 칸을 전진하면서 벽 or 경비병 여부 체크
                for up in range(N):
                    # 전진으로 갱신한 행열 좌표
                    n_row = row + dx[idx] * up
                    n_col = col + dy[idx] * up

                    # 갱신한 좌표가 배열 내에 존재하는 좌표라면
                    if 0 <= n_row < N and 0 <= n_col < N:
                        check = arr[n_row][n_col]
                        if check == 1:
                            break  # 검사 break
                        elif check == 0:
                            continue  # 검사 계속 진행
                        else:  # 2를 만나는 경우 -> 해당 row,col은 경비병 눈을 피할 수 없는 좌표
                            police_meet = True
                            break

                # 만약 경비병을 만난 방향이 있다면 중지
                if police_meet == True:
                    break

            # 상 하 좌 우 방향 모두 경비병을 만나지 못했으면 안전 구역 개수 +1
            if police_meet == False:
                total_safe += 1

    print(f"#{t}",total_safe)