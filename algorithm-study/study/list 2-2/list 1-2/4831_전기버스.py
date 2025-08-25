T = int(input())

for t in range(1,T+1):
    #최대 이동 거리(현재 배터리 양), 종점 번호, 충전기 설치정류장 개수
    K, N, M = map(int, input().split())  #K는 안바뀜

    #전체 정류장 정보 리스트. 0이면 충전기 없고, 1이면 충전기 있음을 표현
    total_bus_info = [0 for _ in range(N+1)]

    # 충전기가 설치된 정류장 리스트
    charge_list = list(map(int, input().split()))

    #충전기 설치 정류장은 1 주기
    for i in charge_list:
        total_bus_info[i] = 1

    #현재 위치
    current_loc = 0
    #충천 횟수
    total_charge = 0

    while current_loc < N:
        current_loc += K   #이동 최대거리만큼 일단 이동
        #이미 도착 가능 거리면 종료
        if current_loc >= N:
            break
        # 정류장이 없다면
        if total_bus_info[current_loc] == 0:
            cnt = 0   #뒤로가기 횟수 : 뒤로 물러나는 횟수가 이동 최대거리보다 커지면 안됨
            flag = False  #정류장 찾았는지 여부
            while cnt < K-1:
                current_loc -= 1   #뒤로 한발 물러나기
                cnt += 1
                #뒤로 물러난 곳에 정류장이 없다면
                if total_bus_info[current_loc] == 0:
                    continue
                # 뒤로 물러난 곳에 정류장이 있다면 충전하고 첫 while문으로 돌아가기
                else:
                    total_charge += 1  # 충전 +1
                    flag = True
                    break

            #뒤로가기로 정류장 못찾은 경우
            if flag == False:
                total_charge = 0
                break
            #뒤로가기로 정류장 찾은 경우
            else:
                continue

        # 정류장이 있다면
        else:
            total_charge += 1   #충전 +1

    print(f"#{t}", total_charge)