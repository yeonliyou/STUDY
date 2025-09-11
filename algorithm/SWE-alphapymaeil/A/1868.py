import sys
sys.stdin = open("1868_input.txt")

from collections import deque

# 지뢰가 없는 칸을 눌렀을 때
# -> 그 칸에 맞닿아 있는 최대 8칸(변이 닿아있거나 or 꼭짓점이 닿아있거나)에 몇개의 지뢰가 있는지 개수를 0~8 중에서 클릭한 칸에 작성
# -> 근데 이때 숫자가 0이면 그 주변 8칸 아무곳에도 지뢰가 없기 때문에 그 칸들은 모두 0으로 채움
# 지뢰가 어디 있는지 입력 받을때부터 알 수 있음 (* 표시)
# 지뢰가 없는 칸을 제외하고 다 숫자로 채우기 위해서는 최소 몇번 클릭해야하는지 출력
# -> * 아니면 숫자 표시만 배열에 남게 해야함

T = int(input())

# delta (상 하 좌 우 왼위대 왼아대 오위대 오아대)
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

# delta 방향 탐색해서 숫자 채워주는 함수
def bfs(arr, cnt, r, c):
    # 주변 8방향 모두 지뢰가 없었는지를 체크하는 플래그
    flag = True

    # 0으로 바꿔주는 함수들 
    q = deque([(r,c)])

    # 지뢰 몇개인지 세는 변수
    num = 0

    while q:
        r, c = q.popleft()

        cnt += 1

        for idx in range(8):
            n_r = r + dx[idx]   
            n_c = c + dy[idx] 

            # 좌표 존재시
            if 0 <= n_r < N and 0 <= n_c < N:
                # 만약 지뢰를 발견했다면
                if arr[n_r][n_c] == '*':
                    flag = False
                    num += 1
                # 지뢰가 아니라면
                else:
                    q.append((n_r,n_c))
        
        # 주변 8방향 모두 지뢰가 없었다면 (그 저장해논 좌표들 다 0으로 바꿔주기)
        if flag == True:
            for l in q:
                arr[l[0]][l[1]] = 0
                bfs(arr, cnt, l[0], l[1])
        else:
            arr[r][c] = num


for x in range(1, T+1):
    # 배열 크기
    N = int(input())

    arr = [list(input().strip()) for _ in range(N)]

    # 좌표 클릭 횟수
    cnt = 0

    # 1. 모든 지점으로 부터 0으로 바꿀 수 있는 것들 체크
    for r in range(N):
        for c in range(N):
            if arr[r][c] != '*':
                bfs(arr, cnt, r, c)
    
    # 2. '.'은 각각 한 번씩 눌러야 함
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '.':
                cnt += 1

    print(f"#{x}", cnt)