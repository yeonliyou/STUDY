import sys
sys.stdin = open('sample_in.txt')

# 숫자를 반대로 바꿔주는 함수
def reverse_str(str):  # num = '0' or '1'
    if str == '0':
        return '1'
    else:
        return '0'
    
T = int(input())

for t in range(1, T + 1):
    # 돌의 수, 뒤집기 횟수
    N, M = map(int, input().split())
    # 돌의 초기 상태
    init_stone = list(input().split())
    
    # M번 뒤집는 반복
    for _ in range(M):
        # i번째 돌, 마주보는 j개의 돌 체크
        i, j = map(int, input().split())
        
        # 좌우 돌을 j번 만큼 같은지 체크하는 반복문
        for up in range(j):
            # 돌 pair를 찾을 수 있다면 진행 (초기 돌의 리스트 범위 안에서 try except 주의)
            # 리스트는 [-1] 처럼 음수 인덱싱이 가능하다는 점 주의
            if 0 <= (i - 2 - up) < N and 0 <= (i + up) <N:
                # 왼쪽 돌, 오른쪽 돌이 같으면 1->0, 0->1
                if init_stone[i - 2 - up] == init_stone[i + up]:
                    init_stone[i - 2 - up] = reverse_str(init_stone[i - 2 - up])
                    init_stone[i + up] = reverse_str(init_stone[i + up])
                else:
                    continue
            # 없다면 넘어가기
            else:
                break

    print(f"#{t}", *init_stone)