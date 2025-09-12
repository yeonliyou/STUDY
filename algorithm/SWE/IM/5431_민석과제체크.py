import sys

#sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    # 수강생의 수, 과제를 제출한 사람의 수
    N, M = map(int, input().split())

    # 과제를 제출한 사람의 번호
    K = list(map(int, input().split()))

    # 전체 학생 리스트
    total_student_list = [i for i in range(1, N + 1)]

    # 과제를 낸 학생들은 학생 리스트에서 없애기
    for check in K:
        total_student_list.remove(check)

    # 과제 안낸 학생들 리스트
    total_student_list.sort()

    print(f"#{t}", *total_student_list)
