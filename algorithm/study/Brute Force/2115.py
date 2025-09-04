import sys
sys.stdin = open('5188_input.txt')

T = int(input())

for t in range(1, T+1):
    # 벌통 크기, 선택할 벌통 개수, 최대 꿀의 양
    N, M, C = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 특정 행에서 어떤 열들을 썼는지
    dp = [0 for _ in range(N)]

    print(f"#{t}", anw)