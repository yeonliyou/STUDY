def counting_sort(input_arr, k):
    count_arr = [0] * (k+1)
    result = [0] * len(input_arr)

    for i in range(len(input_arr)):
        count_arr[input_arr[i]] += 1   #숫자 등장횟수 기록

    for i in range(1, k+1):
        count_arr[i] += count_arr[i-1]   #count 누적 값

    #(시작값, 끝값(제외), 증가/감소값)
    for i in range(len(input_arr)-1, -1, -1):
        count_arr[input_arr[i]] -= 1
        result[count_arr[input_arr[i]]] = input_arr[i]

    return result


arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]