import sys

sys.stdin = open("test.txt")

T = int(input())

for t in range(1, T+1):
    # 배열 크기
    N = int(input())
    arr = []

    # 배열 생성
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 방향키 delta : 왼쪽위 대각선, 오른쪽 위 대각선, 왼쪽 아래 대각선, 오른쪽 아래 대각선
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]