#실제 sw expert academy에서는 sys 사용 금지되어있음
import sys

sys.stdin = open('input2.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # NxM 풍선 배열 만들기
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # "총" 터진 풍선 최대 개수
    max_balloon = 0

    # 행렬 전체 요소 돌기
    for row in range(N):
        for col in range(M):
            # 상, 하, 좌, 우 더해주고 빼주는 델타
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            #"현재 좌표"에서의 풍선이 터졌을 때 터지는 풍선 개수의 합 초기화
            curr_cnt = arr[row][col]

            #터진 풍선의 꽃가루 개수만큼 반복
            for multi in range(1, arr[row][col]+1):
                # 만약 arr[row][col]이 2라면 2번 반복하고,
                # dx는 각각 반복에서 [-1, 1, 0, 0], [-2, 2, 0, 0]가 사용됨
                new_dx = [x * multi for x in dx]
                new_dy = [y * multi for y in dy]
                # 현재 좌표 기준으로 상, 하, 좌, 우 4번 계산
                for i in range(4):
                    # 갱신되는 행좌표
                    n_row = row + new_dx[i]
                    # 갱신되는 열좌표
                    n_col = col + new_dy[i]

                    # 갱신된 좌표가 행렬의 좌표 내에 있으면 합에 추가
                    if 0 <= n_row < N and 0 <= n_col < M:
                        curr_cnt += arr[n_row][n_col]
                    # 없으면 패스
                    else:
                        continue
            #기존의 최대 터진 풍선개수보다 크면 최댓값 갱신
            if curr_cnt > max_balloon:
                max_balloon = curr_cnt
            #아니면 패스
            else:
                continue

    print(f"#{tc}", max_balloon)
