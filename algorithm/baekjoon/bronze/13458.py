import sys

# 시험장 수
N = int(sys.stdin.readline())

# 시험장의 응시자 수 정보
A = list(map(int, sys.stdin.readline().split()))

# 총 감독관이 감시하는 응시자수, 부감독관이 감시하는 응시자 수
B, C = map(int, sys.stdin.readline().split())

# 최소 감독관 수 초기화
anw = 0

for curr_room in A:
    # 현재 응시자 수에서 총감독관이 감시가능한 수를 빼고 남은 응시자 수
    left_student = curr_room - B
    # 총감독관 +1
    anw += 1

    # 만약 남은 학생 수가 0이하면 더이상 감독관 필요 없음
    if left_student <= 0:
        continue
    # 남은 학생 수가 부감독관이 감시하는 응시자 수 이하면
    elif left_student <= C:
        anw += 1
    else:
        # 부감독관으로 나눠떨어지는 몫만큼
        if left_student % C == 0:
            anw += left_student//C
        # 부감독관으로 나눠떨어지는 몫에 추가적으로 필요한 부감독관 + 1
        else:
            anw += left_student//C + 1
    
print(anw)