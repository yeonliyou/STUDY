for t in range(10):
    N = int(input())

    #건물 전체 정보 받기
    building_list = list(map(int, input().split()))

    #가장 높은 빌딩의 높이 저장
    max_height = max(building_list)

    final_list = []

    #제일 높은 층 기준으로 배열 만들기 (층수 해당되면 1, 비어있으면 0)
    for building_height in building_list:
        sample = [0 for _ in range(max_height)]
        for i in range(building_height):
            sample[i] = 1

        final_list.append(sample)

    #print(final_list)

    #조망이 확보된 빌딩 수 초기화
    view_sum = 0
    
    #앞뒤로 0,0 층인 것 제외하고 검사 돌리기
    for row in range(2, N-2):
        for col in range(max_height):
            #만약 1이면 조망 검사하기
            if final_list[row][col] == 1:
                if (final_list[row-1][col] == 0) and (final_list[row-2][col] == 0) and (final_list[row+1][col] == 0) and (final_list[row+2][col] == 0):
                    view_sum += 1
                else:
                    continue
            #만약 0이면 조망 검사 패스하고 반복문 종료
            else:
                break
    
    print(f'#{t+1}', view_sum)


