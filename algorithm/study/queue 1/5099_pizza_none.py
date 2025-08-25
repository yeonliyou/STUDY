import sys
from collections import deque

sys.stdin = open("sample_input.txt")

T = int(input())

for t in range(1, T + 1):
    # 화덕의 크기, 피자 개수
    N, M = map(int, input().split())

    # 피자 치즈 정보 리스트
    pizza_list = []

    # 피자 번호와 치즈 정보를 같이 갖고 있는 pair로 리스트 만들기
    for idx, chee in enumerate(list(map(int, input().split()))):
        # (피자 번호, 치즈)
        pizza_list.append((idx, chee))

    # 데크 객체 만들기
    dq = deque()

    # 처음에 화덕의 크기만큼 피자 채우기
    for _ in range(N):
        # 낮은 번호의 피자부터 차례로 채우기
        dq.append(pizza_list[0])
        # 화덕 안에 넣어준 피자는 피자 리스트에서 없애기
        pizza_list.pop(0)

    # 화덕의 회전 횟수
    turn_cnt = 0

    #print('첫 큐', dq)

    # queue가 1개가 남고, 피자리스트에는 더이상 피자가 없을때까지 반복
    while True:
        # 한 바퀴 돌았다면 치즈 반으로 나눠주기
        if turn_cnt !=0 and turn_cnt % N == 0:
            dq = deque([(chee[0], chee[1] // 2) if chee is not None else None for chee in dq])
            #print(dq)

        # 현재 1번 자리의 피자가 빈자리가 아닌 동시에 치즈 양이 0이라면
        if dq[0] != None and dq[0][1] == 0:
            # 해당 피자 빼주기
            dq.popleft()
            # 화덕에 넣어야 되는 피자가 남았을 경우
            if len(pizza_list) > 0:
                # 빈자리가 생겼으므로 다음 피자 넣어주기
                dq.appendleft(pizza_list[0])
                # 화덕에 넣은 피자는 피자리스트에서 제거
                pizza_list.pop(0)
            # 피자가 안남았을 경우
            else:
                dq.appendleft(None)


        # 왼쪽으로 한칸 rotate 해주기
        dq.rotate(-1)
        # 한칸 옆으로 돌린 횟수 +=1
        turn_cnt += 1

        #print("한칸 회전후 체크",dq)

        # None이 아닌 원소 개수 세기
        none_count = sum(1 for x in dq if x is not None)

        if none_count == 1:   # None 값이 아닌 것이 1개 남으면 멈춤
            for i in dq:
                if i != None:
                    # None이 아닌 값 저장
                    anw = i
                    break
            break

    print(f"#{t}", anw[0] + 1)