import sys
import heapq

sys.stdin = open("5249_input.txt")

T = int(input())

for tc in range(1, T+1):
    # 마지막 노드 번호, 간선 개수
    V, E = map(int, input().split())

    arr = [[0] * (V+1) for _ in range(N)]


    for _ in range(E):
        # 양끝 노드 / 가중치
        n1, n2, w = map(int, input().split())
        arr[n1][n2] = w



