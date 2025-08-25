# 튜플로 묶어서 저장하면 더 보기 편할 것 같음

# 가위바위보 승자 판별
def fight(a, b, a_idx, b_idx):  # 각각 a의 가위바위보, b의 가위바위보, a의 번호, b의 번호
    # 만약 둘이 비기면
    if a == b:
        # 번호가 더 작은 학생이 이김
        return (a, a_idx) if a_idx < b_idx else (b, b_idx)
    # a가 이기는 경우
    elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
        return a, a_idx
    # b가 이기는 경우
    else:
        return b, b_idx

# 이긴 사람만 계속 올라가서 분리시킴
def split_until_win(arr, idx_list):
    # 만약 한명만 남으면 그 사람이 최종 승자
    if len(arr) == 1:
        return arr[0], idx_list[0]
    # 분할의 중간 인덱싱
    mid = (len(arr) - 1) // 2
    # 왼쪽 그룹 토너먼트 인덱싱
    left_card, left_idx = split_until_win(arr[:mid+1], idx_list[:mid+1])
    # 오른쪽 그룹 토너먼트 인덱싱
    right_card, right_idx = split_until_win(arr[mid+1:], idx_list[mid+1:])

    return fight(left_card, right_card, left_idx, right_idx)

# 테스트 개수
T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    idx_list = list(range(N))

    # 최종 승자 반환
    win_person, win_idx = split_until_win(arr, idx_list)
    print(f'#{t+1} {win_idx + 1}')
