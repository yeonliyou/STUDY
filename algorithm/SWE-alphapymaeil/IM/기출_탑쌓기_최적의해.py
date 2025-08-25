import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    # 전체 화물, 탑1 높이, 탑2 높이
    N, W1, W2 = map(int, input().split())
    # 화물들 리스트 (각각의 무게가 요소)
    weight_list = list(map(int, input().split()))

    # 최저 가격 초기화
    min_price = 0

    # 탑의 모든 층 (중복 포함)
    total_floor = [*range(1, W1+1), *range(1, W2+1)]

    # 가장 높은 층부터 적은 무게의 화물을 주면서 비용 더하기
    while len(total_floor) != 0:
        # 현재 가장 높은 층
        curr_max_floor = max(total_floor)
        curr_min_weight = min(weight_list)

        # 비용 더하기
        min_price += curr_max_floor * curr_min_weight

        # 윗줄에서 계산했으면 삭제하기
        total_floor.remove(curr_max_floor)
        weight_list.remove(curr_min_weight)

    print(f"#{t}", min_price)