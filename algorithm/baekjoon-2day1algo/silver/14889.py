import sys
import itertools

#sys.stdin = open('input.txt')

# 사람 수 받기 (짝수)
N = int(input())

# 배열 생성
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
# 전체 사람 리스트
people_list = [i for i in range(N)]

# 정답 초기화
anw = 100 * (N*N-N)

# 모든 조합 만들기
all_comb_set = list(itertools.combinations(people_list, int(N/2)))

# 모든 가능한 start 팀의 점수 계산해보기
for start in all_comb_set:
    # 해당 조합의 start 팀 sum 초기화
    start_curr_sum = 0
   
    # 모든 요소들의 합 구하기
    for row in start:
        # row랑 같은 col은 사용안하기 위해 임시 리스트 생성
        sample = list(start)
        sample.remove(row)

        # 열 돌기
        for col in sample:
             start_curr_sum += arr[row][col]

    # link 합 구하기
    link = [x for x in people_list if x not in start]
    # 해당 조합의 link 팀 sum 초기화
    link_curr_sum = 0
    # 모든 요소들의 합 구하기
    for row in link:
        # row랑 같은 col은 사용안하기 위해 임시 리스트 생성
        sample = list(link)
        sample.remove(row)
        # 열 돌기
        for col in sample:
             link_curr_sum += arr[row][col]


    curr_diff = abs(start_curr_sum - link_curr_sum)

    if curr_diff < anw:
        anw = curr_diff

print(anw)

