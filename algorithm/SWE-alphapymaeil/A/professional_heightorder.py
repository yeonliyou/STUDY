import sys
from collections import deque

sys.stdin = open("키순서_input.txt")

T = int(input())

for tc in range(1, T+1):
    # 학생 수
    N = int(input())

    # 인접행렬 만들기
    arr = []
    for _ in range(N):
        arr.append(list(0 for _ in range(N)))

    # 두 학생 비교 횟수
    M = int(input())

    for _ in range(M):
        # 행 -> 열
        s, t = map(int, input().split())

        # 해당 행 인덱스 < 해당 열 인덱스 이면 1
        arr[s][t] = 1


