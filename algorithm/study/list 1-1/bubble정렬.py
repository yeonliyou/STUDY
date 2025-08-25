def bubble_sort(arr, N):
    # j부터 i까지 검사
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                # 앞 숫자가 더 크면 자리 바꾸기
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

numbers = [64, 13, 9, 62, 3]
N = len(numbers)
sorted_numbers = bubble_sort(numbers, N)
print("정렬 후:", sorted_numbers)