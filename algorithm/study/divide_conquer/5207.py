import sys
sys.stdin = open("5207_input.txt")

T = int(input())

# direction: -1이면 이전에 왼쪽 탐색, 1이면 이전에 오른쪽 탐색, 0은 초기
def binary_search(lst, l, r, direction):
    global target, flag

    # 왼쪽 인덱스가 오른쪽보다 커지면 함수 종료 (끝까지 못 찾은 경우)
    if l > r:
        flag = False
        return

    # 가운데 인덱스값
    m = (l + r) // 2

    # 가운데 값이랑 target이랑 같으면 함수 종료
    if lst[m] == target:
        return

    # 왼쪽(-1) 탐색
    if lst[m] > target and direction != -1:
        binary_search(lst, l, m-1, -1)

    # 오른쪽(1) 탐색
    elif lst[m] < target and direction != 1:
        binary_search(lst, m+1, r, 1)

    # 같은 방향으로 탐색해야 하면 함수 종료
    else:
        flag = False



for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    anw = 0

    for target in B:
        flag = True
        binary_search(A, 0, N-1, 0)  # 초기 방향 0

        if flag:
            anw += 1

    print(f"#{tc} {anw}")
