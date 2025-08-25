T = int(input())

for t in range(T):
    N = int(input())

    #상자의 수 리스트 받기
    box_list = list(map(int, input().split()))

    # 상자가 아예 없을 때
    if all(x == 0 for x in box_list):
        sum = 0
        print(f'#{t + 1}', sum)
    # 상자가 하나라도 쌓인 곳이 있을 때
    else:
        final_list = []

        # 100층 배열 만들기 (층수 해당되면 1, 비어있으면 0)
        for box_height in box_list:
            sample = [0 for _ in range(100)]
            for i in range(box_height):
                sample[i] = 1

            final_list.append(sample)

        #가장 큰 낙차가 될 수 있는 후보들 담는 리스트
        candi = []


        #각 상자가 쌓인 곳마다 가장 꼭대기만 검사
        for row in range(N):
            sum = 0
            max_floor = box_list[row]
            check_floor = final_list[row][max_floor-1]
            for change_row in range(row+1,N):
                if final_list[change_row][max_floor-1] == 0:
                    sum += 1
                else:
                    continue

            candi.append(sum)


        print(f'#{t+1}', max(candi))



