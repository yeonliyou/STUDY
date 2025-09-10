sample_list =[[11, 45, 23, 81, 28, 34],
[11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

def quick_sort_lomuto(arr, start, end):
    # 정렬할 범위에 원소가 1개 이상 있을 때만 실행
    if start < end:
        # 1. 분할: partition 함수를 호출하여 피벗의 최종 위치를 찾기
        pivot_idx = partition_lomuto(arr, start, end)

        # 2. 정복 (재귀 호출)
        # 피벗을 기준으로 나뉜 왼쪽 부분을 재귀적으로 정렬
        quick_sort_lomuto(arr, start, pivot_idx - 1)
        # 피벗을 기준으로 나뉜 오른쪽 부분을 재귀적으로 정렬
        quick_sort_lomuto(arr, pivot_idx + 1, end)

# 피벗의 위치(인덱스) 찾기 함수
def partition_lomuto(arr, start, end):
    # "마지막 원소"를 피벗으로 선택
    pivot = arr[end]
    # i = '피벗보다 작은 그룹'의 경계를 나타내는 인덱스
    i = start - 1

    # start부터 end-1(피벗 직전)까지 순회
    for j in range(start, end):
        # 만약 현재 원소(arr[j])가 피벗보다 작다면,
        if arr[j] < pivot:
            # '작은 그룹'의 경계를 한 칸 오른쪽으로 이동시키고 (pivot보다 작은 것 요소들의 개수 늘리기)
            i += 1
            # 경계 위치(i)의 값과 현재 값(j)을 교환하여, 작은 원소를 왼쪽으로 보낸다
            arr[i], arr[j] = arr[j], arr[i]

    # 모든 순회가 끝나면, i+1 위치가 피벗이 들어갈 최종 자리임
    # 피벗(arr[end])과 경계 다음 위치(arr[i+1])의 값을 교환함
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    # 피벗의 최종 위치 인덱스를 반환
    return i + 1


for idx in range(3):
    numbers = sample_list[idx]
    quick_sort_lomuto(numbers, 0, len(numbers) - 1) # 정렬할 리스트, 시작 인덱스, 마지막 인덱스
    print(f'#{idx+1}', *numbers)
