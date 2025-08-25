def check_babygin(check_list):
    one = check_list[:3]
    two = check_list[3:]

    # 베이비진이면 2가 됨
    result = 0
    # 만약 다 똑같은 숫자 or 연속하는 숫자
    if len(set(one)) == 1 or (one[1]-one[0]==1 and one[2]-one[1]==1):
        result += 1
    if len(set(two)) == 1 or (two[1]-two[0]==1 and two[2]-two[1]==1):
        result += 1

    return result


# 순열 모음 만드는 함수
def perm(selected, remaining): # 현재까지 선택된 원소 리스트 / 남은 원소 리스트
    global sample_arr

    # 원하는 길이만큼의 순열이 만들어지면 중지
    if not remaining:
        sample_arr.append(selected)
        return

    # 재귀 호출
    # 남아있는 원소들(remaining)을 하나씩 순회하며 다음 자리에 놓을 원소를 선택
    for i in range(len(remaining)):

        # i번째 원소를 선택
        pick = remaining[i]

        # i번째 원소를 제외한 새로운 '남은 원소' 리스트 생성
        new_remaining = remaining[:i] + remaining[i + 1 :]

        # 새로운 '선택된 원소'와 '남은 원소'로 자기 자신을 다시 호출
        perm(selected + [pick], new_remaining)


import sys

sys.stdin = open("babygin.txt")

T = int(input())

for t in range(1, T + 1):

    input_list = list(map(int, list(input().strip())))

    # 순열 집합 초기화
    sample_arr = []
    perm([], input_list)

    # 베이비진 찾을 때까지 검사
    flag = 'false'  # 찾았는지 여부

    # 순열 하나하나 검사해보기
    for check_list in sample_arr:
        result = check_babygin(check_list)

        # babygin이면 검사멈추고 1 반환
        if result == 2:
            flag = 'true'
            break

    print(f"#{t}", flag)