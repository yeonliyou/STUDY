# DFS 함수 만들기
def dfs(row, curr_sum):  # 현재 row의 위치, 현재 합
    global arr, anw_sum, visited, N

    # 만약 현재까지의 합이 기존의 최솟값보다 크거나 같다면 현재 순열 만들기 중지
    if curr_sum >= anw_sum:
        return

    # 만약 이미 N개 다 선택했다면 반환하고 중지
    if row == N:
        anw_sum = min(curr_sum, anw_sum)
        return

    # 열 순회
    for col in range(N):
        # 아직 선택하지 않은 열이라면
        if visited[col] == 0:
            # 해당 열 선택하기
            pick = arr[row][col]
            # 방문 표시 해주기
            visited[col] = 1
            # 다음 행과 현재 만드는 순열의 현시점까지 합 넘겨주기 (재귀)
            dfs(row + 1, curr_sum + pick)
            visited[col] = 0


import sys
sys.stdin = open("4881.txt")

T = int(input())

for t in range(1, T + 1):
    # N 받기 (배열 크기)
    N = int(input())

    # arr 만들기
    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 가능한 최대 합
    anw_sum = 10*10

    visited = [0] * N  # 선택한 열의 방문 여부를 탐색하기 위한 것

    # row 0, 현재 합도 0부터 시작
    dfs(0, 0)

    print(f"#{t}", anw_sum)