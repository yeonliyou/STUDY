import copy

#탐색 횟수 계산하
def calculate_count(P, m): #전체 쪽수, 본인이 찾아야 하는 쪽 번호
    #첫번째 페이지
    l = 1
    #마지막 페이지
    r = P
    #탐색 횟수 초기화
    count_value = 0
    #갱신되는 중간 페이지
    c = 0

    #중간 페이지가 찾는 쪽수랑 다른 동안 반복
    while c != m:
        #중간 지점 계산
        c = int((l+r)/2)
        # 중간점 < 찾고자하는 포인트
        if c < m:
            l = c #왼쪽을 중간 페이지로 갱신
            r = r
        # 중간점 > 찾고자 하는 포인트
        else:
            r = c #오른쪽을 중간 페이지로 갱신
            l = l
        #탐색횟수 1 증가
        count_value += 1
    return count_value

T = int(input())

for i in range(T):
    #전체 쪽수, A가 찾아야하는 쪽 번호, B가 찾아야하는 쪽 번호
    P, A, B = map(int, input().split())
    #A의 탐색 횟수 계산
    a_count = calculate_count(P, A)
    #B의 탐색 횟수 계산
    b_count = calculate_count(P, B)
    #A와 B의 탐색횟수를 비교하여 더 적게 탐색한 사람 출력
    if a_count > b_count:
        print(f'#{i+1}', 'B')
    elif a_count < b_count:
        print(f'#{i+1}', 'A')
    #비겼을 경우
    else:
        print(f'#{i+1}', 0)