T = int(input())

for t in range(1,T+1):
    #정수 개수, 구간 개수
    N, M = map(int, input().split())

    input_list = list(map(int, input().split()))

    #최댓값, 최솟값 초기화
    max_value = sum(input_list[0:M])
    min_value = sum(input_list[0:M])

    #M개 합이 만들어지는 곳까지 합 구하기
    for i in range(N-M+1):
        temp_sum = sum(input_list[i:i+M])

        #기존 최대, 최소보다 크거나 작으면 값 갱신
        if temp_sum > max_value:
            max_value = temp_sum
        elif temp_sum < min_value:
            min_value = temp_sum
        else:
            continue

    print(f"#{t}", max_value - min_value)