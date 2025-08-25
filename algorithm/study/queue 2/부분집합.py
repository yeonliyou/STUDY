import sys
import itertools

arr = list(range(1,11))

# 최대 4개까지 가능 (1, 2, 3, 4)
for turn in [4,3,2,1,0]:
    # turn개 짜리 조합 모음
    curr_set = list(itertools.combinations(arr, turn))

    # 조합 모음의 각각의 조합을 하나씩 합이 10이 되는지 체크
    for check in curr_set:
        check = list(check)
        if sum(check) == 10:
            print(*check)


