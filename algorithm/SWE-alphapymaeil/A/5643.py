from collections import deque
import sys

sys.stdin = open("키순서_input.txt")

T = int(input())

for tc in range(1, T+1):
    # 학생 수
    N = int(input())

    # 인접행렬 만들기 (0행, 0열은 안씀)
    arr = [[0] * (N+1) for _ in range(N+1)]

    # 두 학생 비교 횟수
    M = int(input())

    # 방향 그래프의 인접 리스트 만들기
    for _ in range(M):
        # 행 -> 열
        s, t = map(int, input().split())

        # 해당 행 인덱스 < 해당 열 인덱스 이면 1
        arr[s][t] = 1

    # 답 초기화
    anw = 0

    # 학생 한명한명 체크해보기
    for curr_stu in range(1, N+1):
        # 현재 기준이 되는 학생보다 큰지 작은지를 확실히 알 수 있는 학생들 리스트
        known = [0] * (N+1)
        # 현재 기준 학생은 1로 기본 셋팅
        known[curr_stu] = 1

        # 각각 확실히 큰 애들, 작은 애들 체크하는 queue
        q = deque([curr_stu])

        # 1. 현재 기준 학생보다 확실히 큰 애들 다 체크
        while q:
            n_stu = q.popleft()
            # 나머지 학생들이랑 비교 순회
            for c in range(1, N+1):
                # 본인이 아니면서 and 체크해야 될 학생이라면
                ## and 뒤 조건 추가 안해주면 runtime error 뜸(이미 검사했던 애를 다음 q에서 또 하는 거니까)
                if arr[n_stu][c] == 1 and known[c] != 1:
                    # 확실히 현재 기준 학생보다 큰걸 알게됨
                    known[c] = 1
                    # 다음 검사할 q에 추가
                    q.append(c)

        # 모든 학생들이 크고 작음 여부를 안다면 anw +1 => 바로 다음 학생 넘어가기
        # 이미 1번째 while 문에서 자기 키 순서를 알게 됐으면 중지 (시간 save)
        if sum(known) == N:
            anw += 1
            continue

        # 각각 확실히 큰 애들, 작은 애들 체크하는 queue 초기화
        q = deque([curr_stu])

        # 2. 현재 기준 학생보다 확실히 작은 애들 다 체크
        while q:
            n_stu = q.popleft()
            # 나머지 학생들이랑 비교 순회
            for r in range(1, N+1):
                # 체크해야 될 학생이라면 (본인이면 어차피 arr 요소값 0)
                if arr[r][n_stu] == 1 and known[r] != 1:
                    # 확실히 현재 기준 학생보다 작은 걸 알게됨
                    known[r] = 1
                    # q에 추가
                    q.append(r)

        # 모든 학생들이 크고 작음 여부를 안다면 anw +1
        if sum(known) == N:
            anw += 1

    print(f"#{tc}", anw)
