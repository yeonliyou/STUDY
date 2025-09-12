# 시간 복잡도 개 터진 버전 ^^ (딕셔너리)

import sys
sys.stdin = open("키순서_input.txt")

T = int(input())

# 계속 타고타고 가서 작은 사람들 찾는 함수
def find_more_small(queue):
    global height_dict, more_small

    # 다음에 새로 검사할 것들
    n_queue = []

    # 하나씩 검사
    for target in queue:
        # 큐에 있는 학생들보다 더 작은 사람들이 있는지 체크
        for key, value in height_dict.items():
            # 만약 기준 학생이 어떤 키의 밸류 값에 있고 and n_queue에 추가되지 않았다면
            if target in value and key not in n_queue and key not in queue:
                more_small.append(key)
                n_queue.append(key)

    # 만약 더 이상 검사할 게 없다면 함수 종료
    if len(n_queue) == 0:
        return
    else:
        find_more_small(n_queue)

# 타고타고 가서 더 큰 사람들 찾는 함수
def find_more_tall(queue):
    global height_dict, more_tall

    # 다음에 새로 검사할 것들
    n_queue = []

    # 하나씩 검사
    for target in queue:
        # 큐에 있는 학생들보다 더 작은 사람들이 있는지 체크
        for key, value in height_dict.items():
            # 만약 기준 학생이 어떤 키의 밸류 값에 있고 and n_queue에 추가되지 않았다면
            if target == key and key not in n_queue:
                # ex) [1,2] 리스트에 [3,4,5]를 추가 => [1,2,3,4,5]
                more_tall.extend(value)
                n_queue.extend(value)

    # 만약 더 이상 검사할 게 없다면 함수 종료
    if len(n_queue) == 0:
        return
    else:
        find_more_tall(n_queue)


for tc in range(1, T+1):
    # 학생 수
    N = int(input())

    # 키 정보 딕셔너리
    # key를 기준으로, value는 key보다 큰 사람
    height_dict = {}

    # 두 학생 비교 횟수
    M = int(input())

    for _ in range(M):
        # 더 작은, 더 큰
        s, t = map(int, input().split())

        # key가 이미 존재한다면
        if s in height_dict.keys():
            height_dict[s].append(t)
        # 새로운 key라면
        else:
            height_dict[s] = [t]

    # 답 초기화
    anw = 0

    # 학생 한명씩 자기가 몇번째인지 알 수 있는지 여부 확인 돌기
    for idx in range(1,N+1):
        # 한 학생을 기준으로 했을 때 자기보다 작은 사람들 모음 & 큰 사람들 모음
        more_small = []
        more_tall = []

        queue = [idx]

        # 1. 현재 기준 학생보다 작은 사람 찾기
        find_more_small(queue)

        # 2. 현재 기준 학생보다 큰 사람 찾기
        find_more_tall(queue)

        print(more_small, more_tall)

        final_list = more_small + more_tall

        # 만약 모든 학생이 기준 학생보다 작거나 크다고 할 수 있다면 anw +1
        if len(set(final_list)) == N-1:
            anw += 1

    print(f"#{tc}", anw)



