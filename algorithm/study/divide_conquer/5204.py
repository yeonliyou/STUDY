import sys
sys.stdin = open("5204_input.txt")

def merge(left, right):
    global cnt

    merged_arr = []

    # 두 배열을 가리킬 포인터(인덱스) 초기화
    left_idx, right_idx = 0, 0

    # 두 배열 중 하나라도 원소가 남아있는 동안 반복
    while left_idx < len(left) and right_idx < len(right):

        # 왼쪽 배열의 값이 더 작거나 같으면, 결과에 추가하고 왼쪽 포인터 이동
        if left[left_idx] <= right[right_idx]:
            merged_arr.append(left[left_idx])
            left_idx += 1
        # 오른쪽 배열의 값이 더 작으면, 결과에 추가하고 오른쪽 포인터 이동
        else:
            merged_arr.append(right[right_idx])
            right_idx += 1

    # 위 루프가 끝난 후, 아직 남아있는 원소들을 결과 뒤에 그대로 붙여줌
    # (한쪽 배열은 이미 모든 원소가 소진되었으므로, 둘 중 하나만 실행됨)
    merged_arr.extend(left[left_idx:])
    merged_arr.extend(right[right_idx:])

    # 만약 현재 정렬한 배열의 마지막 원소랑, 왼쪽 파트의 마지막 원소랑 같았으면 cnt +1
    if right[-1] != left[-1] and merged_arr[-1] == left[-1]:
        cnt += 1

    return merged_arr

def merge_sort(arr):
    # 배열의 길이가 1 이하면 이미 정렬된 상태이므로 그대로 반환
    if len(arr) <= 1:
        return arr

    # 1. 분할 (Divide): 배열을 절반으로 나눔
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 2. 정복 (Conquer): 각 절반을 재귀적으로 정렬
    # left와 right는 결국 정렬된 상태로 반환됨
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # 3. 통합 (Combine): 정렬된 두 부분을 병합하여 반환
    return merge(left_sorted, right_sorted)

T = int(input())

for tc in range(1, T+1):
    # 인풋리스트 길이
    N = int(input())

    lst = list(map(int, input().split()))

    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 출력
    cnt = 0

    arr = merge_sort(lst)

    print(f"#{tc}", arr[N//2], cnt)