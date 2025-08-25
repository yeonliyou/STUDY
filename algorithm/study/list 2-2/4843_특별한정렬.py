T = int(input())

#카운팅 정렬 이용
#오름차순 정렬하는 함수
def sort_asce(num_list, k):   #숫자리스트, 리스트 길이
    count_arr = [0] * (max(num_list)+1)
    result = [0] * k

    for i in range(k):
        count_arr[num_list[i]] += 1  # 숫자 등장횟수 기록

    #1부터 k 숫자까지 돌면서 등장 횟수 누적
    for i in range(1, max(num_list)+1):
        count_arr[i] += count_arr[i - 1]  # count 누적 값

    # (시작값, 끝값(제외), 증가/감소값)
    for i in range(k - 1, -1, -1):
        count_arr[num_list[i]] -= 1
        result[count_arr[num_list[i]]] = num_list[i]

    return result

#내림차순 정렬하는 함수
def sort_desc(num_list, k):
    # 리스트 내부 숫자의 범위
    max_num = max(num_list)

    # 각 숫자의 등장횟수를 담을 리스트 : 0부터 max_num까지
    count_arr = [0] * (max_num + 1)

    # 최종 답을 넣을 리스트
    result = [0] * k

    # 숫자 등장횟수 기록
    for i in range(k):
        count_arr[num_list[i]] += 1

    # 오름차순이랑 반대로 누적
    for i in range(max_num, 0, -1):
        count_arr[i-1] += count_arr[i]  # count 누적 값

    # (시작값, 끝값(제외), 증가/감소값)
    for i in range(k - 1, -1, -1):
        count_arr[num_list[i]] -= 1
        result[count_arr[num_list[i]]] = num_list[i]

    return result


for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    #내림차순, 오름차순 정렬 리스트 구하기
    desc_list = sort_desc(num_list, N)
    asce_list = sort_asce(num_list, N)

    #최종 답
    anw_list = []
    # 내림차순, 오름차순 정렬 리스트 각각 5번씩 번갈아가면서 정답 리스트에 추가
    for idx in range(5):
        anw_list.append(desc_list[idx])
        anw_list.append(asce_list[idx])

    print(f"#{t}", *anw_list)
