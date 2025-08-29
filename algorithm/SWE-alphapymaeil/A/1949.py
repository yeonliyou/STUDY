import sys

sys.stdin = open("test.txt")

T = int(input())

for t in range(1, T+1):
    # 배열 크기, 공사 가능 최대 높이
    N, K = map(int, input().split())
    
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))

    max_length = 0

    

    print(f"#{t}", max_length)