from collections import deque
import sys

sys.stdin = open("input (1).txt")

for _ in range(1, 11):
    t = int(input())

    dq = deque(list(map(int, input().split())))

    # flag 세우기
    flag = False

    while flag == False:
        # 한 싸이클 돌기 (5까지 감소)
        for i in range(1, 6):
            dq[0] -= i

            # 혹시 음수값 되면 0으로 저장
            if dq[0] <= 0:
                dq[0] = 0
                flag = True

            # 맨 뒤로 보내기
            dq.rotate(-1)

            # 만약 flag가 true 라면 for문 탈출
            if flag == True:
                break

    print(f"#{t}", *dq)