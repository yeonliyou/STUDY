import sys

sys.stdin = open('input.txt')
print(sys.stdin)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # NxN 배열 만들기
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    #상, 하, 좌, 우 더해주고 빼주는 델타
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #전체 합
    total_sum = 0
    #행렬 전체 요소 돌기
    for row in range(N):
        for col in range(N):
            #절댓값 합 초기화
            abs_sum = 0
            # 현재 좌표 기준으로 상, 하, 좌, 우 4번 계산
            for i in range(4):
                #갱신되는 행좌표
                n_row = row + dx[i]
                #갱신되는 열좌표
                n_col = col + dy[i]

                #갱신된 좌표가 행렬의 좌표 내에 있으면 합에 추가
                if 0 <= n_row < N and 0 <= n_col < N:
                    abs_sum += abs(arr[row][col] - arr[n_row][n_col])
                #없으면 패스
                else:
                    continue

            total_sum += abs_sum
    #답 출력
    print(f"#{tc}", total_sum)



