import sys
sys.stdin = open('switch_sample_in.txt')

T = int(input())

# 숫자를 반대로 바꿔주는 함수
def reverse_number(num):  # num = 0 or 1
    if num == 0:
        return 1
    else:
        return 0

for t in range(1, T + 1):
    # 스위치 개수
    N = int(input())

    # 최소 조작 횟수 초기화
    cnt = 0

    # 조작전 스위치 상태
    before = list(map(int, input().split()))
    # 조작후 상태
    after = list(map(int, input().split()))

    for idx in range(N):
        # 해당 자리의 조작 전, 후가 같을 때
        if before[idx] == after[idx]:
            continue
        # 다를 때
        else:
            # 조작 횟수 증가
            cnt += 1
            # 현재 인덱스부터 끝가지 반대 숫자 할당하기
            for change_idx in range(idx, N):
                after[change_idx] = reverse_number(after[change_idx])

    print(f"#{t}", cnt)