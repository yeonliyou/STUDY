#오름차순 정렬하는 함수
def sort_asce(num_list, k):   #숫자리스트, 인풋 리스트 길이
    #리스트 내부 숫자의 범위
    max_num = max(num_list)

    #각 숫자의 등장횟수를 담을 리스트 : 0부터 max_num까지
    count_arr = [0] * (max_num+1)

    #최종 답을 넣을 리스트
    result = [0] * k

    # 숫자 등장횟수 기록
    for i in range(k):
        count_arr[num_list[i]] += 1

    #1부터 k 숫자까지 돌면서 등장 횟수 누적
    for i in range(1, max_num + 1):
        count_arr[i] += count_arr[i - 1]  # count 누적 값

    # (시작값, 끝값(제외), 증가/감소값)
    for i in range(k - 1, -1, -1):
        count_arr[num_list[i]] -= 1
        result[count_arr[num_list[i]]] = num_list[i]

    return result

T = int(input())

for t in range(1, T+1):
    #리스트 길이
    N = int(input())
    num_list = list(map(int, input().split()))
    
    #오름차순 함수 호출
    result = sort_asce(num_list, N)

    print(f"#{t}", *result)