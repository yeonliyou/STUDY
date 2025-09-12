T = int(input())

for t in range(1, T + 1):
    # 학생수, 문항수
    N, M = map(int, input().split())

    total_score_list = []

    # 솔루션 리스트
    solution = list(map(int, input().split()))

    # 학생 정보 받기
    for _ in range(N):
        # 현재 학생의 답안지
        curr_sol = list(map(int, input().split()))

        # 현재 학생의 점수 초기화
        score_sum = 0

        # 현재 누적된 점수 기준
        curr_score = 1

        for idx in range(M):
            if solution[idx] == curr_sol[idx]:
                score_sum += curr_score  # 정답 점수 더하기
                curr_score += 1  # 점수 기준 증가
            else:
                curr_score = 1

        # 학생들 점수 리스트에 추가
        total_score_list.append(score_sum)

    print(f"#{t}", max(total_score_list) - min(total_score_list))

