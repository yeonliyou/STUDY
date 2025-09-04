import sys
sys.stdin = open('5188_input.txt')

T = int(input())

# delta 만들기 (오른쪽 , 아래)
dx = [0, 1]
dy = [1, 0]

def dfs(r, c, curr_sum):
    global anw, N

    # 기존 최솟값보다 이미 합이 커져버리면 조기 종료
    if anw < curr_sum:
        return

    # 마지막 좌표에 도착했다면
    if r == N - 1 and c == N - 1:
        anw = min(anw, curr_sum)

    # 오른쪽 한칸, 아래쪽 한칸 순회 시작하기
    for idx in range(2):
        n_r = r + dx[idx]
        n_c = c + dy[idx]

        # 만일 좌표 내 존재하면
        if 0 <= n_r < N and 0 <= n_c < N:
            dfs(n_r, n_c, curr_sum + arr[n_r][n_c])

        # 존재하지 않으면 다음 방향 시작
        else:
            continue


for t in range(1, T+1):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 적당히 큰 수로 초기화
    anw = float('inf')

    # 현재 배열 합 초기화
    curr_sum = arr[0][0]

    # 맨 왼쪽 위에서 출발
    dfs(0, 0, curr_sum)

    print(f"#{t}", anw)