import sys
import itertools

sys.stdin = open('2115_input.txt')

T = int(input())

# 최대 꿀양에 따라 벌꿀 수확 계산하는 함수
def calculate_honey(honey_set, C, M):
    # 최대값 초기화
    m = 0

    # 이미 벌꿀 수 제한을 만족한다면
    if sum(honey_set) <= C:
        m = sum(i*i for i in honey_set)
    # 벌꿀 수 조절을 해야하는 경우
    else:
        while True:
            # 1개 조합까지 다 했다면 반복문 중지
            if M == 1:
                break
            # 벌꿀양 제한 됐을 때 각 조합의 벌꿀 수확량 계산
            for curr in list(itertools.combinations(honey_set, M-1)):
                if sum(curr) <= C:
                    # 벌꿀 수확량 공식으로 구한 현재 수확량
                    temp_sum = sum(i*i for i in curr)
                    # 더 큰 값으로 갱신
                    m = max(temp_sum, m)
                else:
                    continue
            M -= 1

    return m
    
    
for t in range(1, T+1):
    # 벌통 크기, 선택할 벌통 개수, 최대 꿀의 양
    N, M, C = map(int, input().split())

    # 벌꿀 정보 배열 만들기
    arr = []
    # 조합별로 벌꿀양을 기록하기 위한 배열
    comb_arr = list(0 for _ in range(N*N))

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 첫 행부터 출발 - 모든 가능한 최대합 조합 배열 만들기
    for r in range(N):
        # 시작 열 초기화
        c = 0

        while c < N:
            # 현재 시작 열부터 같은 행에서 M개의 벌꿀을 선택할 수 있다면
            if c + M <= N:
                # 현재 벌꿀 조합
                temp_honey_list = arr[r][c:c+M]
                
                # 현재 벌꿀 조합으로 얻어지는 최대 꿀양
                temp_honey = calculate_honey(temp_honey_list, C, M)
                comb_arr.append(temp_honey)

            # 선택할 수 없다면 그냥 빈칸 0 추가
            else:
                comb_arr.append(0)

            # 한칸 옆으로 이동
            c += 1
                
    # 답 초기화
    anw = 0

    # 모든 가능한 조합 탐색 g1, g2(g1보다 M만큼 떨어진 곳부터)
    for g1 in range(len(comb_arr)):
        for g2 in range(g1 + M, len(comb_arr)):
            anw = max(comb_arr[g1] + comb_arr[g2] , anw)


    print(f"#{t}", anw)