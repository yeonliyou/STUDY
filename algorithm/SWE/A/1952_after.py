import sys

sys.stdin = open("1952_input.txt")

T = int(input())

for t in range(1, T+1):
    # 가격 정보 : day(0), month(1), three_month(2), year(3)
    price_info = list(map(int, input().split()))

    # 12개월 이용 계획 (1월(0) ~ 12월(11))
    plan_list = list(map(int, input().split()))

    # 각 달의 이용권 정보 초기화
    price_plan = [-1 for _ in range(12)]

    # 최소 가격으로 초기화
    min_price = 0

    # 1. 하루, 한달, 세달 이용권까지 고려 (서치 결과 greedy ---> DP 보완)
    # dp[i] = i월부터 12월까지의 최소 비용
    dp = [0] * 13

    for m in range(1, 13):
        # 하루 이용권 vs 한달 이용권 비교
        dp[m] = dp[m-1] + min(plan_list[m-1] * price_info[0], price_info[1])

        # 세달 이용권 고려
        if m >= 3:
            dp[m] = min(dp[m], dp[m-3] + price_info[2])

    # 2. 연간권과 최종 비교
    min_price = min(price_info[3], dp[12])

    print(f"#{t}", min_price)
