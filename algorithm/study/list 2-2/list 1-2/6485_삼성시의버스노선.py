T = int(input())

for t in range(1, T+1):
    #버스 노선 개수
    N = int(input())
    line_list = []   #버스 노선 리스트

    #Ai, Bi N번 받기
    for _ in range(N):
        sample = list(map(int, input().split()))
        line_list.append(sample)

    #체크해야하는 버스 정류장 개수
    P = int(input())
    #몇 개의 버스 노선이 다니는지 알아야 하는 버스 정류장의 번호 모음
    check_bus_stop_list = []
    check_bus_idx_list = [0 for _ in range(P)]

    for i in range(P):
        check_bus_stop_list.append(int(input()))   #지나가는 버스 노선 개수 초기화

    #체크해야 하는 버스 정류장들 키 호출
    for idx, i in enumerate(check_bus_stop_list):
        for j in line_list:
            if j[0] <= i <= j[1]:   #노선표 사이에 해당되면
                check_bus_idx_list[idx] += 1   #value값 1추가
            else:
                continue

    #최종 답안 형태 만들기
    check_bus_idx_list = list(map(str, check_bus_idx_list))

    print(f"#{t}", ' '.join(check_bus_idx_list))