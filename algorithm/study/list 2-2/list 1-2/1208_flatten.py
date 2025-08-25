for t in range(1, 11):
    limit_dump = int(input())
    dump_list = list(map(int, input().split()))

    # 덤프 가능 횟수가 남아 있고 평탄화가 아직 안됐을 때만 반복
    while limit_dump > 0 and (max(dump_list)-min(dump_list) > 1):

        #최대, 최소, 인덱스 초기화
        current_max = dump_list[0]
        current_min = dump_list[0]
        current_max_idx = 0
        current_min_idx = 0

        #최댓값, 최솟값 갱신하기
        for idx, i in enumerate(dump_list):
            if i >= current_max:
                current_max = i
                current_max_idx = idx
            elif i <= current_min:
                current_min = i
                current_min_idx = idx

        #최대 층의 상자를 최소 층으로 옮기기
        dump_list[current_max_idx] -= 1
        dump_list[current_min_idx] += 1
        limit_dump -= 1

    print(f"#{t}", max(dump_list)-min(dump_list))


