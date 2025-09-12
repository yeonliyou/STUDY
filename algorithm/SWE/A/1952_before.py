# 이 버전은 greedy => 최적해 못찾음
import sys

sys.stdin = open("1952_input.txt")

T = int(input())

for t in range(1,T+1):
    # 이용권 가격 받기
    #day(0), month(1), three_month(2), year(3) = map(int, input().split())
    price_info = list(map(int, input().split()))

    # 12개월 이용 계획 ( 1월(0) ~ 12월(11) )
    plan_list = list(map(int, input().split()))

    # 각 달의 이용권 정보 초기화
    price_plan = [-1 for _ in range(12)]

    # 최소 가격으로 초기화
    min_price = 0

    # 1. 하루, 한달 이용권까지만 고려
    for m in range(12):
        # 이용 계획이 있는 달일 때
        if plan_list[m] != 0:
            # 한달 이용료가 더 싸면 1 아니면 0 배정
            if plan_list[m] * price_info[0] >= price_info[1]:
                price_plan[m] = 1
                # 비용 누적해주기
                min_price += price_info[1]

            else:
                price_plan[m] = 0
                min_price += plan_list[m] * price_info[0]

    print("한달권까지 고려", price_plan)

    # 2. 세달 이용권까지 고려 (greedy)
    next_first = 0

    while next_first < 12:
        #print("지금 next_first", next_first)
        stack = []
        temp_sum = 0

        for m in range(next_first, 14):

            # 현재 달을 스택에 추가
            stack.append(m)

            # 조건에 걸리면
            if len(stack) != 3:
                continue
            #print(stack)

            for i in stack:
                # 가짜 인덱스라면
                if i > 11:
                    continue

                # 해당 달은 이용계획이 없다면
                elif price_plan[i] == -1:
                    continue
                # 해당 달은 원데이 이용권이라면
                elif price_plan[i] == 0:
                    # 해당 달의 기존 이용권 가격 누적
                    temp_sum += plan_list[i] * price_info[0]
                # 해당 달은 한달 이용권이라면
                elif price_plan[i] == 1:
                    # 해당 달의 기존 이용권 가격 누적
                    temp_sum += price_info[1]

            # 3달의 기존 비용 합이 세달권 비용 이상이면
            if temp_sum >= price_info[2]:
                min_price -= temp_sum
                min_price += price_info[2]
                next_first = stack[-1] + 1

            else:
                next_first += 1

            # 초기화
            break

    # 3. 연권 이용권까지 고려 (연권 이용권 vs 지금까지의 최소비용 => 비교)
    min_price = min(price_info[3], min_price)


    print(f"#{t}", min_price)

