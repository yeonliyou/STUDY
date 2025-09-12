import sys
sys.stdin = open('input.txt')

def make_permutation_list():
     

T = int(input())

for t in range(1, T + 1):
    # 전체 화물, 탑1 높이, 탑2 높이
    N, W1, W2= map(int, input().split())
    # 화물들 리스트 (각각의 무게가 요소)
    weight_list = list(map(int, input().split()))

    # 최저 가격 초기화
    min_price = 0
    for i in weight_list:
        min_price += i * max(W1, W2)

    for permu_list in all_permu_list:
        # 탑 1, 탑 2가 가져갈 각각의 그룹으로 화물 리스트 쪼개기
        group1 = permu_list[:W1]
        group2 = permu_list[W1:]

        # 탑1의 비용
        price1 = 0
        for num in range(W1):
            price1 += (num+1) * group1[num]

        # 탑2의 비용
        price2 = 0
        for num in range(W2):
            price2 += (num+1) * group2[num]

        # 탑1 + 탑2 비용
        total_price = price1 + price2

        # 만약 기존 최솟값보다 작으면 최소 비용 갱신
        if total_price < min_price:
            min_price = total_price
