T = int(input())

for t in range(T):
    N = int(input())
    number_list = list(map(int, input().split()))
    
    #적당히 작은 숫자, 큰 숫자
    max_num = 0
    min_num = 1000000
    
    for i in number_list:
        # max_num보다 크면 최댓값 갱신
        if i > max_num:
            max_num = i
        # min_num보다 작으면 최댓값 갱신
        if i < min_num:
            min_num = i

    #최대 최소 차이 구하기
    anw = max_num - min_num

    print(f'#{t+1}', anw)