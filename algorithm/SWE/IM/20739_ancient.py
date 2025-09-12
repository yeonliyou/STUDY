import sys
sys.stdin = open('sample_in.txt')

T = int(input())

for t in range(1, T + 1):
    # 행, 열
    N, M = map(int, input().split())

    # 배열 만들기
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 최댓값 찾을 리스트 만들기
    max_list = []

    for row in range(N):
        for col in range(M):

            # 시작 기준 점이 1일 때만 검사
            if arr[row][col] == 1:

                # 열방향 1의 길이 초기화 (초기화 위치 실수 주의!!)
                col_cnt = 0

                # 오른 쪽으로 가능한 좌표까지 검사
                for col_dir in range(col, M):
                    # 만약 요소가 1이면 카운트 증가
                    if arr[row][col_dir] == 1:
                        col_cnt += 1
                        continue
                    else:   # 만약 col_cnt 초기화를 두번째 for문 바로 밑에서 했으면 바로 break로 가는 순간 그 전 기준 좌표에서 설정된 값이 그대로 쓰이게 됨
                        break
                
                # 행방향 1의 길이 초기화
                row_cnt = 0
                # 아래 쪽으로 가능한 좌표까지 검사
                for row_dir in range(row, N):
                    if arr[row_dir][col] == 1:
                        row_cnt += 1
                        continue
                    else:
                        break

                # 현재 기준점으로 부터 가로 방향, 세로 방향 중에 더 긴 값 추가
                max_list.append(max(col_cnt, row_cnt))
            # 체크 기준점이 1이 아니면 패스
            else:
                continue
                
    # 구조물이 없는 경우
    if max(max_list) <= 1:
        print(f"#{t}", 0)
    # 구조물이 있는 경우
    else:
        print(f"#{t}", max(max_list))
