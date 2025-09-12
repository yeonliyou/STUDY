import sys
sys.stdin = open("2112_input.txt")

T = int(input())

# K개 연속 체크 탐색 함수
def check_Kcnt(arr):

    # 열 하나씩 통과할 수 있는 지 체크
    for c in range(W):
        # 해당 열 검사 통과 여부
        flag = False

        # 해당 열의 첫번째 문자 저장
        fir = arr[0][c]

        # 같은 문자가 연속 몇개 인지
        cnt = 1

        # 행 하나씩 돌기
        for r in range(1, D):
            # 해당 행의 요소랑 현재 기준 첫번째 문자랑 같으면 길이 추가
            if fir == arr[r][c]:
                cnt += 1
                # K개가 되면
                if cnt == K:
                    flag = True
                    break
            else:
                fir = arr[r][c]
                cnt = 1

        # 만약 앞에 검사한 열이 통과를 못했다면 for문 중지
        if flag == False:
            break

    return flag

# 최소 약품 처리 찾는 함수
def find_min_drug():



for x in range(1, T+1):
    # 두께, 가로크기, 합격기준
        # 3 <= D <= 13
        # 1 <= W <= 20
        # 1 <= K <= D
    D, W, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(D)]

    # 답 초기화 (약품의 최소 투입 횟수)
    anw = 0

    # K가 2 이상일 때만 dfs 함수 돌리기
    if K != 1:
        pass
    else:
        flag = check_Kcnt(arr)
        if flag == True:



    print(f"#{x}", anw)