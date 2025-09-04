import sys
import itertools

sys.stdin = open('5189_input.txt')

T = int(input())

def calculate_battery(per, curr_sum):
    global anw, arr

    # 만약 기존 비용보다 커지면 조기 종료
    if curr_sum > anw:
        return

    if len(per) == 1:
        anw = curr_sum
        return

    # 현재 출발하는 지점에서, 다음 도착 지점 후보들 순회하기
    # start, end
    s, e = per[0], per[1]
    curr_sum += arr[s][e]

    # 맨 앞에꺼 삭제
    per.pop(0)
    calculate_battery(per, curr_sum)



for t in range(1, T+1):
    N = int(input())

    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 방문해야 하는 관리구역 번호들 (실제번호 - 1) / 1번 사무실은 제외
    room_list = [i for i in range(1, N)]

    # 답 초기화
    anw = float('inf')

    # 모든 가능한 관리구역 순열 구하기 (사무실은 제외)
    order_list = list(itertools.permutations(room_list, N-1))


    # 각각의 순서 조합 비용 계산하기
    for per in order_list:
        per = list(per)
        # 맨앞, 맨뒤에 사무실 인덱스 추가해주기
        per.insert(0,0)
        per.append(0)

        # 현재 합 초기화
        curr_sum = 0

        calculate_battery(per, curr_sum)

    print(f"#{t}", anw)



