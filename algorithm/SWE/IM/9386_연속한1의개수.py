# 생각보다 조금 오래걸린 느낌 ..

import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    # 테스트 케이스의 길이
    N = int(input())

    check_str = input()
    max_len = 0

    # 연속한 1의 개수
    cnt = 0

    for idx in range(N):
        # 인덱스 비교가 가능할 때
        if idx != N-1:
            # 지금 요소가 1이고
            if check_str[idx] == '1':
                # 다음 값도 1일때
                if check_str[idx + 1] == '1':
                    cnt += 1
                # 다음 값은 1이 아니라면 현재 1의 길이로 종료
                else:
                    cnt += 1
                    if cnt > max_len:  # 현재 최댓값 보다 크다면 갱신
                        max_len = cnt
                    cnt = 0  # 초기화
            # 지금 요소가 1이 아니면
            else:
                continue
        # 인덱스 비교가 불가능할 때 (리스트의 마지막 element)
        else:
            if check_str[idx] == '1':
                cnt += 1
            if cnt > max_len:  # 현재 최댓값 보다 크다면 갱신
                max_len = cnt  # 첫 시작 1을 안 더해서

    print(f"#{t}", max_len)





