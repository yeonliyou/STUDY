import sys
import itertools

sys.stdin = open("4881.txt")

T = int(input())

for t in range(1, T + 1):
    N = int(input())

    arr = []
    arr.append(list(map(int, input().split())))

    # 식재료의 개수
    num_list = [i for i in range(N)]

    # 식재료 2개 조합의 모음
    com_set = itertools.combinations(num_list, 2)

    # 최대 식재료 시너지의 합
    min_diff = 2000 * N

    for curr in com_set:


