import sys
sys.stdin = open("2112_input.txt")

T = int(input())

# K개 연속 체크 탐색 함수
def check_Kcnt(arr, D, W):
    # 전부 검사 통과 여부
    flag = True

    # 열 하나씩 통과할 수 있는 지 체크
    for c in range(W):
        for r in range(D):

# 최소 약품 처리 찾는 함수
def find_min_drug():
    


for x in range(1, T+1):
    # 두께, 가로크기, 합격기준
        # 3 <= D <= 13
        # 1 <= W <= 20
        # 1 <= K <= D
    D, W, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(D)]

    # 답 초기화 (약품의 최소 투입 횟수)
    anw = 0

    # K가 2 이상일 때만 dfs 함수 돌리기
    if K != 1:


    print(f"#{x}", anw)