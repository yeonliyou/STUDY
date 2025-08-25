T = int(input())

for t in range(1, T+1):
    N = int(input())
    number_list = list(map(int, input().split()))

    #최대,최소,인덱스값 초기화
    max_value = number_list[0]
    min_value = number_list[0]
    max_value_idx = 0
    min_value_idx = 0

    for i in range(N):
        if number_list[i] >= max_value:   #기존 최댓값 이상인 것만 갱신
            max_value = number_list[i]
            max_value_idx = i
        elif number_list[i] < min_value:   #기존 최소값보다 작은 것만 갱신
            min_value = number_list[i]
            min_value_idx = i
        else:
            continue

    print(f"#{t}", abs(max_value_idx - min_value_idx))