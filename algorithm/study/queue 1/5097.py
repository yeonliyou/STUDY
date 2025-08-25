import sys
from collections import deque

sys.stdin = open("sample_input (2).txt")

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    # 피자 치즈 정보 리스트
    dq = deque(list(map(int, input().split())))

    # 오른쪽으로 M번 보내기
    for _ in range(M):
        dq.rotate(-1)


    print(f"#{t}", dq.popleft())