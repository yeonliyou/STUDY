#import sys
#sys.stdin = open('input.txt')

T = int(input())

# 오름차순 정렬
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

for t in range(1, T + 1):
    # 입력 정수의 개수
    N = int(input())

    # Ai 리스트
    ai_list = list(map(int, input().split()))

    # 최댓값 초기화
    max_value = -1

    for i in range(N):
        for j in range(i+1, N):
            # ai * aj의 결과
            cal_num = ai_list[i] * ai_list[j]

            # str로 바꾸고 리스트에 담아서 각 원소를 쪼개고
            # 이 각각의 요소를 바로 int로 바꿔주기
            change_str_list = [int(num) for num in list(str(cal_num))]

            # 카운팅 정렬로 오름차순 정렬해주기
            reversed_list = sort_asce(change_str_list, len(change_str_list))

            # 다시 이 리스트를 하나의 숫자로 합쳐주기
            compare_num = int(''.join(map(str, reversed_list)))

            # 단조증가 수랑 기존 계산한 수랑 같고
            if cal_num == compare_num:
                # 기존 최댓값보다 현재 값이 크면최댓값 갱신
                if max_value < cal_num:
                    max_value = cal_num
                else:
                    continue
            # 단조증가가 아니라면 패스
            else:
                continue

    print(f"#{t}", max_value)

